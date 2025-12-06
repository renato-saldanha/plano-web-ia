#!/usr/bin/env python3
"""
Agent ReAct com Tools (Calculator + RAG) usando LangChain v1.0

Este exemplo demonstra como criar um Agent ReAct usando a API oficial do LangChain v1.0 que:
1) Decide autonomamente quando usar ferramentas.
2) Usa um calculator simples.
3) Reutiliza o RAG avançado do Dia 4 como tool (FAISS persistido).

Pré-requisitos:
- Ambiente virtual ativo.
- LangChain >= 1.0.0 instalado.
- .env com GROQ_API_KEY (prioridade); GOOGLE_API_KEY/ANTHROPIC_API_KEY como fallback.
- Vector store do Dia 4 persistido em ../Dia4/faiss_index (recrie no Dia 4 se ausente).

Fluxo do Agent:
User input -> Agent (create_agent v1.0) -> escolhe tools -> observa resultados -> responde.

NOTA: LangChain v1.0 introduziu `create_agent` como a API oficial para agents,
substituindo AgentExecutor clássico e langgraph.prebuilt.create_react_agent.
Documentação: https://docs.langchain.com/oss/python/releases/langchain-v1
"""

from __future__ import annotations

import os
from typing import Annotated

import re
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.agents import create_agent

# =============================================================================
# SEÇÃO 1: Configuração
# =============================================================================

load_dotenv()  # Carrega chaves de API do .env

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise RuntimeError("Defina GROQ_API_KEY no .env para usar o ChatGroq.")

# Caminho padrão do vector store criado no Dia 4
FAISS_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "Dia4", "faiss_index"))


# =============================================================================
# SEÇÃO 2: Tools (usando decorator @tool da API v1.0)
# =============================================================================

@tool
def calculadora(expressao: Annotated[str, "Expressão matemática para calcular, ex: '2+2' ou '10*5'"]) -> str:
    """
    Calcula uma expressão aritmética simples.
    
    Aceita apenas operações básicas (+, -, *, /, **, %) com números.
    Rejeita qualquer tentativa de código malicioso.
    
    Exemplos:
        calculadora("2 + 2") -> "4"
        calculadora("10 * 5") -> "50"
        calculadora("100 / 4") -> "25.0"
    """
    # PASSO 1: Validar segurança (aceitar apenas dígitos e operadores)
    if not re.match(r'^[\d\s\+\-\*\/\(\)\.\%\*\*]+$', expressao):
        return "Erro: Expressão inválida. Use apenas números e operadores (+, -, *, /, **, %)."
    
    # PASSO 2: Executar cálculo
    try:
        resultado = eval(expressao)  # noqa: S307 - uso controlado após validação
        return str(resultado)
    except Exception as e:
        return f"Erro ao calcular: {e}"


@tool
def buscar_conhecimento(pergunta: Annotated[str, "Pergunta para buscar em documentos"]) -> str:
    """
    Busca informações em documentos usando RAG avançado (busca semântica).
    
    Usa o vector store FAISS criado no Dia 4 com embeddings para encontrar
    documentos relevantes semanticamente e retorná-los como contexto.
    
    Use esta ferramenta quando precisar de informações específicas sobre
    tópicos documentados no sistema.
    
    Exemplos:
        buscar_conhecimento("O que é Python?")
        buscar_conhecimento("Explique LangChain")
    """
    # PASSO 1: Carregar vector store do Dia 4
    try:
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        vectorstore = FAISS.load_local(
            FAISS_DIR, 
            embeddings, 
            allow_dangerous_deserialization=True
        )
    except Exception as e:
        return f"Erro ao carregar vector store: {e}. Certifique-se de ter o Dia 4 completo."
    
    # PASSO 2: Buscar documentos relevantes (top 3)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    try:
        docs = retriever.invoke(pergunta)
        if not docs:
            return "Nenhum documento relevante encontrado."
        
        # PASSO 3: Concatenar conteúdo dos documentos
        contexto = "\n\n---\n\n".join([doc.page_content for doc in docs])
        return f"Documentos encontrados:\n\n{contexto}"
    except Exception as e:
        return f"Erro ao buscar: {e}"


# =============================================================================
# SEÇÃO 3: Criar Agent com LangChain v1.0
# =============================================================================

def criar_agent():
    """
    Cria um Agent ReAct usando create_agent (API oficial LangChain v1.0).
    
    O Agent:
    - Recebe uma lista de tools disponíveis.
    - Decide autonomamente qual tool usar baseado na pergunta.
    - Pode usar múltiplas tools em sequência.
    - Raciocina sobre os resultados e gera resposta final.
    
    Recursos v1.0:
    - Middleware: PIIMiddleware, SummarizationMiddleware, HumanInTheLoopMiddleware
    - Structured output: Respostas tipadas com Pydantic
    - Content blocks: Acesso unificado a reasoning traces
    
    Returns:
        Agent executável que pode ser invocado com .invoke()
    """
    # PASSO 1: Configurar LLM
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0,  # Determinístico para raciocínio consistente
        api_key=GROQ_API_KEY
    )
    
    # PASSO 2: Listar tools disponíveis
    tools = [calculadora, buscar_conhecimento]
    
    # PASSO 3: Criar agent com create_agent (v1.0)
    # create_agent é a API oficial que substitui AgentExecutor e langgraph.prebuilt
    agent_executor = create_agent(llm, tools)
    
    return agent_executor


# =============================================================================
# SEÇÃO 4: Função de execução principal
# =============================================================================

def executar_agent(pergunta: str, verbose: bool = True):
    """
    Executa o Agent com uma pergunta e retorna a resposta.
    
    Args:
        pergunta: Pergunta do usuário.
        verbose: Se True, imprime o raciocínio do Agent.
    
    Returns:
        Resposta final do Agent.
    """
    agent = criar_agent()
    
    # Invocar agent com mensagem
    # LangChain v1.0 espera formato: {"messages": [HumanMessage(...)]}
    resultado = agent.invoke(
        {"messages": [HumanMessage(content=pergunta)]},
        config={"recursion_limit": 10}  # Limite de iterações do agent
    )
    
    if verbose:
        print("\n" + "="*70)
        print("RACIOCÍNIO DO AGENT:")
        print("="*70)
        for mensagem in resultado["messages"]:
            tipo = type(mensagem).__name__
            conteudo = mensagem.content if hasattr(mensagem, 'content') else str(mensagem)
            print(f"\n[{tipo}]")
            print(conteudo)
        print("="*70 + "\n")
    
    # Retornar última mensagem (resposta final)
    return resultado["messages"][-1].content


# =============================================================================
# SEÇÃO 5: Exemplos de uso
# =============================================================================

if __name__ == "__main__":
    print("🤖 Agent ReAct com LangChain v1.0 - Dia 5")
    print("=" * 70)
    
    # EXEMPLO 1: Pergunta que precisa apenas de calculator
    print("\n📊 EXEMPLO 1: Cálculo simples")
    print("-" * 70)
    pergunta1 = "Quanto é 15 multiplicado por 8?"
    resposta1 = executar_agent(pergunta1, verbose=True)
    print(f"\n✅ Resposta final: {resposta1}")
    
    # EXEMPLO 2: Pergunta que precisa de RAG
    print("\n\n📚 EXEMPLO 2: Busca em documentos")
    print("-" * 70)
    pergunta2 = "O que você sabe sobre Python?"
    resposta2 = executar_agent(pergunta2, verbose=True)
    print(f"\n✅ Resposta final: {resposta2}")
    
    # EXEMPLO 3: Pergunta que pode precisar de ambas as tools
    print("\n\n🔀 EXEMPLO 3: Multi-tool")
    print("-" * 70)
    pergunta3 = "Se Python foi criado em 1991 e hoje é 2025, quantos anos tem a linguagem?"
    resposta3 = executar_agent(pergunta3, verbose=True)
    print(f"\n✅ Resposta final: {resposta3}")
    
    print("\n" + "=" * 70)
    print("🎉 Exemplos concluídos! Agent funcionando com LangChain v1.0.")
    print("=" * 70)
