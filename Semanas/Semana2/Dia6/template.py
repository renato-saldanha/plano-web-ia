#!/usr/bin/env python3
"""
Template - Knowledge Assistant (LangGraph)

Objetivo: Integrar tools (calculator + RAG do Dia 4) em um fluxo ReAct com
langgraph.prebuilt.create_react_agent.

TODO: Preencher docstrings, validações e prompt base antes de rodar.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Annotated

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent


# TODO: Ajuste se usar outro modelo ou provider
DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")


def load_env() -> None:
    """Carrega variáveis de ambiente (.env) para usar a API do LLM."""
    load_dotenv()


def load_retriever():
    """
    Descrever o retriever (origem: Dia 4, FAISS, embeddings HuggingFace).

    Returns:
        Retriever configurado com search_kwargs={"k": 3}.
    """
    base = Path(__file__).parent.parent / "Dia4" / "faiss_index"
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.load_local(
        base,
        embeddings,
        allow_dangerous_deserialization=True,
    ).as_retriever(
        search_kwargs={"k": 3},
        search_function = "simirality"
    )


@tool
def calculadora(expressao: Annotated[str, "Expressão aritmética simples, ex: '2+2'"]) -> str:
    """
    Quando usar: Use para contas aritméticas simples (+ - * /). Evite texto longo.
    """
    try:
        # TODO: adicionar validação leve (permitir apenas dígitos e operadores básicos)
        resultado = eval(expressao)  # noqa: S307 (apenas para fins educacionais)
        return str(resultado)
    except Exception as exc:  # noqa: BLE001
        return f"Erro ao calcular: {exc}"


def _load_retriever_once():
    # Cache leve para evitar reabrir FAISS a cada chamada
    if not hasattr(_load_retriever_once, "_cache"):
        _load_retriever_once._cache = load_retriever()
    return _load_retriever_once._cache


@tool
def buscar_conhecimento(pergunta: Annotated[str, "Pergunta que precisa de contexto nos documentos do Dia 4"]) -> str:
    """
    Efetua busca no banco vetorizado utilizando FAISS.
    Cria Chain para efetuar a busca no banco.
    Responde somente a perguntas relacionadas ao documento FAISS.

    Args: answer-> 'Me fale sobre Engenharia de Softwares'
    Return: str-> 'Engenharia de Software é...' 

    Ex: certo: 'O que é Arquitetura de Software? -> 'Arquitetura de Software é...'
        incorreto: 'Qual a capital de Mato Grosso? -> 'Não sei responder...'
    """

    retriever = _load_retriever_once()
    docs = retriever.invoke(pergunta)
    if not docs:
        return "Nenhum documento relevante encontrado."
    trechos = [doc.page_content for doc in docs]
    return "\n---\n".join(trechos)


def build_agent():
    """
    Agente que responde as perguntas somente usando as tools calculator e search_knowledges.
    Se não souber diga: 'Eu não sou capaz de responder essa pergunta.'.
    """
    load_env()
    llm = ChatOpenAI(model = "gpt-4o-mini")
    tools = [calculadora, buscar_conhecimento]
    return create_agent(llm, tools)


def run_demo():
    """
    Executa três consultas de exemplo:
    1) Só cálculo
    2) Só RAG
    3) Pergunta mista (RAG + cálculo)
    """
    agent = build_agent()
    queries = [
        "Some 789 + 432?",
        "Me fale sobre Engenharia de Softwares.",
        "Qual é a capital da França e quanto é 13*7?",
    ]
    for query in queries:
        result = agent.invoke(
            {"messages": [HumanMessage(content=query)]},
            config={"recursion_limit": 8, "run_name": "dia6-demo"},
        )
        final_message = result["messages"][-1].content
        print(f"\n[Query] {query}\n[Resposta]\n{final_message}")


if __name__ == "__main__":
    run_demo()

