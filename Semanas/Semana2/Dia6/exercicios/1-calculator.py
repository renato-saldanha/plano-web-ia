"""
## Exercício 1 — Calculator-only (Smoke)
- Pergunta: `Some 789 + 432`
- Esperado: usar **calculadora** apenas.
- Se escolher RAG, fortaleça a docstring da calculadora deixando explícito “Use para contas aritméticas simples”.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Annotated

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.tools import tool
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langgraph.graph.state import CompiledStateGraph


load_dotenv()

# Define o embedding
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",    
)

llm_openai = ChatOpenAI(model="gpt-4o-mini", temperature=0)

model = llm_openai


def load_retriever() -> FAISS:
    """ Cria e retorna uma instância do retriever """
    # Carrrega o caminho o banco
    base_path = Path(__file__).resolve().parents[2] / "Dia4" / "faiss_index"
    
    # Retorna a instância de um retriever
    return FAISS.load_local(
        base_path,
        embeddings,
        allow_dangerous_deserialization = True,
    ).as_retriever(
        search_type = "similarity",
        search_kwargs = { "k": 3}
    )


@tool
def calculator(expression: Annotated[str, "Expressão aritimética simple. Exemplo: 2*10-> 20"]) -> str:
    """
    @@Tool@@

    Efetua calculos matemáticos usando expressões aritméticas simple.
    Usar textos curtos.

    Args: expression: 'Expressão a ser processada'

    Return: Resultado com o eval da expression

    Ex: certo: 'Quanto é 3 + 10?' -> '13'
        incorreto: 'Onde fica o centro geodezico da América do Sul?' -> 'Não sei resposer...'
    """

    try:
        # Retorna o resultado de uma expressão aritmética simples
        resultado = eval(expression)
    except Exception as e:
        return f"Erro ao tentar calcular.\n{e}"

    return resultado

@tool
def search_knowledges(answer: Annotated[str, "Pergunta que depende do documento Dia 4 FAISS"]):
    """
    @@Tool@@

    Efetua busca no banco vetorizado utilizando FAISS
    Cria Chain para efetuar a busca no banco

    Args: answer-> 'Me fale sobre Engenharia de Softwares'
    Return: str-> 'Engenharia de Software é...' 

    Ex: certo: 'O que é Engenharia de Software? -> 'Engenharia de Software é...'
        incorreto: 'Qual a capital de Mato Grosso? -> 'Não sei responder...'
    """
    
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    SYSTEM_MESSAGE = """Efetua busca no banco vetorizado utilizando FAISS.
    Não invente.
    Não alucine.
    Se não souber diga: 'Eu não sou capaz de responder essa pergunta.'.    
    """
    HUMAN_MESSAGE = "Contexto:\n{context}\n\nPergunta: {answer}\nResposta:"

    template = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_MESSAGE),
        ("human", HUMAN_MESSAGE)
    ])

    retriever = load_retriever()

    knowledge_chain = (
        {
            "context": retriever | format_docs,
            "answer": RunnablePassthrough()
        }
        | template
        | model
        | StrOutputParser()
    )

    resposta = knowledge_chain.invoke(answer)

    return resposta


def build_agent() -> CompiledStateGraph:
    """
    Cria As Tools e define o Agent ReAct
    Return: Instância do Agent
    """

    # Cria as tools
    tools = [calculator, search_knowledges]

    # Define o Agent ReAct
    agent_executor = create_agent(llm_openai, tools)

    return agent_executor


def execute_agent(content: str, verbose: bool = True) -> str:
    agent_executor = build_agent()

    messages = HumanMessage(content=content)

    agent_content = agent_executor.invoke(
        {
            "messages": [messages]
        }
    )

    response = agent_content["messages"][-1].content
    print("\n" + "="*70)
    print("RACIOCÍNIO DO AGENT:")
    print("="*70)

    for message in agent_content["messages"]:
        tipo = type(message).__name__
        content = message.content if hasattr(message, "content") else str(message)
        print(f"\n[{tipo}]")
        print(content)
    print("="*70 + "\n")

    return response


if __name__ == "__main__":
    execute_agent("Some 789 + 432")
    execute_agent("O que é Engenharia de Softwares?")
    execute_agent("Qual carro é amarelo?")
