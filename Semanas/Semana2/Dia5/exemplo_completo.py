#!/usr/bin/env python3
"""
Agent ReAct com Tools (Calculator + RAG)

Este exemplo demonstra como criar um Agent ReAct usando LangChain que:
1) Decide autonomamente quando usar ferramentas.
2) Usa um calculator simples.
3) Reutiliza o RAG avançado do Dia 4 como tool (Chroma persistido).

Pré-requisitos:
- Ambiente virtual ativo.
- .env com GROQ_API_KEY (prioridade); GOOGLE_API_KEY/ANTHROPIC_API_KEY como fallback.
- Vector store do Dia 4 persistido em ../Dia4/chroma_db (recrie no Dia 4 se ausente).

Fluxo do Agent:
User input -> Agent (ReAct) -> escolhe tools -> observa resultados -> responde.
"""

from __future__ import annotations

import os
import re
from typing import Callable, List

from dotenv import load_dotenv
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import Tool
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# =============================================================================
# SEÇÃO 1: Configuração
# =============================================================================

load_dotenv()  # Carrega chaves de API do .env

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise RuntimeError("Defina GROQ_API_KEY no .env para usar o ChatGroq.")

# Caminho padrão do vector store criado no Dia 4
CHROMA_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "Dia4", "chroma_db"))


# =============================================================================
# SEÇÃO 2: Tools
# =============================================================================

def _is_safe_expression(expr: str) -> bool:
    """Valida expressão simples para evitar eval inseguro."""
    return bool(re.fullmatch(r"[0-9+\-*/().\s]+", expr))


def somar(numeros: str) -> str:
    """
    Calcula expressões matemáticas simples.

    Args:
        numeros: string com expressão, ex.: "13*7" ou "123 + 456".
    """
    expr = numeros.strip()
    if not _is_safe_expression(expr):
        return "Expressão não permitida. Use apenas dígitos e + - * / ()"
    try:
        return str(eval(expr))  # noqa: S307 - uso controlado após validação
    except Exception as exc:  # pragma: no cover - caminho de erro genérico
        return f"Erro ao calcular: {exc}"


def criar_rag_tool(chroma_dir: str = CHROMA_DIR) -> Tool:
    """
    Cria a tool de RAG a partir do vector store persistido no Dia 4.
    Retorna Tool pronta para ser usada pelo Agent.
    """
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma(
        persist_directory=chroma_dir,
        embedding_function=embeddings,
    )
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    def buscar_conhecimento(query: str) -> str:
        """Busca informações nos documentos persistidos (Dia 4) usando RAG."""
        docs = retriever.invoke(query)
        if not docs:
            return "Nenhum documento encontrado. Recrie o vector store do Dia 4."
        return "\n\n".join([doc.page_content for doc in docs])

    return Tool(
        name="buscar_conhecimento",
        description=(
            "Use para buscar informações em documentos persistidos do Dia 4 (RAG avançado). "
            "Ideal para perguntas que exigem contexto/documentação."
        ),
        func=buscar_conhecimento,
    )


def build_tools() -> List[Tool]:
    """Monta lista de tools disponíveis para o Agent."""
    return [
        Tool(
            name="calculator",
            description="Use para cálculos aritméticos simples (somar, subtrair, multiplicar, dividir).",
            func=somar,
        ),
        criar_rag_tool(),
    ]


# =============================================================================
# SEÇÃO 3: Prompt do Agent (ReAct)
# =============================================================================

SYSTEM_PROMPT = """Você é um agente que usa ferramentas para responder.
Siga o padrão: Pensamento -> Ação -> Observação, e repita até concluir.
Use calculator para contas; use buscar_conhecimento para dados em documentos (Dia 4)."""

HUMAN_PROMPT = """Responda ao usuário escolhendo ferramentas quando precisar.
Sempre mostre raciocínio passo a passo (thoughts) no verbose.
Pergunta: {input}"""

PROMPT = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEM_PROMPT),
        ("human", HUMAN_PROMPT),
    ]
)


# =============================================================================
# SEÇÃO 4: Factory do Agent
# =============================================================================

def build_agent() -> AgentExecutor:
    """Cria AgentExecutor configurado com ReAct + tools."""
    llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)  # determinístico
    tools = build_tools()
    agent = create_react_agent(llm=llm, tools=tools, prompt=PROMPT)
    return AgentExecutor(agent=agent, tools=tools, verbose=True)


# =============================================================================
# SEÇÃO 5: Execução principal (exemplos)
# =============================================================================

def main() -> None:
    agent_executor = build_agent()

    exemplos = [
        "Some 123 + 456",
        "Qual é a diferença entre embeddings e BM25?",
        "Qual a capital da França e quanto é 13*7?",
    ]

    for pergunta in exemplos:
        print("=" * 80)
        print(f"Pergunta: {pergunta}")
        try:
            resposta = agent_executor.invoke({"input": pergunta})
            print("Resposta:", resposta["output"])
        except Exception as exc:  # pragma: no cover - execução manual
            print("Falhou:", exc)


if __name__ == "__main__":
    main()

