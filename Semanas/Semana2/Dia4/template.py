#!/usr/bin/env python3
"""
RAG Avançado com Vector Databases - Template

Este template guia você na criação de um sistema RAG avançado usando:
- Embeddings para representação vetorial de texto
- FAISS como vector database para busca semântica
- RAG chain completa com LCEL

Complete os TODOs seguindo as dicas fornecidas.
Consulte `exemplo_referencia.py` e `GUIA_RAG_AVANCADO.md` quando necessário.
"""

# ============================================================================
# TODO 1: IMPORTAR BIBLIOTECAS NECESSÁRIAS
# ============================================================================
# Dica: Você precisará de:
# - langchain_groq: Para o LLM (ChatGroq)
# - langchain_core: Para prompts, runnables e parsers
# - langchain_community: Para embeddings e vector stores
# - dotenv: Para carregar variáveis de ambiente
# - os: Para acessar variáveis de ambiente

import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_groq import ChatGroq
from langchain_text_splitters import RecursiveCharacterTextSplitter

# ============================================================================
# TODO 2: CONFIGURAR AMBIENTE
# ============================================================================
# Dica: Use load_dotenv() para carregar arquivo .env
# Certifique-se de que GROQ_API_KEY está definida

load_dotenv();
# ============================================================================
# TODO 7: CONFIGURAR LLM
# ============================================================================
# Dica: Use ChatGroq com modelo "llama-3.1-70b-versatile"
# Certifique-se de que GROQ_API_KEY está no .env

llm = ChatGroq(
   model = "llama-3.1-8b-instant",
   temperature = 0,
)

# ============================================================================
# TODO 3: CRIAR MODELO DE EMBEDDINGS
# ============================================================================
# Dica: Use HuggingFaceEmbeddings com modelo "all-MiniLM-L6-v2"
# Este modelo é leve (384 dimensões) e rápido
# 
# Referência: GUIA_RAG_AVANCADO.md seção "3.1 Criando Embeddings"

# TODO: Criar modelo de embeddings
# embeddings = HuggingFaceEmbeddings(
#     model_name="...",  # Qual modelo usar?
#     model_kwargs={'device': '...'},  # CPU ou CUDA?
#     encode_kwargs={'normalize_embeddings': True}
# )

embedding = HuggingFaceEmbeddings(
   model_name = "all-MiniLM-L6-v2",
   model_kwargs = {"device": 'cpu'},
   encode_kwargs = {"normalize_embeddings": True}
)


# ============================================================================
# TODO 4: CARREGAR E DIVIDIR DOCUMENTOS
# ============================================================================
# Dica: Reutilize código do Dia 3!
# - Use PyPDFLoader para carregar documento
# - Use RecursiveCharacterTextSplitter para dividir
# - Chunk size recomendado: 500, overlap: 50
#
# Referência: ../Dia3/template.py


# TODO: Carregar documento
# loader = PyPDFLoader("caminho/para/documento.txt", extract_images = False)
# docs = loader.load()
def definir_chunks():
   caminho_arquivo = "F:\\Projetos\\plano web+ia\\Semanas\\Semana2\\Dia3\\db\\Engenharia de Software para Ciência de Dados - Marcos Kalinowski.pdf"
   loader = PyPDFLoader(caminho_arquivo, extract_images = False)
   docs = loader.load()

   # TODO: Dividir em chunksplitter.split_documents(docs)

   text_splitter = RecursiveCharacterTextSplitter(
      chunk_size = 1000,
      chunk_overlap = 400,   
      length_function = lambda x: len(x.encode("utf-8")),
      separators = ["\n\n", "\n", ". ", " ", ""]  # Ordem de separação
   )

   chunks = text_splitter.split_documents(docs)

   # TODO: Mostrar informações
   print(f"Documento carregado: {len(docs)} documento(s)")
   print(f"Chunks criados: {len(chunks)}")

   return chunks

# ============================================================================
# TODO 5: CRIAR VECTOR STORE COM CHROMA
# ============================================================================
# Dica: Use Chroma.from_documents() para criar a partir dos chunks
# - Passe os chunks processados
# - Passe o modelo de embeddings criado anteriormente
# - Use persist_directory para salvar dados localmente
#
# Referência: GUIA_RAG_AVANCADO.md seção "3.2 Setup Chroma"
# Exemplo: exemplo_referencia.py seção "Vector Store"

# TODO: Criar vector store
# vectorstore = Chroma.from_documents(
#     documents=...,  # Chunks processados
#     embedding=...,  # Modelo de embeddings
#     persist_directory="..."  # Pasta para persistir (ex: "./chroma_db")
# )

def definir_setup(chunks):
   print("\nCriando vector store com FAISS...")
   vectorstore = FAISS.from_documents(
      documents = chunks,
      embedding = embedding,
   )
   vectorstore.save_local("./faiss_index")
   print("Vector store criado e persistido!")


   # Para carregar depois:
   # vectorstore = FAISS.load_local("./faiss_index", embedding)


   # ============================================================================
   # TODO 6: CRIAR RETRIEVER SEMÂNTICO
   # ============================================================================
   # Dica: Use vectorstore.as_retriever() para criar retriever
   # - search_type="similarity" (busca por similaridade semântica)
   # - search_kwargs={"k": 3} (retornar 3 documentos mais relevantes)
   #
   # Referência: GUIA_RAG_AVANCADO.md seção "3.3 Busca Semântica"

   # TODO: Criar retriever
   # retriever = vectorstore.as_retriever(
   #     search_type="...",
   #     search_kwargs={"k": ...}
   # )

   retriever = vectorstore.as_retriever(
      search_type = "similarity",
      search_kwargs = {"k": 3}
   )

   # TODO: Testar retriever (opcional mas recomendado)
   # query_teste = "Sua query de teste aqui"
   # docs_encontrados = retriever.invoke(query_teste)
   # print(f"Encontrados {len(docs_encontrados)} documentos relevantes")
   # for i, doc in enumerate(docs_encontrados):

   print("\nTestando retriever...")
   query_teste = "O que é Engenharia de Software?"
   docs_encontrados = retriever.invoke(query_teste)

   print(f"Encontrados {len(docs_encontrados)} documentos relevantes")

   for i, doc in enumerate(docs_encontrados):
      print(f"\n--- Documento {i+1} ---")
      print(doc.page_content[:200] + "...")


   # ============================================================================
   # TODO 8: CRIAR PROMPT TEMPLATE
   # ============================================================================
   # Dica: O prompt deve instruir o LLM a:
   # - Responder baseado apenas no contexto fornecido
   # - Dizer quando não sabe a resposta
   # - Ser claro e objetivo
   #
   # Variáveis necessárias: {context} e {question}
   #
   # Referência: GUIA_RAG_AVANCADO.md seção "3.4 RAG Chain"

   # TODO: Criar template de prompt
   system_template = """Você é um assistente especializado em responder perguntas baseado em contexto.
   Use APENAS as informações do contexto abaixo para responder.
   Se não souber a resposta, diga "Não encontrei essa informação no contexto."
   """

   human_template = """
   Contexto:
   {context}

   Pergunta: {question}

   Resposta:
   """

   prompt = ChatPromptTemplate.from_messages([
      ("system", system_template),
      ("human", human_template)
   ])

   return retriever, prompt


def definir_chains(retriever, prompt):   
   # ============================================================================
   # TODO 9: CRIAR RAG CHAIN COM LCEL
   # ============================================================================
   # Dica: Use LCEL (LangChain Expression Language) aprendido no Dia 2
   # Estrutura:
   # 1. Criar dicionário com context (do retriever) e question (passthrough)
   # 2. Aplicar prompt template
   # 3. Passar para LLM
   # 4. Parsear output
   #
   # Referência: GUIA_RAG_AVANCADO.md seção "3.4 RAG Chain"
   # Exemplo: exemplo_referencia.py seção "RAG Chain"

   # TODO: Função auxiliar para formatar documentos

   # TODO: Criar RAG chain

   def format_docs(docs):
      """Formata lista de documentos em string única."""
      return "\n\n".join([doc.page_content for doc in docs])

   rag_chain = (
      {
         "context": retriever | format_docs,
         "question": RunnablePassthrough(),   
      }
      | prompt
      | llm
      | StrOutputParser()
   )

   return rag_chain

def executar_chain(rag_chain):   
   # ============================================================================
   # TODO 10: TESTAR RAG CHAIN
   # ============================================================================
   # Dica: Teste com queries diferentes para validar funcionamento
   # Compare com resultados do Dia 3 (RAG básico) se possível

   # TODO: Testar com queries
   print("\n" + "="*60)
   print("TESTANDO RAG AVANÇADO COM BUSCA SEMÂNTICA")
   print("="*60)

   queries = [
      "Quais bibliotecas são usadas para desenvolver com IA?",
      "O que a IA melhora na Engenharia de Softwares?",
      "Quais os pontos chaves da Arquitetura de Softwares?"
   ]

   for query in queries:
      print(f"\n{'='*60}")
      print(f"Pergunta: {query}")
      print(f"{'='*60}")
      
      resposta = rag_chain.invoke(query)
      print(f"\nResposta:\n{resposta}")


   # ============================================================================
   # TODO 11: COMPARAR COM RAG BÁSICO (OPCIONAL MAS RECOMENDADO)
   # ============================================================================
   # Dica: Execute mesmas queries que usou no Dia 3
   # Compare:
   # - Relevância dos documentos recuperados
   # - Qualidade das respostas
   # - Capacidade de entender sinônimos
   #
   # Referência: GUIA_RAG_AVANCADO.md seção "4. Comparação"

   # TODO: Fazer comparação
   print("\n" + "="*60)

# ============================================================================
# EXECUÇÃO PRINCIPAL
# ============================================================================
if __name__ == "__main__":
   print("="*60)
   print("RAG AVANÇADO COM VECTOR DATABASES")
   print("="*60)

   # TODO: Descomentar após completar TODOs acima
   chunks = definir_chunks();
   print("\n✅ Setup completo!")
   retriever, prompt = definir_setup(chunks)
   print("✅ Vector store criado!")
   rag_chains = definir_chains(retriever, prompt)
   executar_chain(rag_chains)
   print("✅ RAG chain funcionando!")


