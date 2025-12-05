#!/usr/bin/env python3
"""
RAG Avançado com Vector Databases - Exemplo Completo

Este arquivo contém um exemplo completo e funcional de RAG avançado usando:
- Embeddings (HuggingFace sentence-transformers)
- Chroma vector database para busca semântica
- RAG chain completa com LCEL

Use este arquivo como referência ao trabalhar no template.py
Cada seção está comentada para facilitar o entendimento.

Autor: Plano de Desenvolvimento 2 Meses Web + IA
Data: 4 Dez 2025
"""

# ============================================================================
# SEÇÃO 1: IMPORTS
# ============================================================================
# Por que precisamos destes imports:
# - ChatGroq: LLM para gerar respostas
# - ChatPromptTemplate: Criar templates de prompts
# - RunnablePassthrough: Passar dados através da chain
# - StrOutputParser: Extrair string do output do LLM
# - Chroma: Vector database para busca semântica
# - HuggingFaceEmbeddings: Modelo de embeddings gratuito
# - TextLoader: Carregar documentos de texto
# - RecursiveCharacterTextSplitter: Dividir documentos em chunks
# - dotenv: Carregar variáveis de ambiente
# - os: Acessar variáveis de ambiente

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
import os

# ============================================================================
# SEÇÃO 2: CONFIGURAÇÃO
# ============================================================================
# PASSO 1: Carregar variáveis de ambiente
print("="*70)
print("RAG AVANÇADO COM VECTOR DATABASES - EXEMPLO COMPLETO")
print("="*70)

load_dotenv()  # Carrega arquivo .env na raiz do projeto

# PASSO 2: Verificar se API key está disponível
if not os.getenv("GROQ_API_KEY"):
    raise ValueError("GROQ_API_KEY não encontrada no .env")

print("\n✅ Variáveis de ambiente carregadas")

# ============================================================================
# SEÇÃO 3: CRIAR MODELO DE EMBEDDINGS
# ============================================================================
# Por que: Embeddings são representações vetoriais de texto que capturam
# significado semântico. Textos similares têm embeddings próximos.
#
# Modelo escolhido: all-MiniLM-L6-v2
# - 384 dimensões (leve e rápido)
# - Treinado em inglês (funciona razoavelmente em português)
# - Gratuito (HuggingFace)

print("\n" + "-"*70)
print("CRIANDO MODELO DE EMBEDDINGS")
print("-"*70)

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2",  # Modelo leve e rápido
    model_kwargs={'device': 'cpu'},  # Usar CPU (trocar para 'cuda' se tiver GPU)
    encode_kwargs={'normalize_embeddings': True}  # Normalizar vetores
)

print("✅ Modelo de embeddings criado: all-MiniLM-L6-v2")
print(f"   Dimensões: 384")

# DEMONSTRAÇÃO: Criar embeddings de exemplo
print("\n📊 Demonstração de Embeddings:")
textos_exemplo = [
    "O carro é rápido",
    "O automóvel é veloz",
    "O computador é lento"
]

print("\nTextos de exemplo:")
for i, texto in enumerate(textos_exemplo):
    print(f"{i+1}. '{texto}'")

# Criar embeddings
embs_exemplo = [embeddings.embed_query(t) for t in textos_exemplo]

# Calcular similaridade (usando cosine similarity manualmente)
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

sim_1_2 = cosine_similarity([embs_exemplo[0]], [embs_exemplo[1]])[0][0]
sim_1_3 = cosine_similarity([embs_exemplo[0]], [embs_exemplo[2]])[0][0]

print(f"\n📏 Similaridades:")
print(f"   'carro' vs 'automóvel': {sim_1_2:.4f} (similares! ✅)")
print(f"   'carro' vs 'computador': {sim_1_3:.4f} (diferentes ✅)")
print("   → Embeddings capturam significado semântico!")

# ============================================================================
# SEÇÃO 4: CARREGAR E PROCESSAR DOCUMENTOS
# ============================================================================
# Reutilizando conhecimento do Dia 3
# PASSO 1: Carregar documento de texto
# PASSO 2: Dividir em chunks menores

print("\n" + "-"*70)
print("CARREGANDO E PROCESSANDO DOCUMENTOS")
print("-"*70)

# Criar documento de exemplo se não existir
documento_exemplo = """# Carros e Automóveis

Um carro, também chamado de automóvel ou veículo, é um meio de transporte motorizado.

## Tipos de Motores

### Motor a Gasolina
O motor a gasolina é um dos mais comuns. Funciona através da combustão interna, 
onde a gasolina é misturada com ar e queimada nos cilindros. É eficiente para 
uso urbano e oferece boa aceleração.

### Motor Diesel
O motor diesel é mais econômico que o motor a gasolina. Utiliza combustível diesel 
e funciona através de alta compressão. É comum em veículos de carga e transporte 
pesado devido ao seu torque elevado.

### Motor Elétrico
O motor elétrico é o mais moderno. Funciona com baterias recarregáveis e não 
emite poluentes. Carros elétricos são silenciosos e muito eficientes em termos 
de energia. São o futuro do transporte sustentável.

## Componentes Principais

### Transmissão
A transmissão transfere a potência do motor para as rodas. Pode ser manual 
ou automática. Transmissões modernas têm múltiplas marchas para eficiência.

### Sistema de Freios
Os freios são essenciais para segurança. Podem ser a disco ou a tambor. 
Freios modernos incluem sistema ABS para evitar travamento das rodas.

### Suspensão
A suspensão absorve impactos e mantém o conforto. Sistemas modernos 
ajustam-se automaticamente para diferentes condições de estrada.
"""

# Salvar documento de exemplo
with open("documento_carros.txt", "w", encoding="utf-8") as f:
    f.write(documento_exemplo)

print("✅ Documento de exemplo criado: documento_carros.txt")

# Carregar documento
loader = TextLoader("documento_carros.txt", encoding="utf-8")
docs = loader.load()

print(f"✅ Documento carregado: {len(docs)} arquivo(s)")

# Dividir em chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,  # Tamanho de cada chunk
    chunk_overlap=50,  # Overlap entre chunks para manter contexto
    length_function=len,
    separators=["\n\n", "\n", " ", ""]  # Ordem de separadores
)

chunks = text_splitter.split_documents(docs)
print(f"✅ Documento dividido: {len(chunks)} chunks")

# Mostrar exemplo de chunk
print(f"\n📄 Exemplo de Chunk (primeiros 200 caracteres):")
print(f"   {chunks[0].page_content[:200]}...")

# ============================================================================
# SEÇÃO 5: CRIAR VECTOR STORE COM CHROMA
# ============================================================================
# Por que Chroma: Vector database local, simples e gratuito
# Ideal para desenvolvimento e testes
#
# O que acontece:
# 1. Cada chunk é convertido em embedding (vetor)
# 2. Embeddings são armazenados em índice otimizado
# 3. Índice permite busca rápida por similaridade

print("\n" + "-"*70)
print("CRIANDO VECTOR STORE COM CHROMA")
print("-"*70)

# Criar vector store
# IMPORTANTE: Primeira execução demora (cria embeddings de todos os chunks)
# Execuções futuras são rápidas (carrega do disco)
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db"  # Pasta para persistir dados
)

print(f"✅ Vector store criado com sucesso!")
print(f"   Documentos indexados: {len(chunks)}")
print(f"   Persistido em: ./chroma_db")

# ============================================================================
# SEÇÃO 6: CRIAR RETRIEVER SEMÂNTICO
# ============================================================================
# Retriever: Componente que busca documentos relevantes
# search_type="similarity": Busca por similaridade semântica
# k=3: Retorna os 3 documentos mais relevantes

print("\n" + "-"*70)
print("CRIANDO RETRIEVER SEMÂNTICO")
print("-"*70)

retriever = vectorstore.as_retriever(
    search_type="similarity",  # Busca por similaridade
    search_kwargs={"k": 3}  # Retornar 3 documentos mais relevantes
)

print("✅ Retriever configurado")
print("   Tipo de busca: Semântica (embeddings)")
print("   Documentos por query: 3")

# DEMONSTRAÇÃO: Testar retriever com query sobre sinônimos
print("\n📊 Demonstração de Busca Semântica:")
query_teste = "veículo veloz"  # Usando sinônimos
print(f"\nQuery: '{query_teste}'")
print("   (Note: documento usa 'carro', 'automóvel', não 'veículo')")

docs_encontrados = retriever.invoke(query_teste)
print(f"\n✅ Encontrados {len(docs_encontrados)} documentos relevantes:")

for i, doc in enumerate(docs_encontrados):
    print(f"\n--- Documento {i+1} ---")
    print(doc.page_content[:150] + "...")

print("\n   → Busca semântica encontrou docs relevantes mesmo sem palavra exata!")

# ============================================================================
# SEÇÃO 7: CONFIGURAR LLM
# ============================================================================
# Usar Groq com modelo Llama 3.1 70B
# Por que: Rápido, gratuito, qualidade excelente

print("\n" + "-"*70)
print("CONFIGURANDO LLM")
print("-"*70)

llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0  # Determinístico (mesma resposta para mesma query)
)

print("✅ LLM configurado: Groq Llama 3.1 70B")

# ============================================================================
# SEÇÃO 8: CRIAR PROMPT TEMPLATE
# ============================================================================
# Prompt instrui o LLM a:
# - Usar apenas o contexto fornecido
# - Admitir quando não sabe
# - Ser objetivo e claro

print("\n" + "-"*70)
print("CRIANDO PROMPT TEMPLATE")
print("-"*70)

template = """Você é um assistente especializado em responder perguntas baseado em contexto fornecido.

IMPORTANTE:
- Use APENAS as informações do contexto abaixo
- Se a resposta não estiver no contexto, diga: "Não encontrei essa informação no contexto fornecido."
- Seja objetivo e claro
- Cite partes relevantes do contexto quando possível

Contexto:
{context}

Pergunta: {question}

Resposta detalhada:"""

prompt = ChatPromptTemplate.from_template(template)

print("✅ Prompt template criado")

# ============================================================================
# SEÇÃO 9: CRIAR RAG CHAIN COM LCEL
# ============================================================================
# RAG Chain: Retrieval (busca) + Augmented (aumenta prompt) + Generation (gera resposta)
#
# Fluxo:
# 1. Retriever busca documentos relevantes
# 2. format_docs formata documentos em string
# 3. Prompt template é preenchido com context + question
# 4. LLM gera resposta baseada no prompt
# 5. StrOutputParser extrai string da resposta

print("\n" + "-"*70)
print("CRIANDO RAG CHAIN COM LCEL")
print("-"*70)

# Função auxiliar para formatar documentos
def format_docs(docs):
    """
    Formata lista de documentos em string única.
    
    Args:
        docs: Lista de documentos retornados pelo retriever
        
    Returns:
        str: Documentos concatenados com quebras de linha
    """
    return "\n\n".join([doc.page_content for doc in docs])

# Criar RAG chain usando LCEL (LangChain Expression Language)
rag_chain = (
    {
        "context": retriever | format_docs,  # Busca documentos e formata
        "question": RunnablePassthrough()     # Passa pergunta direto
    }
    | prompt          # Aplica template de prompt
    | llm            # Gera resposta com LLM
    | StrOutputParser()  # Extrai string do output
)

print("✅ RAG Chain criada com sucesso!")
print("\nFluxo da chain:")
print("   1. Query → Retriever (busca semântica)")
print("   2. Docs relevantes → format_docs")
print("   3. Context + Question → Prompt Template")
print("   4. Prompt → LLM")
print("   5. LLM output → StrOutputParser → Resposta final")

# ============================================================================
# SEÇÃO 10: TESTAR RAG CHAIN
# ============================================================================
# Testar com diferentes tipos de queries:
# 1. Query direta (palavra exata no documento)
# 2. Query com sinônimos (testar busca semântica)
# 3. Query conceitual (testar entendimento de contexto)

print("\n" + "="*70)
print("TESTANDO RAG AVANÇADO COM BUSCA SEMÂNTICA")
print("="*70)

queries = [
    "Como funciona o motor a gasolina?",
    "Qual tipo de motor é mais econômico?",
    "Fale sobre veículos elétricos",  # Sinônimo: veículo = carro
    "O que é transmissão automática?"
]

for query in queries:
    print(f"\n{'-'*70}")
    print(f"❓ Pergunta: {query}")
    print(f"{'-'*70}")
    
    # Invocar RAG chain
    resposta = rag_chain.invoke(query)
    
    print(f"\n💡 Resposta:")
    print(resposta)

# ============================================================================
# SEÇÃO 11: RAG CHAIN COM FONTES (BONUS)
# ============================================================================
# Versão melhorada que retorna resposta + documentos fonte
# Útil para rastreabilidade e debugging

print("\n" + "="*70)
print("BONUS: RAG COM FONTES (RASTREABILIDADE)")
print("="*70)

# Chain que retorna resposta + fontes
rag_chain_com_fontes = (
    {
        "context": retriever,  # Retorna docs completos (não formata ainda)
        "question": RunnablePassthrough()
    }
    | (lambda x: {
        "resposta": (
            {"context": format_docs(x["context"]), "question": x["question"]}
            | prompt | llm | StrOutputParser()
        ),
        "fontes": x["context"]
    })
)

# Testar
query_exemplo = "Como funciona o motor elétrico?"
print(f"\n❓ Pergunta: {query_exemplo}")
print(f"{'-'*70}")

resultado = rag_chain_com_fontes.invoke(query_exemplo)

print(f"\n💡 Resposta:")
print(resultado['resposta'])

print(f"\n📚 Fontes ({len(resultado['fontes'])} documentos):")
for i, doc in enumerate(resultado['fontes']):
    print(f"\n{i+1}. {doc.page_content[:200]}...")

# ============================================================================
# SEÇÃO 12: COMPARAÇÃO COM RAG BÁSICO
# ============================================================================
# Demonstrar diferença entre RAG básico (BM25) e RAG avançado (embeddings)

print("\n" + "="*70)
print("COMPARAÇÃO: RAG BÁSICO vs RAG AVANÇADO")
print("="*70)

print("\n📊 Teste de Sinônimos:")
print("-" * 70)

# Query com sinônimo
query_sinonimo = "Fale sobre automóveis movidos a eletricidade"
#                       ↓ sinônimos ↓
# Documento real: "carro", "motor elétrico"

print(f"\nQuery: '{query_sinonimo}'")
print("\nPalavras-chave na query: 'automóveis', 'eletricidade'")
print("Palavras no documento: 'carro', 'motor elétrico'")
print("\nRAG Básico (BM25): ❌ Não encontraria (palavras diferentes)")
print("RAG Avançado (Embeddings): ✅ Encontra (entende significado)")

# Testar
resposta_sinonimo = rag_chain.invoke(query_sinonimo)
print(f"\n💡 Resposta do RAG Avançado:")
print(resposta_sinonimo)

# ============================================================================
# CONCLUSÃO
# ============================================================================
print("\n" + "="*70)
print("CONCLUSÃO")
print("="*70)

print("""
✅ Sistema RAG Avançado implementado com sucesso!

📚 O que aprendemos:
1. Embeddings capturam significado semântico
2. Vector databases permitem busca eficiente por similaridade
3. Chroma é simples e eficaz para desenvolvimento
4. Busca semântica é superior a busca literal
5. RAG chain integra retrieval + geração perfeitamente

🎯 Vantagens do RAG Avançado:
- ✅ Entende sinônimos
- ✅ Busca por significado, não apenas palavras
- ✅ Mais relevante que busca literal
- ✅ Escalável para muitos documentos
- ✅ Production-ready

📈 Próximos passos:
- Dia 5: Usar RAG avançado como ferramenta de Agents
- Experimentar FAISS para melhor performance
- Testar com documentos maiores e mais complexos
- Explorar embeddings multilíngues para português
""")

print("="*70)
print("FIM DO EXEMPLO")
print("="*70)

