#!/usr/bin/env python3
"""
exemplo_referencia.py — Knowledge Assistant (LangGraph ReAct Agent)

Propósito:
- Integrar duas tools (calculadora + RAG do Dia 4) em um fluxo ReAct
  usando langchain.agents import create_agent.
- Servir como referência para preencher `template.py`.

Como usar:
    python exemplo_referencia.py

Requisitos:
- `.env` com GROQ_API_KEY (ou provider alternativo).
- Diretório ../Dia4/faiss_index existente (recrie no Dia 4 se faltar).
- Python 3.12, dependências em requirements.txt.
"""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Annotated, List

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent


# --------------------------------------------------------------------------- #
# Configuração
# --------------------------------------------------------------------------- #
load_dotenv()
DEFAULT_MODEL = os.getenv("LANGGRAPH_MODEL", "llama-3.1-70b-versatile")
INDEX_PATH = Path(__file__).parent.parent / "Dia4" / "faiss_index"


def load_retriever():
    """Carrega o retriever FAISS persistido no Dia 4."""
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.load_local(
        INDEX_PATH,
        embeddings,
        allow_dangerous_deserialization=True,
    ).as_retriever(search_kwargs={"k": 3})


@tool
def calculadora(expressao: Annotated[str, "Expressão matemática simples, ex: '2+2'"]) -> str:
    """
    Use para contas aritméticas simples (+ - * /). Evite texto longo.
    Faz uma validação leve para evitar código malicioso.
    """
    if not re.fullmatch(r"[0-9+\-*/().\s]+", expressao):
        return "Expressão inválida. Use apenas dígitos e + - * / ( ) ."
    try:
        resultado = eval(expressao)  # noqa: S307 (uso educativo)
        return str(resultado)
    except Exception as exc:  # noqa: BLE001
        return f"Erro ao calcular: {exc}"


_retriever_cache = None


@tool
def buscar_conhecimento(pergunta: Annotated[str, "Pergunta que depende dos documentos do Dia 4 (FAISS)"]) -> str:
    """
    Busca informações no corpus do Dia 4 via retriever FAISS.
    Retorna trechos concatenados. Use quando a pergunta requer contexto documental.
    """
    global _retriever_cache
    if _retriever_cache is None:
        _retriever_cache = load_retriever()
    docs = _retriever_cache.get_relevant_documents(pergunta)
    if not docs:
        return "Nenhum documento relevante encontrado."
    trechos: List[str] = [doc.page_content for doc in docs]
    return "\n---\n".join(trechos)


def build_agent():
    """Constroi o agent ReAct com LangGraph usando as duas tools."""
    llm = ChatGroq(model=DEFAULT_MODEL, temperature=0)
    tools = [calculadora, buscar_conhecimento]
    return create_react_agent(llm, tools)


def demo():
    """Roda 3 consultas de exemplo e imprime a resposta final do agent."""
    agent = build_agent()
    casos = [
        "Some 321 + 456",
        "Explique em 2 frases a diferença entre embeddings e BM25.",
        "Qual a capital da França e 13*7?",
    ]
    for query in casos:
        result = agent.invoke(
            {"messages": [HumanMessage(content=query)]},
            config={"recursion_limit": 8, "run_name": "dia6-demo"},
        )
        final_message = result["messages"][-1].content
        print(f"\n[Consulta] {query}\n[Resposta]\n{final_message}")


if __name__ == "__main__":
    demo()

