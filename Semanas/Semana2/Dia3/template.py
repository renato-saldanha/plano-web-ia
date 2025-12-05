#!/usr/bin/env python3
"""
Template: Sistema RAG Básico - Prática Guiada

Este arquivo contém TODOs para você completar e aprender RAG básico.
Siga os comentários e complete cada seção.

Uso:
    python template.py
"""

import encodings
import os
from dotenv import load_dotenv

# TODO: Importar bibliotecas necessárias do LangChain
# Dica: Você precisará de:
# - TextLoader (de langchain_community.document_loaders)
# - RecursiveCharacterTextSplitter (de langchain_text_splitters)
# - BM25Retriever (de langchain_community.retrievers)
# - StrOutputParser (de langchain_core.output_parsers)
# - RunnablePassthrough (de langchain_core.runnables)
# - ChatGroq (de langchain_groq)
# - ChatPromptTemplate (de langchain_core.prompts)

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.retrievers import BM25Retriever
from langchain_core.runnables import RunnablePassthrough
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate


# ============================================================================
# SEÇÃO 1: CONFIGURAÇÃO
# ============================================================================

# TODO: Carregar variáveis de ambiente
# Dica: Use load_dotenv() sem argumentos para carregar .env na raiz

load_dotenv()

MODELOS_GROQ = {
    "llama-3.1-8b-instant": "llama-3.1-8b-instant",  # "Rápido e eficiente ⭐"
    "llama-3.1-70b-versatile": "llama-3.1-70b-versatile",  # "Mais poderoso"
    "llama-3.3-70b-versatile": "llama-3.3-70b-versatile",  # "Versão mais recente"
    "mixtral-8x7b-32768": "mixtral-8x7b-32768",  # "Textos longos (32k tokens)"
    "gemma-7b-it": "gemma-7b-it",  # "Google Gemma"
}

# TODO: Criar instância do LLM
# Dica: Use ChatGroq com modelo "llama-3.1-8b-instant"
# Parâmetros: model, temperature=0, groq_api_key=os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model=MODELOS_GROQ["llama-3.1-8b-instant"],
    temperature=0
)

# ============================================================================
# SEÇÃO 2: CARREGAR DOCUMENTO
# ============================================================================


def carregar_documento(caminho_documento: str):
    """
    TODO: Carregar documento de texto

    Args:
        caminho_arquivo: Caminho para o arquivo de texto

    Returns:
        Lista de documentos carregados

    Dica: Use TextLoader para carregar arquivo de texto
    """

    # TODO: Criar loader
    # TODO: Carregar documentos
    # TODO: Retornar documentos

    loader = PyPDFLoader(caminho_documento, extract_images=False)

    # print(f" Documentos carregados: {len(documents)}")
    # print(f"Conteúdo inicial: {documents[0].page_content[:200]}... \n")

    # Retorna loader por conta do tamanho do arquivo usado para testes
    return loader


# ============================================================================
# SEÇÃO 3: DIVIDIR EM CHUNKS
# ============================================================================

def dividir_em_chunks(loader=PyPDFLoader, chunk_size: int = 4000, chunk_overlap: int = 1000):
    """
    TODO: Dividir documentos em chunks menores

    Args:
        documents: Lista de documentos
        chunk_size: Tamanho de cada chunk (caracteres)
        chunk_overlap: Sobreposição entre chunks

    Returns:
        Lista de chunks

    Dica: Use RecursiveCharacterTextSplitter
    """
    # TODO: Criar text splitter
    # TODO: Dividir documentos
    # TODO: Retornar chunks

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=lambda x: len(x.encode("utf-8")),
        separators=["\n\n", "\n", ". ", " ", ""]  # Ordem de separação
    )

    chunks = []

    # Melhora significavelmente a performance quando arquivos maiores
    for doc in loader.lazy_load():
        chunks.extend(text_splitter.split_documents([doc]))

    print(f"Chunks criados: {len(chunks)}")
    # for i, chunk in enumerate(chunk, i):
    #     print(f"\n Chunk {i} ({len(chunk.page_content)})")
    #     print(f"     {chunk.page_content[:100]}...")

    return chunks

# ============================================================================
# SEÇÃO 4: CRIAR RETRIEVER
# ============================================================================


def criar_retriever(chunks, k: int = 6):
    """
    TODO: Criar retriever para buscar chunks relevantes

    Args:
        chunks: Lista de chunks
        k: Número de chunks a retornar

    Returns:
        Retriever configurado

    Dica: Use BM25Retriever.from_documents()
    """
    # TODO: Criar retriever
    # TODO: Configurar k (número de chunks a retornar)
    # TODO: Retornar retriever

    retriever = BM25Retriever.from_documents(chunks)
    retriever.k = k

    query = "O que dizer sobre engenharia de softwares?"
    relevants_chunks = retriever.invoke(query)

    print("Retriever criado!")
    print(f"Chunks encontrado: {len(relevants_chunks)}")

    return retriever

# ============================================================================
# SEÇÃO 5: CRIAR CHAIN RAG
# ============================================================================


def criar_chain_rag(llm, retriever):
    """
    TODO: Criar chain RAG completa usando LCEL puro (abordagem moderna)

    Args:
        llm: Instância do LLM
        retriever: Retriever configurado

    Returns:
        Chain RAG configurada

    Dica: Use LCEL puro com RunnablePassthrough e StrOutputParser
    Passos:
    1. Criar função format_docs() para formatar documentos em string
    2. Criar ChatPromptTemplate com {context} e {input}
    3. Criar chain usando operador | (pipe) do LCEL
    """
    # TODO: Criar função para formatar documentos
    # Dica: def format_docs(docs):
    #           return "\n\n".join(doc.page_content for doc in docs)

    # TODO: Criar prompt template moderno
    # Dica: Use ChatPromptTemplate.from_messages() com:
    #       - ("system", "mensagem do sistema")
    #       - ("human", "Contexto:\n{context}\n\nPergunta: {input}")

    # TODO: Criar chain RAG usando LCEL puro
    # Dica: qa_chain = (
    #           {
    #               "context": retriever | format_docs,
    #               "input": RunnablePassthrough()
    #           }
    #           | prompt_template
    #           | llm
    #           | StrOutputParser()
    #       )

    # TODO: Retornar chain

    def format_docs(docs):
        """Formata documentos em uma string para o contexto"""
        return "\n\n".join(doc.page_content for doc in docs)

    template = ChatPromptTemplate.from_messages([
        ("system", "Use as seguintes informações do contexto para responder a pergunta. "
         "Se você não souber a resposta, diga que não sabe."
         "Não invente informações."),
        ("human", "Contexto:\n{context}\n\nPergunta: {input}\n\nResposta:")
    ])

    rag_chain = (
        {
            "context": retriever | format_docs,
            "input": RunnablePassthrough(),
        }
        | template
        | llm
        | StrOutputParser()
    )

    return rag_chain


# ============================================================================
# SEÇÃO 6: FUNÇÃO PRINCIPAL
# ============================================================================

def main():
    """
    TODO: Função principal que orquestra todo o sistema RAG
    """
    print("=" * 60)
    print("Sistema RAG Básico - Template")
    print("=" * 60)

    caminho_documento = "D:/plano web+ia/Semanas/Semana2/Dia3/db/Engenharia de Software para Ciência de Dados - Marcos Kalinowski.pdf"

    documents = carregar_documento(caminho_documento)

    chunks = dividir_em_chunks(documents)

    retriever = criar_retriever(chunks)

    rag_chain = criar_chain_rag(llm, retriever)

    prompt = "Qual a melhor métrica de engenharia aplicado à IA?"

    response = rag_chain.invoke(prompt)

    print("=" * 60)
    print("Prompt:")
    print("=" * 60)
    print(response)


if __name__ == "__main__":
    main()
