"""
## Exercício 1 - RAG completo com comparação de STUFF e MapReduce

"""


from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
import os
import random
import time
from dotenv import load_dotenv  
from pathlib import Path
from typing import Annotated


from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.tools import tool
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain.agents import create_agent


load_dotenv()

# Define llms
llm_groq = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
)

llm_openai = ChatOpenAI(
    model = "gpt-4o-mini",
    temperature = 0,
)

# Troca de modelo
def model_changed(model = ChatGroq | ChatOpenAI):
    if model is ChatOpenAI: 
        return llm_groq
    else:
        return llm_openai


def load_retriever():
    """ Criado para evitar de ter loop na criaç~çao do Retriever """
    base_path = Path(__file__).resolve().parents[2] / "Dia4" / "faiss_index"
    embeddings = HuggingFaceEmbeddings(model_name = "all-MiniLM-L6-v2")

    return FAISS.load_local(
       base_path,
       embeddings,
       allow_dangerous_deserialization = True, 
    ).as_retriever(
        search_type = "similarity",
        search_kwargs = {"k": 6}
    )

@tool
def search_knowledges(answer: Annotated[str, "Pergunta que depende do documento Dia 4 FAISS"]):
    """
    @@Tool@@

    Responde perguntas somente com base no documento FAISS.    

    Args: answer-> 'Me fale sobre Engenharia de Softwares'
    Return: str-> 'Engenharia de Software é...' 

    Ex: certo: 'O que é Arquitetura de Software? -> 'Arquitetura de Software é...'
        incorreto: 'Qual a capital de Mato Grosso? -> 'Não sei responder.'
    """

    # Método que formata a saída do retriever
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)


    # Define as mensagens do prompt
    SYSTEM_MESSAGE = """Somente responda perguntas relacionadas ao contexto.
    Perguntas fora do contexto responda: 'Não sei responder.'.
    """
    HUMAN_MESSGE = """Contexto:
    {context}

    Pergunta: {answer}
    Resposta:
    """

    # Define o prompt
    prompt = ChatPromptTemplate([
        ("system", SYSTEM_MESSAGE),
        ("human", HUMAN_MESSGE)
    ])

    retriever = load_retriever()

    knowledge_chain = (
        {
            "context": retriever | format_docs,
            "answer": RunnablePassthrough(),
        }
        | prompt
        | model_changed()
        | StrOutputParser()
    )

    try:
        resposta = knowledge_chain.invoke(answer)
    except Exception as e:
        return f"Não foi possível executar a Tool search_knowledges\n{e}"

    return resposta


@tool
def calculator(exp: Annotated[str, "Resolve expressões aritméticas simples e intermediárias. Ex: 'Quanto é 15*2**2?'-> '900'"]):
    """
    Somente Resolve expressões aritméticas simples e intermediárias usando eval.
    Para calculos mais complexos retorne: 'Não consigo fazer esse calculo.'.

    Args: exp-> '15*2'
    Return: '30'

    Ex: certo: 'Quanto é 15 mais 30**4? -> '4100625.'
        incorreto: 'Qual é o resultado de x+2=2*(50/5)+30? -> 'Não consigo fazer esse calculo.'
    """

    try:
        # Retorna o resultado de uma expressão aritmética simples
        resultado = eval(exp)
    except Exception as e:
        return f"Erro ao tentar calcular.\n{e}"


def build_agent()-> type(create_agent):
    """
    Cria um Agentic IA usando Agent ReAct que usa somente as Tools.
    Usa a Tool search_knowledges para responder a perguntas conceituais.
    Usa a Tool calculator para resolver expressões aritméticas intermediárias.
    Para calculos mais complexos responder: 'Não consigo resolver esse tipode calculo.S'.

    Returns: Instancia de um create_agent()
    """

    try:
        tools = [search_knowledges, calculator]

        agent_execute = create_agent(model_changed(), tools)

        return agent_execute
    except Exception as e:
        return f"Ocorreu um erro ao criar o agente, verifique a configuração do modelo.\n{e}"


def execute_agent(answer: str):
    """
    Define e executa o agente.
    Agente responde somente à perguntas relacionadas ao documento FAISS do Dia 4

    Args: answer-> 'Me fale sobre Engenharia de Softwares.'
    """

    # Define o agente
    agent = build_agent()

    messages = HumanMessage(content = answer)

    try:
        agent_content = agent.invoke(
            {"messages": [messages]},
            config={"recursion_limit": 10}
        )

        reponse = agent_content["messages"][-1].content

        print("\n" + "=" * 70)
        print("RACIOCÍNIO DO AGENT:")
        print("="*70)      

        for message in agent_content["messages"]:
            tipo = type(message).__name__
            content = message.content if hasattr(message, "content") else str(message)
            print(f"\n[{tipo}]")
            print(content)
        print("=" * 70 + "\n")

        return reponse
    except Exception as e:
        return f"Não foi possível definir o agente.\n{e}"


def map_reduce_parallel(retriever, question, max_workers=5):
    """
    Processa chunks em paralelo usando map-reduce

    Args:
        retriever: Retriever configurado
        question: Pergunta a ser respondida
        max_workers: Número de threads paralelas

    Returns:
        Resposta final combinada
    """
    
    # Define os templates MAP e REDUCE
    map_template = ChatPromptTemplate.from_messages([
        ("system", "Resuma o seguinte trecho de documento. Mantenha apenas informações relevantes para responder perguntas."),
        ("human", "Trecho:\n{chunk}\n\nResumo:")
    ])

    reduce_template = ChatPromptTemplate.from_messages([
        ("system", "Combine os seguintes resumos em uma resposta completa e coerente à pergunta. Se não houver informação suficiente, diga 'Não sei responder'."),
        ("human",
        "Resumos:\n{summaries}\n\nPergunta: {input}\n\nResposta completa:")
    ])

    map_chain = (
        map_template
        | model_changed()
        | StrOutputParser()
    )

    reduce_chain = (
        reduce_template
        | model_changed()
        | StrOutputParser()
    )
    
    # Busca chunks relevantes
    chunks = retriever.invoke(question)
    inputs = [{"chunk": c.page_content for c in chunks}]

    print(f"Processando {len(chunks)} chunks em paralelo...")

    # Processa chunks em paralelo (MAP)
    summaries = map_chain.batch(
        inputs,
        config = {
            "max_concurrency": max_workers,
        }
    )

    # Combina resumos (REDUCE)
    combined = "\n\n".join(summaries)
    final_answer = reduce_chain.invoke({
        "summaries": combined,
        "input": question,
    })

    return final_answer


def comparar_chain_types():
    """
    TODO: Comparar diferentes tipos de chains RAG

    Compare:
    - "stuff" (mais simples, mais rápido)
    - "map_reduce" (funciona com muitos chunks)
    """
    
    print("=" * 60)

    # Lista de perguntas
    answers_list = [
        "Qual é o resultado de x+2=2*(50/5)+30?",
        "Quem descobriu o Brasil?",
        "Quais bibliotecas são usadas para desenvolver com IA?",
        "Quanto é 15 elevado na potência de 5?",
        "Quais os pontos chaves da Arquitetura de Softwares?"
    ]
    
    # Compara STUFF vs MAP-REDUCE
    resultados = []    
    
    for i, answers in enumerate(answers_list):
        print(f"\n{'='*60}")
        print(f"Pergunta {i+1}: {answers}")
        print(f"{'='*60}")
        
        # Teste STUFF
        tempo_inicio = time.time()
        # Tenta a call da chain
        try:
            resposta_stuff = execute_agent(answers)
        except Exception as e:
            print(f"Erro em STUFF: {e}")
            resposta_stuff = "Erro ao processar"

        tempo_stuff = time.time() - tempo_inicio
        
        # Teste MAP-REDUCE
        tempo_inicio = time.time()
        retriever = load_retriever()
        resposta_map_reduce = map_reduce_parallel(retriever, answers)
        tempo_map_reduce = time.time() - tempo_inicio
        
        resultados.append({
            "pergunta": answers,
            "stuff": {
                "resposta": resposta_stuff,
                "tempo": tempo_stuff
            },
            "map_reduce": {
                "resposta": resposta_map_reduce,
                "tempo": tempo_map_reduce
            }
        })
        
        print(f"\nSTUFF:")
        print(f"  Tempo: {tempo_stuff:.2f}s")
        print(f"  Resposta: {resposta_stuff[:150]}...")
        
        print(f"\nMAP-REDUCE:")
        print(f"  Tempo: {tempo_map_reduce:.2f}s")
        print(f"  Resposta: {resposta_map_reduce[:150]}...")
     
    # Resumo final
    print("\n" + "=" * 60)
    print("RESUMO DA COMPARAÇÃO")
    print("=" * 60)
    
    tempo_total_stuff = sum(r["stuff"]["tempo"] for r in resultados)
    tempo_total_map_reduce = sum(r["map_reduce"]["tempo"] for r in resultados)
    
    print(f"\nTempo total STUFF: {tempo_total_stuff:.2f}s")
    print(f"Tempo total MAP-REDUCE: {tempo_total_map_reduce:.2f}s")
    print(f"Diferença: {abs(tempo_total_map_reduce - tempo_total_stuff):.2f}s")
    
    print("\n💡 Análise:")
    print("   - STUFF é mais rápido para poucos chunks")
    print("   - MAP-REDUCE processa melhor muitos chunks")
    print("   - Use STUFF quando contexto cabe no limite do LLM")
    print("   - Use MAP-REDUCE quando precisa processar muitos documentos")


if __name__ == "__main__":
    comparar_chain_types()
