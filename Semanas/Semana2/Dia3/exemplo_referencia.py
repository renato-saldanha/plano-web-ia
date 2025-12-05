#!/usr/bin/env python3
"""
Exemplo de Referência: RAG Básico com LangChain

Este arquivo demonstra como criar um sistema RAG básico usando LangChain.
RAG (Retrieval-Augmented Generation) combina busca em documentos com geração de resposta.

Uso:
    python exemplo_referencia.py
"""

import os
from dotenv import load_dotenv  # type: ignore
from langchain_community.document_loaders import TextLoader  # type: ignore
from langchain_text_splitters import RecursiveCharacterTextSplitter  # type: ignore
from langchain_community.retrievers import BM25Retriever  # type: ignore
from langchain_core.output_parsers import StrOutputParser  # type: ignore
from langchain_core.runnables import RunnablePassthrough  # type: ignore
from langchain_groq import ChatGroq  # type: ignore
from langchain_core.prompts import ChatPromptTemplate  # type: ignore

# ============================================================================
# SEÇÃO 1: CONFIGURAÇÃO
# ============================================================================
load_dotenv()

# Criar instância do LLM (reutilizável)
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

# ============================================================================
# SEÇÃO 2: CRIAR DOCUMENTO DE EXEMPLO
# ============================================================================
# Em produção, você carregaria documentos reais. Aqui criamos um exemplo.

print("=" * 60)
print("EXEMPLO: Sistema RAG Básico")
print("=" * 60)

# Criar arquivo de exemplo com informações sobre Python
documento_exemplo = """
Python é uma linguagem de programação de alto nível criada por Guido van Rossum em 1991.
A linguagem foi projetada com foco na legibilidade do código e produtividade do programador.

Python suporta múltiplos paradigmas de programação, incluindo programação orientada a objetos,
programação imperativa e programação funcional. Possui um sistema de tipos dinâmico e gerenciamento
automático de memória.

A linguagem é amplamente usada para desenvolvimento web, ciência de dados, inteligência artificial,
automação de tarefas e muito mais. Python tem uma grande comunidade e ecossistema de bibliotecas.

Algumas bibliotecas populares incluem:
- NumPy: Para computação científica
- Pandas: Para análise de dados
- Django e Flask: Para desenvolvimento web
- LangChain: Para aplicações com IA generativa
"""

# Salvar documento temporário
arquivo_temp = "documento_exemplo.txt"
with open(arquivo_temp, "w", encoding="utf-8") as f:
    f.write(documento_exemplo)

print(f"✅ Documento criado: {arquivo_temp}\n")

# ============================================================================
# SEÇÃO 3: CARREGAR DOCUMENTO
# ============================================================================
# Document Loader: Carrega documentos de diferentes fontes

print("=" * 60)
print("PASSO 1: Carregar Documento")
print("=" * 60)
# PyPDFLoader para PDF
loader = TextLoader(arquivo_temp, encoding="utf-8")
documents = loader.load()

print(f"✅ Documentos carregados: {len(documents)}")
print(
    f"📄 Conteúdo (primeiros 200 caracteres): {documents[0].page_content[:200]}...\n")

# ============================================================================
# SEÇÃO 4: DIVIDIR EM CHUNKS
# ============================================================================
# Text Splitter: Divide documentos grandes em chunks menores

print("=" * 60)
print("PASSO 2: Dividir em Chunks")
print("=" * 60)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,      # Tamanho de cada chunk (caracteres)
    chunk_overlap=50,    # Sobreposição entre chunks
    length_function=len,
    separators=["\n\n", "\n", ". ", " ", ""]  # Ordem de separação
)

chunks = text_splitter.split_documents(documents)

print(f"✅ Chunks criados: {len(chunks)}")
for i, chunk in enumerate(chunks, 1):
    print(f"\n📦 Chunk {i} ({len(chunk.page_content)} caracteres):")
    print(f"   {chunk.page_content[:100]}...")

# ============================================================================
# SEÇÃO 5: CRIAR RETRIEVER
# ============================================================================
# Retriever: Busca chunks relevantes baseado em query

print("\n" + "=" * 60)
print("PASSO 3: Criar Retriever")
print("=" * 60)

retriever = BM25Retriever.from_documents(chunks)
retriever.k = 2  # Retornar top 2 chunks mais relevantes

# Testar busca
query_teste = "Quem criou Python?"
chunks_relevantes = retriever.invoke(query_teste)

print(f"✅ Retriever criado")
print(f"🔍 Query de teste: '{query_teste}'")
print(f"📚 Chunks encontrados: {len(chunks_relevantes)}")
for i, chunk in enumerate(chunks_relevantes, 1):
    print(f"\n   Chunk {i}:")
    print(f"   {chunk.page_content[:150]}...")

# ============================================================================
# SEÇÃO 6: CRIAR CHAIN RAG COMPLETA
# ============================================================================
# Chain RAG: Combina retriever + LLM para gerar resposta contextualizada
# Usando LCEL (LangChain Expression Language) - abordagem moderna

print("\n" + "=" * 60)
print("PASSO 4: Criar Chain RAG")
print("=" * 60)

# Criar prompt template moderno com ChatPromptTemplate
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "Use as seguintes informações do contexto para responder a pergunta. Se você não souber a resposta, diga que não sabe. Não invente informações."),
    ("human", "Contexto:\n{context}\n\nPergunta: {input}\n\nResposta:")
])

# Criar chain RAG usando LCEL puro (sem funções helper)


def format_docs(docs):
    """Formata documentos em uma string para o contexto"""
    return "\n\n".join(doc.page_content for doc in docs)


qa_chain = (
    {
        "context": retriever | format_docs,
        "input": RunnablePassthrough()
    }
    | prompt_template
    | llm
    | StrOutputParser()
)

print("✅ Chain RAG criada\n")

# ============================================================================
# SEÇÃO 7: FAZER PERGUNTAS
# ============================================================================
# Testar sistema RAG com diferentes perguntas

print("=" * 60)
print("PASSO 5: Fazer Perguntas")
print("=" * 60)

perguntas = [
    "Quem criou Python?",
    "Quais são algumas bibliotecas populares do Python?",
    "Para que Python é usado?",
]

for pergunta in perguntas:
    print(f"\n❓ Pergunta: {pergunta}")
    print("-" * 60)

    # LCEL puro retorna apenas a resposta (string)
    resposta = qa_chain.invoke(pergunta)

    # Buscar chunks relevantes separadamente para mostrar fontes
    chunks_relevantes = retriever.invoke(pergunta)

    print(f"💡 Resposta: {resposta}")
    print(f"📚 Fontes usadas: {len(chunks_relevantes)} chunks")

    # Mostrar chunks usados
    for i, doc in enumerate(chunks_relevantes, 1):
        print(f"\n   Fonte {i}:")
        print(f"   {doc.page_content[:100]}...")

# ============================================================================
# SEÇÃO 8: LIMPEZA
# ============================================================================
# Remover arquivo temporário

print("\n" + "=" * 60)
print("Limpeza")
print("=" * 60)

if os.path.exists(arquivo_temp):
    os.remove(arquivo_temp)
    print(f"✅ Arquivo temporário removido: {arquivo_temp}")

print("\n✅ Exemplo concluído!")
print("\n💡 Próximos passos:")
print("   - Modifique o documento para testar com seus próprios dados")
print("   - Experimente diferentes tamanhos de chunks")
print("   - Teste com diferentes perguntas")
print("   - Veja como RAG melhora respostas comparado a geração simples")
