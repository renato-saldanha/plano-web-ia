"""
## Exercício 2 — RAG-only (Conceitual)
- Pergunta: `Explique em 2 frases a diferença entre embeddings e BM25.`
- Esperado: usar **buscar_conhecimento** apenas.
- Se escolher calculadora, reforce docstring do RAG: “Use para perguntas conceituais baseadas no corpus do Dia 4 (FAISS)”.colher RAG, fortaleça a docstring da calculadora deixando explícito “Use para contas aritméticas simples”.
"""

from __future__ import annotations

import os
from pathlib import Path
from dotenv import load_dotenv
from typing import Annotated

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.tools import tool
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent


load_dotenv()

llm_openai = ChatOpenAI(model="gpt-4o-mini", temperature=0)

model = llm_openai

def load_retriever() -> FAISS:
    """ Cria e retorna uma instância do retriever """
    # Carrrega o caminho o banco
    base_path = Path(__file__).resolve().parents[2] / "Dia4" / "faiss_index"
    # Define o embedding
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    # Retorna a instância de um retriever
    return FAISS.load_local(
        base_path,
        embeddings,
        allow_dangerous_deserialization = True,
    ).as_retriever(
        search_type = "similarity",
        search_kwargs = {"k": 6}
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
    Efetua busca no banco vetorizado utilizando FAISS.
    Responde somente a perguntas relacionadas ao documento FAISS.

    Args: answer-> 'Me fale sobre Engenharia de Softwares'
    Return: str-> 'Engenharia de Software é...' 

    Ex: certo: 'O que é Arquitetura de Software? -> 'Arquitetura de Software é...'
        incorreto: 'Qual a capital de Mato Grosso? -> 'Não sei responder...'
    """
    
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    SYSTEM_MESSAGE = """Somente responda perguntas que tenham relação com o contexto.
    Se não souber diga: 'Não encontrado na base de conhecimento.'"""

    HUMAN_MESSAGE = """Contexto:
    {context}

    Pergunta:{answer}
    Resposta:"""

    prompt = ChatPromptTemplate([
        ("system", SYSTEM_MESSAGE),
        ("human", HUMAN_MESSAGE)
    ])

    retriever = load_retriever()

    knowledge_chain = (
        {
            "context": retriever | format_docs,
            "answer": RunnablePassthrough()
        }
        | prompt
        | model
        | StrOutputParser()
    )

    try:
        resposta = knowledge_chain.invoke(answer)
    except Exception as e:
        return f"Não foi possível executar a Tool search_knowledges\n{e}"

    return resposta

def build_agent():
    """
    Cria As Tools e define o Agent ReAct
    Return: Instância do Agent
    """

    tools = [search_knowledges, calculator]

    agent_executor = create_agent(model, tools)

    return agent_executor

def execute_agent(content: str):
    agent = build_agent()

    system = SystemMessage(content = """
    Agente que responde as perguntas somente usando as tools calculator e search_knowledges.
    Se não souber diga: 'Eu não sou capaz de responder essa pergunta.'.    
    """)
    messages = HumanMessage(content = content)

    try:
         agent_content = agent.invoke(
            {
                "messages": [system, messages]
            }
        )
    except Exception as e:
        return f"Não foi possível definir o agente."

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
    execute_agent("Me fale sobre Engenharia de Softwares.")        
    execute_agent("Explique em 2 frases a diferença entre embeddings e BM25.")


