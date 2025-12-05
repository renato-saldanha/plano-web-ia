#!/usr/bin/env python3
"""
Exercício 1: RAG Simples

Crie seu primeiro sistema RAG básico funcionando.

Tarefas:
1. Carregar um documento de texto simples
2. Dividir o documento em chunks
3. Criar um retriever simples
4. Criar uma chain RAG básica
5. Fazer uma pergunta e ver a resposta
"""

import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_community.retrievers import BM25Retriever
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_groq import ChatGroq
from langchain_text_splitters import RecursiveCharacterTextSplitter

# TODO: Importar bibliotecas necessárias
# Dica: Você precisará de:
# - TextLoader (de langchain_community.document_loaders)
# - RecursiveCharacterTextSplitter (de langchain_text_splitters)
# - BM25Retriever (de langchain_community.retrievers)
# - StrOutputParser (de langchain_core.output_parsers)
# - RunnablePassthrough (de langchain_core.runnables)
# - ChatGroq (de langchain_groq)
# - ChatPromptTemplate (de langchain_core.prompts)

# TODO: Carregar variáveis de ambiente
load_dotenv()

# TODO: Criar documento de exemplo
# Crie um arquivo temporário com texto sobre um tópico que você conhece
# Exemplo: informações sobre Python, sua cidade, um hobby, etc.

def criar_documento_exemplo():
    """
    TODO: Criar arquivo temporário com texto de exemplo
    
    Returns:
        Caminho do arquivo criado
    """
    # TODO: Criar texto sobre um tópico que você conhece
    texto = """
    [TODO: Escreva 2-3 parágrafos sobre um tópico que você conhece bem]
    """
    
    # TODO: Salvar em arquivo temporário
    # Dica: Use open() com modo 'w' e encoding='utf-8'
    
    # TODO: Retornar caminho do arquivo
    
    contexto = """
    O Python é a linguagem dominante para inteligência artificial (IA) devido à sua simplicidade e vasta coleção de bibliotecas especializadas. 
    Frameworks populares como o TensorFlow e o PyTorch facilitam a criação de modelos complexos de aprendizado de máquina e redes neurais. 
    A sintaxe intuitiva do Python permite que os desenvolvedores se concentrem na lógica da IA em vez de detalhes de implementação de baixo nível. 
    Bibliotecas adicionais como NumPy e Pandas oferecem ferramentas eficientes para manipulação e análise de dados, 
    etapas cruciais no desenvolvimento de soluções de IA. 
    Essa combinação de facilidade de uso e ecossistema robusto faz do Python a escolha ideal para o desenvolvimento de sistemas inteligentes.
    """
    
    arquivo_temp = "contexto.txt"

    with open(arquivo_temp, mode = "w", encoding = "utf-8") as f:
        arquivo = f.write(contexto)
    
    return arquivo_temp


def sistema_rag_simples():
    """
    TODO: Criar sistema RAG simples completo
    
    Esta função deve:
    1. Carregar documento
    2. Dividir em chunks
    3. Criar retriever
    4. Criar chain RAG
    5. Fazer pergunta e mostrar resposta
    """
    print("=" * 60)
    print("Exercício 1: RAG Simples")
    print("=" * 60)
    
    # TODO: Criar documento de exemplo
    arquivo = criar_documento_exemplo()
    
    # TODO: Carregar documento usando TextLoader
    # Dica: loader = TextLoader(arquivo, encoding="utf-8")
    #       documents = loader.load()

    loader = TextLoader(arquivo, encoding = "utf-8")
    documents = loader.load()

    # TODO: Dividir em chunks usando RecursiveCharacterTextSplitter
    # Dica: chunk_size=300, chunk_overlap=50

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 300,
        chunk_overlap = 50,         
        length_function = lambda x: len(x.encode("utf-8")),
        separators = ["\n\n", "\n", ". ", " ", ""]  # Ordem de separação
    )

    chunks = text_splitter.split_documents(documents)
    
    # TODO: Criar retriever usando BM25Retriever
    # Dica: retriever = BM25Retriever.from_documents(chunks)
    #       retriever.k = 2

    retriever = BM25Retriever.from_documents(chunks)
    retriever.k = 4

    # TODO: Criar LLM usando ChatGroq
    # Dica: model="llama-3.1-8b-instant", temperature=0
    
    llm = ChatGroq(
        model = "llama-3.1-8b-instant",
        temperature = 0,        
    )

    # TODO: Criar chain RAG usando LCEL puro (abordagem moderna)
    # Dica: 
    # 1. Criar função format_docs(docs) que retorna "\n\n".join(doc.page_content for doc in docs)
    # 2. Criar ChatPromptTemplate.from_messages() com {context} e {input}
    # 3. Criar chain usando:
    #    qa_chain = (
    #        {
    #            "context": retriever | format_docs,
    #            "input": RunnablePassthrough()
    #        }
    #        | prompt_template
    #        | llm
    #        | StrOutputParser()
    #    )

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)
    
    template = ChatPromptTemplate.from_messages([
        ("system", "Responda as perguntar conforme o contexto."
                "Somente responda a perguntas relacionadas ao contexto."
                "Nunca invente nada que esteja dentro ou fora do contexto."),
        ("human", "Contexto:\n{contexto}\n\nPergunta: {input}\n\nResposta:\n")   
    ])

    question_chain = (
        {
            "contexto": retriever | format_docs,
            "input": RunnablePassthrough()
        }
        | template
        | llm
        | StrOutputParser()
    )


    # TODO: Fazer uma pergunta
    pergunta = "O que dizer de Engenharia de Software com agentes IA para automação?"
    
    # TODO: Invocar chain e mostrar resultado
    # Dica: resposta = qa_chain.invoke(pergunta)  # Retorna string diretamente
    #       chunks_usados = retriever.invoke(pergunta)  # Buscar chunks separadamente
    #       print(f"Resposta: {resposta}")
    #       print(f"Chunks usados: {len(chunks_usados)}")
    

    response = question_chain.invoke(pergunta)
    chunks_usados = retriever.invoke(pergunta)

    print(f"Pergunta:\n{pergunta}")
    print("=" * 60)
    print(f"Resposta:\n{response}")
    print("=" * 60)
    print(f"Chunks usados: {chunks_usados}")

    # TODO: Limpar arquivo temporário
    # Dica: os.remove(arquivo) se necessário

    os.remove(arquivo)
    

if __name__ == "__main__":
    sistema_rag_simples()

