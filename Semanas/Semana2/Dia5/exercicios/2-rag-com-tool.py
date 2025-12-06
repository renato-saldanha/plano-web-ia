# Exercício 1 — Calculator Tool
# - Implemente uma variação da tool que suporte potência (`**`) de forma segura.
# - Teste com: `2**5 + 10`.

from __future__ import annotations

import os
from typing import Annotated

import re
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.tools import tool
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

load_dotenv()

if not os.getenv("GROQ_API_KEY"):
    raise Exception(".env não configurado.")

llm_groq = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
)

llm_openai = ChatOpenAI(model="gpt-4o-mini")

modelo = llm_openai

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")


@tool
def search_knowledges(answer: str) -> str:
    """
    Recebe a pergunta.
    Retira a palavra-chave da pergunta e retorna
    Processa o chain e retorna o resultado.

    Ex:
        search_knowledges("O que é Java?") - > 'Java é uma li...'
            palavra-chave: 'Java'
    """

    def format_docs(docs):
        return "\n\n".join([doc.page_content for doc in docs])

    def return_keyword(answer):
        template = f"""Retorne SOMENTE a palavra-chave da pergunta.
        Seja preciso e atento.
        Pergunta:{answer}\n\nPalavra-Chave:
        """

        prompt = ChatPromptTemplate.from_template(template)
        key_chain = prompt | modelo

        response = key_chain.invoke({
            "answer": answer,
        })

        return response.content

    keyword = return_keyword(answer)

    path = "F:\\Projetos\\plano web+ia\\Semanas\\Semana2\\Dia4\\faiss_index"
    vectorstore = FAISS.load_local(
        path,
        embeddings,
        allow_dangerous_deserialization=True,
    )
    retriever = vectorstore.as_retriever(search_kwargs={"k": 10})
    print("Retriever")

    key_docs = retriever.invoke(keyword)

    print("Documento encontrados por palavra-chave")
    for i, doc in enumerate(key_docs, 1):
        if keyword in doc.page_content:
            print(f"Documento{i}: {doc.page_content}")
            print("-" * 60)

    # Define os templates do prompt
    SYSTEM_TEMPLATE = """Responda a pergunta SOMENTE com base nos contextos.
    NUNCA invente uma informação. Não alucine.
    Não forneça informação fora dos contextos.
    Compare ambos contextos e retorne em uma lista rankeada.
    """
    HUMAN_TEMPLATE = "Contextos:\n{context}\n\nPergunta: {answer}\n\nResposta:\n"

    # Define o prompt
    searched_prompt = ChatPromptTemplate([
        ("system", SYSTEM_TEMPLATE),
        ("human", HUMAN_TEMPLATE)
    ])

    # Define a chain
    searched_chain = (
        {
            "context": retriever | format_docs,
            "answer": RunnablePassthrough(),
        }
        | searched_prompt
        | llm_groq
        | StrOutputParser()
    )

    # Recebe o top 10 da busca semântica
    searched_docs = searched_chain.invoke(answer)

    print("Informações relevantes")
    print(searched_docs)

    return searched_docs


def agent_create():
    """
    Cria um Agent ReAct

    O Agent:
        Recebe uma lista de tools
        Decide autonomamente qual tool usar com base na pergunta
        Pode usar múltiplas tools em sequência
        Raciocina sobre os resultados e gera resposta final

    Returns:
        Agent invocado com .invoke()
    """

    tools = [search_knowledges]

    agent_executor = create_agent(modelo, tools)

    return agent_executor


def agent_execute(content: str, verbose: bool = True):
    """
    Executa o Agent com uma pergunta e retorna a resposta.

    Args:
        pergunta: Pergunta do usuário.
        verbose: Se True, imprime o raciocínio do Agent.

    Returns:
        Resposta final do Agent.
    """

    agent = agent_create()

    resultado = agent.invoke(
        {"messages": [HumanMessage(content=content)]},
    )

    if verbose:
        print("\n" + "="*70)
        print("RACIOCÍNIO DO AGENT:")
        print("="*70)

        for message in resultado["messages"]:
            tipo = type(message).__name__
            content = message.content if hasattr(
                message, "content") else str(message)
            print(f"\n[{tipo}]")
            print(content)
        print("="*70 + "\n")

        return resultado["messages"][-1].content


if __name__ == "__main__":
    # Ex 1
    print("\n EXEMPLO 1: Busca em docs")
    print("-" * 70)
    pergunta3 = "O que é vermelho?"
    resposta3 = agent_execute(pergunta3)
    print(f"\n✅ Resposta final: {resposta3}")
