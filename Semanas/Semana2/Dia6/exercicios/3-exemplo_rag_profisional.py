#!/usr/bin/env python3
"""RAG profissional com FAISS, busca híbrida, reranker opcional e agente."""

from __future__ import annotations

import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Dict, Iterable, List, Optional, Tuple

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field
from langchain_community.document_transformers import (
    EmbeddingsRedundantFilter,
    LongContextReorder,
)
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_community.retrievers import BM25Retriever
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter

try:
    from sentence_transformers import CrossEncoder
except Exception:  # pragma: no cover - dependência opcional
    CrossEncoder = None  # type: ignore


load_dotenv()

DEFAULT_MODEL = os.getenv("LLM_MODEL", "gpt-4o-mini")
EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2"
)
DEFAULT_INDEX_PATH = Path(__file__).parent / "faiss_index"


# --------------------------------------------------------------------------- #
# Dados de exemplo para estudo (substitua por seus PDFs/CSVs/etc)
# --------------------------------------------------------------------------- #
def _sample_docs():
    from langchain_core.documents import Document

    return [
        Document(
            page_content=(
                "RAG (Retrieval Augmented Generation) combina busca de contexto "
                "com geração. Usa um retriever para buscar chunks relevantes e um "
                "LLM para responder apenas com base no contexto recuperado."
            ),
            metadata={"source": "guides/rag_intro"},
        ),
        Document(
            page_content=(
                "FAISS é uma biblioteca para busca vetorial eficiente. É usada para "
                "indexar embeddings e recuperar similaridade rapidamente."
            ),
            metadata={"source": "guides/faiss"},
        ),
        Document(
            page_content=(
                "BM25 é um método de busca lexical (full-text). Pode ser combinado "
                "com vetores para buscas híbridas, equilibrando precisão semântica "
                "e textual."
            ),
            metadata={"source": "guides/bm25"},
        ),
        Document(
            page_content=(
                "Rerankers reordenam resultados usando modelos cross-encoder. "
                "Eles avaliam pares (query, documento) para melhorar o ranking."
            ),
            metadata={"source": "guides/rerank"},
        ),
    ]


# --------------------------------------------------------------------------- #
# Indexação e carregamento
# --------------------------------------------------------------------------- #
def _build_splitter() -> RecursiveCharacterTextSplitter:
    return RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        separators=["\n\n", "\n", ". ", " ", ""],
    )


def build_or_load_faiss(
    index_path: Path = DEFAULT_INDEX_PATH,
    docs: Optional[Iterable] = None,
) -> FAISS:
    """Cria (se não existir) ou carrega um índice FAISS com embeddings HF."""
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    if index_path.exists():
        return FAISS.load_local(
            str(index_path),
            embeddings,
            allow_dangerous_deserialization=True,
        )

    base_docs = list(docs) if docs is not None else _sample_docs()
    splitter = _build_splitter()
    splits = splitter.split_documents(base_docs)

    redundancy_filter = EmbeddingsRedundantFilter(embeddings=embeddings)
    splits = redundancy_filter.transform_documents(splits)

    reorder = LongContextReorder()
    splits = reorder.transform_documents(splits)

    store = FAISS.from_documents(splits, embeddings)
    store.save_local(str(index_path))
    return store


# --------------------------------------------------------------------------- #
# Reranker opcional
# --------------------------------------------------------------------------- #
def load_reranker(model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2"):
    """Carrega CrossEncoder se disponível; caso contrário retorna None."""
    if CrossEncoder is None:
        return None
    try:
        return CrossEncoder(model_name)
    except Exception:
        return None


def apply_rerank(
    reranker,
    query: str,
    docs_with_scores: List[Tuple],
    top_k: int,
) -> List[Tuple]:
    """Aplica reranker (cross-encoder). Se indisponível, retorna original."""
    if reranker is None:
        return docs_with_scores[:top_k]

    pairs = [(query, doc.page_content) for doc, _ in docs_with_scores]
    scores = reranker.predict(pairs)
    reranked = list(zip(scores, docs_with_scores))
    reranked.sort(key=lambda x: x[0], reverse=True)
    return [(doc, float(rerank_score)) for rerank_score, (doc, _) in reranked[:top_k]]


# --------------------------------------------------------------------------- #
# Cliente de busca (vetorial, lexical, híbrida)
# --------------------------------------------------------------------------- #
def _normalize_vector_score(distance: float) -> float:
    return 1.0 / (1.0 + distance)


@dataclass
class SearchResult:
    content: str
    score: float
    source: str


def build_search_client(
    index_path: Path = DEFAULT_INDEX_PATH,
    search_type: str = "hybrid",
    top_k: int = 5,
    match_threshold: Optional[float] = None,
    reranker_model: Optional[str] = None,
) -> Callable[[str], List[SearchResult]]:
    store = build_or_load_faiss(index_path)
    docs_corpus = list(store.docstore._dict.values())

    bm25 = BM25Retriever.from_documents(docs_corpus)
    bm25.k = top_k

    reranker = load_reranker(reranker_model) if reranker_model else None

    def search(
        query: str,
        *,
        top_k_override: Optional[int] = None,
        match_threshold_override: Optional[float] = None,
    ) -> List[SearchResult]:
        candidates: Dict[str, Tuple] = {}
        k = top_k_override or top_k
        threshold = (
            match_threshold if match_threshold_override is None else match_threshold_override
        )
        bm25.k = k

        if search_type in {"vector", "hybrid"}:
            for doc, dist in store.similarity_search_with_score(query, k=k * 2):
                score = _normalize_vector_score(dist)
                key = doc.metadata.get("source", doc.page_content[:50])
                if key not in candidates or score > candidates[key][1]:
                    candidates[key] = (doc, score)

        if search_type in {"text", "hybrid"}:
            for doc in bm25.invoke(query):
                score = float(doc.metadata.get("score", 0.0))
                key = doc.metadata.get("source", doc.page_content[:50])
                if key not in candidates or score > candidates[key][1]:
                    candidates[key] = (doc, score)

        docs_with_scores = list(candidates.values())
        docs_with_scores.sort(key=lambda x: x[1], reverse=True)

        docs_with_scores = apply_rerank(reranker, query, docs_with_scores, top_k)

        results: List[SearchResult] = []
        for doc, score in docs_with_scores:
            if threshold is not None and score < threshold:
                continue
            results.append(
                SearchResult(
                    content=doc.page_content,
                    score=round(float(score), 4),
                    source=str(doc.metadata.get("source", "unknown")),
                )
            )
        return results

    return search


# --------------------------------------------------------------------------- #
# Tool de busca para o agente
# --------------------------------------------------------------------------- #
def build_agent_search_tool(search_fn: Callable[[str], List[SearchResult]]) -> StructuredTool:
    class SearchArgs(BaseModel):
        query: str = Field(..., description="Pergunta a ser pesquisada.")
        search_type: str = Field(
            "hybrid",
            description="Tipo de busca: vector | text | hybrid.",
            pattern="^(vector|text|hybrid)$",
        )
        top_k: int = Field(5, ge=1, le=20, description="Quantidade de resultados.")
        match_threshold: Optional[float] = Field(
            None, ge=0.0, le=1.0, description="Filtra por score mínimo."
        )

    def _run(
        query: str,
        search_type: str = "hybrid",
        top_k: int = 5,
        match_threshold: Optional[float] = None,
    ) -> str:
        _ = search_type  # Mantido para assinatura; search_fn já está configurado.
        results = search_fn(
            query,
            top_k_override=top_k,
            match_threshold_override=match_threshold,
        )
        if not results:
            return "Nenhum resultado relevante encontrado."

        lines = []
        for idx, item in enumerate(results, start=1):
            lines.append(
                f"[{idx}] score={item.score} source={item.source}\n{item.content[:500]}"
            )
        return "\n\n".join(lines)

    return StructuredTool.from_function(
        func=_run,
        name="pesquisa_contexto",
        description=(
            "Busca conhecimento em FAISS/BM25. Use antes de responder. "
            "search_type suportado: vector, text, hybrid. Ajuste top_k e match_threshold."
        ),
        args_schema=SearchArgs,
    )


# --------------------------------------------------------------------------- #
# Agente orquestrador
# --------------------------------------------------------------------------- #
SYSTEM_PROMPT = (
    "Você é um agente de respostas factuais. "
    "Use SEMPRE a ferramenta de busca antes de responder. "
    "Responda somente com base nos trechos retornados. "
    "Se não houver contexto suficiente, diga que não encontrou."
)


def build_agent(search_fn: Callable[[str], List[SearchResult]]):
    llm = ChatOpenAI(model=DEFAULT_MODEL, temperature=0)
    search_tool = build_agent_search_tool(search_fn)
    agent = create_agent(model=llm, tools=[search_tool])
    return agent, search_tool


def run_agent(agent, query: str) -> str:
    result = agent.invoke(
        {
            "messages": [
                SystemMessage(content=SYSTEM_PROMPT),
                HumanMessage(content=query),
            ]
        },
        config={"recursion_limit": 6, "run_name": "rag-agent"},
    )
    return result["messages"][-1].content


# --------------------------------------------------------------------------- #
# Demonstração
# --------------------------------------------------------------------------- #
def demo():
    print(">> Construindo/Carregando índice FAISS...")
    store = build_or_load_faiss() 
    print(f"Index carregado com {len(store.docstore._dict)} documentos.")

    search_fn = build_search_client(
        index_path=DEFAULT_INDEX_PATH,
        search_type="hybrid",
        top_k=5,
        match_threshold=0.25,
        reranker_model="cross-encoder/ms-marco-MiniLM-L-6-v2",  # Altere para ativar: "cross-encoder/ms-marco-MiniLM-L-6-v2" \ None
    )

    agent, _ = build_agent(search_fn)

    consultas = [
        "O que é RAG e quando usar?",
        "Explique FAISS em 2 frases.",
        "O que é BM25 e por que combinar com busca vetorial?",
        "Para que serve um reranker em RAG?",
    ]

    for q in consultas:
        print("\n" + "-" * 70)
        print(f"Pergunta: {q}")
        resposta = run_agent(agent, q)
        print("Resposta:", resposta)


if __name__ == "__main__":
    demo()

