#!/usr/bin/env python3
"""
Exercício 2: RAG com Documentos Reais

Crie sistema RAG que funciona com documentos reais (PDF ou texto mais complexo).

Tarefas:
1. Carregar um documento mais complexo
2. Ajustar parâmetros de split
3. Criar sistema RAG otimizado
4. Testar com múltiplas perguntas
"""

import os
from dotenv import load_dotenv  # type: ignore

# TODO: Importar bibliotecas necessárias
# Dica: Você precisará de:
# - TextLoader ou PyPDFLoader (de langchain_community.document_loaders)
# - RecursiveCharacterTextSplitter (de langchain_text_splitters)
# - BM25Retriever (de langchain_community.retrievers)
# - StrOutputParser (de langchain_core.output_parsers)
# - RunnablePassthrough (de langchain_core.runnables)
# - ChatGroq (de langchain_groq)
# - ChatPromptTemplate (de langchain_core.prompts)

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.retrievers import BM25Retriever
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq


load_dotenv()

llm = ChatGroq(
    model = "llama-3.1-8b-instant",
    temperature = 0,   
)

def sistema_rag_complexo():
    """
    TODO: Criar sistema RAG com documento mais complexo
    
    Esta função deve:
    1. Carregar documento complexo (ou criar um maior)
    2. Ajustar tamanho de chunks apropriadamente
    3. Criar sistema RAG
    4. Testar com múltiplas perguntas
    """
    print("=" * 60)
    print("Exercício 2: RAG com Documentos Reais")
    print("=" * 60)
    
    # TODO: Criar ou carregar documento mais complexo
    # Dica: Crie um documento com 5-10 parágrafos sobre um tópico
    # TODO: Carregar documento

    caminho_arquivo = "D:\plano web+ia\Semanas\Semana2\Dia3\db\Engenharia de Software para Ciência de Dados - Marcos Kalinowski.pdf"
    try:
        loader = PyPDFLoader(caminho_arquivo, extract_images = False)
        arquivo_carregado = loader.load()
    except Exception as e:
        raise Exception(f"Arquivo não pode ser carregado.\n{e}")
    
    print("Arquivo carregado!")
    print(f"Caminho: {caminho_arquivo}")
    print("-" * 60)
    
    # TODO: Dividir em chunks com tamanho apropriado
    # Dica: Experimente diferentes tamanhos (500, 1000 caracteres)
    #       Ajuste overlap conforme necessário    


    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap = 70,                
        length_function = lambda x: len(x.encode("utf-8")),
        separators = ["\n\n", "\n", ". ", " ", ""]  # Ordem de separação
    )

    chunks = text_splitter.split_documents(arquivo_carregado)

    print("Chunks criados!")
    print(f"Chunks: {len(chunks)}")
    print("-" * 60)

    # TODO: Criar retriever
    # Dica: Aumente k para retornar mais chunks (3-5)

    text_retriever = BM25Retriever.from_documents(chunks)    
    text_retriever.k = 5

    # TODO: Criar chain RAG usando LCEL puro (abordagem moderna)
    # Dica: 
    # 1. Criar função format_docs(docs) para formatar documentos
    # 2. Criar ChatPromptTemplate com {context} e {input}
    # 3. Criar chain usando operador | (pipe) do LCEL:
    #    qa_chain = (
    #        {"context": retriever | format_docs, "input": RunnablePassthrough()}
    #        | prompt_template | llm | StrOutputParser()
    #    )

    def format_docs(docs):
        "\n\n".join(doc.page_content for doc in docs)

    template = ChatPromptTemplate([
        ("system", "Responda a pergunta com base no contexto. Não invente informações. Se não souber diga: Não sei responder."),
        ("human", "Contexto:\n{contexto}\n\nPergunta: {input}\n\nResposta:\n")
    ])

    print("Template instanciado!")
    print("-" * 60)

    question_chain = (
        {
            "contexto": text_retriever | format_docs,
            "input": RunnablePassthrough(),
        }
        | template
        | llm
        | StrOutputParser()
    )
    
    print("Chain instanciada!")
    print("-" * 60)

    # TODO: Fazer múltiplas perguntas
    # Dica: Use chain.invoke(pergunta) - LCEL puro retorna string diretamente
    #       Para mostrar fontes: chunks = retriever.invoke(pergunta)
    perguntas = [
        "O que é Engenharia de Software?",
        "Como implementar IA na Engenharia de Software?",
        "O que é mais de importânte na Engenharia de Software?",
    ]
    
    # TODO: Para cada pergunta, mostrar resposta e chunks usados
    
    for pergunta in perguntas:
        response = question_chain.invoke(pergunta)
        chunks = text_retriever.invoke(pergunta)

        print(f"Pergunta:\n {pergunta}")
        print("=" * 60)
        print(f"Resposta:\n {response}")
        print("=" * 60)
        
        for chunk in chunks:
            print(f"Chunks usados:\n {len(chunk.page_content)}")
            print(f"parte do texto:\n {chunk.page_content[:100]}...")
        
        print("=" * 60)
    
    
if __name__ == "__main__":
    sistema_rag_complexo()

