# 📚 Guia Completo: RAG Avançado com Vector Databases

## 📋 Índice

1. [Conceitos Fundamentais](#1-conceitos-fundamentais)
2. [Vector Databases](#2-vector-databases)
3. [Implementação Prática](#3-implementação-prática)
4. [Comparação: RAG Básico vs Avançado](#4-comparação-rag-básico-vs-avançado)
5. [Troubleshooting](#5-troubleshooting)
6. [Boas Práticas](#6-boas-práticas)

---

## 1. Conceitos Fundamentais

### 1.1 O que são Embeddings?

**Definição Simples:**
Embeddings são representações numéricas de texto que capturam significado semântico.

**Analogia:**
Imagine que cada palavra ou frase é um ponto em um mapa multidimensional. Palavras com significados similares ficam próximas no mapa, palavras diferentes ficam distantes.

```
No mapa de embeddings:
"cachorro" está perto de "cão" ✅
"cachorro" está longe de "computador" ✅
```

### 1.2 Como Funcionam Embeddings?

**Processo:**
1. **Texto entra** → "O cachorro late"
2. **Modelo de embeddings processa** → Rede neural treinada
3. **Vetor numérico sai** → [0.23, -0.45, 0.67, ..., 0.12]

**Características:**
- **Dimensões:** Geralmente 384, 768, 1536 ou mais números
- **Normalização:** Valores entre -1 e 1
- **Semântica:** Vetores próximos = significados similares

**Exemplo Visual:**
```python
# Texto original
texto1 = "O carro é rápido"
texto2 = "O automóvel é veloz"
texto3 = "O computador é lento"

# Embeddings (simplificado para 3 dimensões)
embedding1 = [0.8, 0.2, 0.1]  # carro + velocidade
embedding2 = [0.78, 0.25, 0.09]  # muito similar!
embedding3 = [0.1, 0.05, 0.9]  # muito diferente
```

### 1.3 Por que Embeddings Capturam Significado?

**Treinamento:**
Modelos de embeddings são treinados em bilhões de textos para aprender padrões:

- **Contexto:** Palavras que aparecem juntas ficam próximas
- **Sinônimos:** Palavras usadas em contextos similares ficam próximas
- **Relações:** Relações semânticas são capturadas (rei - homem + mulher ≈ rainha)

**Exemplo de Treinamento:**
```
Textos de treinamento:
- "O cachorro late"
- "O cão late"
- "O cachorro corre"
- "O cão corre"

Modelo aprende: "cachorro" ≈ "cão"
```

### 1.4 Similaridade entre Embeddings

**Cosine Similarity (Similaridade Cosine):**
Medida matemática de quão similares são dois vetores.

**Fórmula:**
```
similarity = cos(θ) = (A · B) / (||A|| ||B||)
```

**Valores:**
- `1.0`: Idênticos (mesmo significado)
- `0.8-0.99`: Muito similares (sinônimos, contextos similares)
- `0.5-0.79`: Relacionados (mesmo tópico)
- `0.0-0.49`: Pouco relacionados
- `< 0`: Opostos (raro em textos naturais)

**Exemplo Prático:**
```python
from sklearn.metrics.pairwise import cosine_similarity

# Embeddings (exemplo simplificado)
emb_carro = [[0.8, 0.2, 0.1]]
emb_automovel = [[0.78, 0.25, 0.09]]
emb_computador = [[0.1, 0.05, 0.9]]

# Calcular similaridade
sim_carro_automovel = cosine_similarity(emb_carro, emb_automovel)
# Resultado: 0.98 (muito similar!)

sim_carro_computador = cosine_similarity(emb_carro, emb_computador)
# Resultado: 0.15 (pouco similar)
```

### 1.5 Modelos de Embeddings Populares

| Modelo                            | Dimensões     | Qualidade | Velocidade | Uso |
|--------                           |-----------            |-----------|------------|-----|
| `all-MiniLM-L6-v2`                | 384           | 🟡 Boa          | 🟢 Rápido | Desenvolvimento |
| `all-mpnet-base-v2`               | 768           | 🟢 Excelente    | 🟡 Médio | Produção balanceada |
| `text-embedding-3-small` (OpenAI) | 1536          | 🟢 Excelente   | 🟢 Rápido | Produção (pago) |
| `text-embedding-3-large` (OpenAI) | 3072          | 🟢🟢 Superior  | 🟡 Médio | Produção premium |

**Recomendação para Dia 4:**
- Usar `all-MiniLM-L6-v2` (gratuito, rápido, suficiente para aprender)

---

## 2. Vector Databases

### 2.1 O que são Vector Databases?

**Definição:**
Bancos de dados otimizados para armazenar e buscar vetores (embeddings) eficientemente.

**Problema que Resolvem:**
- Banco de dados tradicional: "Encontre documento com palavra 'carro'"
- Vector database: "Encontre documentos semanticamente similares a 'carro'"

**Diferença:**
```
SQL Database:
SELECT * FROM docs WHERE text LIKE '%carro%'
→ Busca literal, não encontra "automóvel"

Vector Database:
SELECT * FROM docs ORDER BY similarity(embedding, query_embedding) LIMIT 5
→ Busca semântica, encontra "automóvel", "veículo", "transporte"
```

### 2.2 Como Funcionam Vector Databases?

**Fluxo:**
1. **Indexação:**
   - Documentos são convertidos em embeddings
   - Embeddings são armazenados em índice otimizado
   - Índice permite busca rápida por proximidade

2. **Busca:**
   - Query é convertida em embedding
   - Vector DB busca embeddings mais próximos (nearest neighbors)
   - Retorna documentos correspondentes aos embeddings encontrados

**Estrutura Interna:**
```
Vector Database:
┌─────────────────────────────────┐
│ ID  | Documento       | Embedding │
├─────────────────────────────────┤
│ 1   | "carro rápido"  | [0.8, ...]│
│ 2   | "automóvel"     | [0.78,...]│
│ 3   | "computador"    | [0.1, ...]│
└─────────────────────────────────┘

Query: "veículo veloz"
Query Embedding: [0.79, 0.23, 0.08]

Vector DB calcula:
- Distance(query, doc1) = 0.02 ← Próximo!
- Distance(query, doc2) = 0.03 ← Próximo!
- Distance(query, doc3) = 0.95 ← Distante

Retorna: doc1, doc2 (mais relevantes)
```

### 2.3 Comparação: Chroma vs FAISS vs Pinecone

#### Chroma

**Características:**
- ✅ Local e gratuito
- ✅ Fácil de usar (API simples)
- ✅ Persiste dados automaticamente
- ✅ Ótimo para desenvolvimento
- ⚠️ Performance limitada (milhares de docs OK, milhões não)

**Quando usar:**
- Desenvolvimento e testes
- Protótipos
- Aplicações com poucos documentos (< 100k)

**Exemplo:**
```python
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings()
vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory="./chroma_db"
)
```

#### FAISS

**Características:**
- ✅ Muito rápido (otimizado pelo Facebook)
- ✅ Gratuito e open-source
- ✅ Escalável (milhões de docs)
- ⚠️ Mais complexo de usar
- ⚠️ Requer gerenciamento manual de persistência

**Quando usar:**
- Produção com muitos documentos
- Performance crítica
- Aplicações locais (sem custo cloud)

**Exemplo:**
```python
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings()
vectorstore = FAISS.from_documents(
    documents=docs,
    embedding=embeddings
)
# Salvar
vectorstore.save_local("faiss_index")
# Carregar
vectorstore = FAISS.load_local("faiss_index", embeddings)
```

#### Pinecone

**Características:**
- ✅ Cloud-based (não precisa hospedar)
- ✅ Muito escalável (bilhões de vetores)
- ✅ Gerenciamento automático
- ⚠️ Pago (plano gratuito limitado)
- ⚠️ Requer conexão internet

**Quando usar:**
- Produção enterprise
- Escalabilidade massiva necessária
- Time sem expertise em infraestrutura

**Exemplo:**
```python
from langchain_community.vectorstores import Pinecone
import pinecone

pinecone.init(api_key="sua-chave")
vectorstore = Pinecone.from_documents(
    documents=docs,
    embedding=embeddings,
    index_name="meu-index"
)
```

### 2.4 Comparação Resumida

| Aspecto | Chroma | FAISS | Pinecone |
|---------|--------|-------|----------|
| **Custo** | 🟢 Grátis | 🟢 Grátis | 🟡 Pago |
| **Setup** | 🟢 Fácil | 🟡 Médio | 🟢 Fácil |
| **Performance** | 🟡 Boa | 🟢 Excelente | 🟢 Excelente |
| **Escalabilidade** | 🟡 Limitada | 🟢 Alta | 🟢🟢 Massiva |
| **Persistência** | 🟢 Automática | 🟡 Manual | 🟢 Automática |
| **Local/Cloud** | 🟢 Local | 🟢 Local | ⚠️ Cloud |

**Recomendação para Dia 4:**
- **Começar com Chroma** (simples e suficiente)
- **Experimentar FAISS** (entender diferença de performance)

---

## 3. Implementação Prática

### 3.1 Criando Embeddings com HuggingFace

**Passo a Passo:**

#### Passo 1: Instalar Dependências
```bash
pip install sentence-transformers
```

#### Passo 2: Importar e Configurar
```python
from langchain_community.embeddings import HuggingFaceEmbeddings

# Criar modelo de embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2",  # Modelo leve e rápido
    model_kwargs={'device': 'cpu'},  # Usar CPU (ou 'cuda' para GPU)
    encode_kwargs={'normalize_embeddings': True}  # Normalizar vetores
)
```

#### Passo 3: Criar Embeddings de Textos
```python
# Embeddings de um texto
texto = "O carro é rápido"
embedding = embeddings.embed_query(texto)

print(f"Dimensões: {len(embedding)}")  # 384
print(f"Primeiros 5 valores: {embedding[:5]}")
# Saída: [0.023, -0.045, 0.067, 0.012, -0.089]
```

#### Passo 4: Calcular Similaridade
```python
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Criar embeddings de múltiplos textos
textos = [
    "O carro é rápido",
    "O automóvel é veloz",
    "O computador é lento"
]

embs = [embeddings.embed_query(t) for t in textos]

# Calcular similaridade entre texto 1 e os outros
sim_1_2 = cosine_similarity([embs[0]], [embs[1]])[0][0]
sim_1_3 = cosine_similarity([embs[0]], [embs[2]])[0][0]

print(f"Similaridade carro-automóvel: {sim_1_2:.2f}")  # ~0.85
print(f"Similaridade carro-computador: {sim_1_3:.2f}")  # ~0.15
```

### 3.2 Setup Chroma Vector Store

**Passo a Passo:**

#### Passo 1: Instalar Chroma
```bash
pip install chromadb
```

#### Passo 2: Carregar Documentos (reutilizar Dia 3)
```python
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Carregar documento
loader = TextLoader("documento.txt", encoding="utf-8")
docs = loader.load()

# Dividir em chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = text_splitter.split_documents(docs)

print(f"Número de chunks: {len(chunks)}")
```

#### Passo 3: Criar Vector Store
```python
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# Criar embeddings model
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Criar vector store a partir dos documentos
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db"  # Pasta para persistir dados
)

print("Vector store criado com sucesso!")
```

**O que acontece internamente:**
1. Chroma cria embedding de cada chunk automaticamente
2. Armazena embeddings em índice otimizado
3. Persiste dados na pasta `./chroma_db`

#### Passo 4: Carregar Vector Store Existente
```python
# Sessão futura: carregar vector store já criado
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)
```

### 3.3 Busca Semântica com Chroma

**Passo a Passo:**

#### Passo 1: Criar Retriever
```python
# Criar retriever do vector store
retriever = vectorstore.as_retriever(
    search_type="similarity",  # Tipo de busca (similarity = mais comum)
    search_kwargs={"k": 3}  # Número de documentos a retornar
)
```

#### Passo 2: Buscar Documentos
```python
# Buscar documentos relevantes
query = "Como funciona um motor?"
docs_relevantes = retriever.invoke(query)

# Mostrar resultados
for i, doc in enumerate(docs_relevantes):
    print(f"\n--- Documento {i+1} ---")
    print(doc.page_content)
    print(f"Metadata: {doc.metadata}")
```

#### Passo 3: Busca Direta com Scores
```python
# Busca com scores de similaridade
query = "Como funciona um motor?"
docs_com_scores = vectorstore.similarity_search_with_score(query, k=3)

for doc, score in docs_com_scores:
    print(f"\nScore: {score:.2f}")
    print(f"Conteúdo: {doc.page_content[:100]}...")
```

**Interpretação de Scores:**
- Chroma usa distância euclidiana (menor = mais similar)
- Score típico: 0.0-2.0
- < 0.5: Muito relevante
- 0.5-1.0: Relevante
- > 1.0: Pouco relevante

### 3.4 RAG Chain Completo com LCEL

**Passo a Passo:**

#### Passo 1: Setup Completo
```python
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente
load_dotenv()

# LLM
llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

# Embeddings e Vector Store
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)

# Retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
```

#### Passo 2: Criar Prompt Template
```python
# Template de prompt
template = """Você é um assistente especializado em responder perguntas baseado em contexto fornecido.

Use APENAS as informações do contexto abaixo para responder a pergunta.
Se a resposta não estiver no contexto, diga "Não encontrei essa informação no contexto fornecido."

Contexto:
{context}

Pergunta: {question}

Resposta detalhada:"""

prompt = ChatPromptTemplate.from_template(template)
```

#### Passo 3: Criar RAG Chain com LCEL
```python
# Função auxiliar para formatar documentos
def format_docs(docs):
    return "\n\n".join([doc.page_content for doc in docs])

# RAG Chain usando LCEL
rag_chain = (
    {
        "context": retriever | format_docs,  # Busca e formata documentos
        "question": RunnablePassthrough()     # Passa pergunta direto
    }
    | prompt          # Aplica template
    | llm            # Gera resposta
    | StrOutputParser()  # Extrai string
)
```

#### Passo 4: Testar RAG Chain
```python
# Fazer perguntas
questions = [
    "Como funciona um motor?",
    "Qual a diferença entre gasolina e diesel?",
    "O que é um turbocompressor?"
]

for q in questions:
    print(f"\n{'='*60}")
    print(f"Pergunta: {q}")
    print(f"{'='*60}")
    
    resposta = rag_chain.invoke(q)
    print(f"\nResposta: {resposta}")
```

#### Passo 5: Versão com Fontes
```python
# RAG Chain que retorna resposta + fontes
rag_chain_com_fontes = (
    {
        "context": retriever,  # Retorna docs completos
        "question": RunnablePassthrough()
    }
    | (lambda x: {
        "resposta": (
            {"context": x["context"] | format_docs, "question": x["question"]}
            | prompt | llm | StrOutputParser()
        ),
        "fontes": x["context"]
    })
)

# Testar
resultado = rag_chain_com_fontes.invoke("Como funciona um motor?")
print(f"Resposta: {resultado['resposta']}")
print(f"\nFontes ({len(resultado['fontes'])} documentos):")
for i, doc in enumerate(resultado['fontes']):
    print(f"\n{i+1}. {doc.page_content[:100]}...")
```

### 3.5 Alternativa: FAISS

**Implementação com FAISS:**

```python
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Criar embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Criar FAISS vector store
vectorstore_faiss = FAISS.from_documents(
    documents=chunks,
    embedding=embeddings
)

# Salvar localmente
vectorstore_faiss.save_local("faiss_index")

# Carregar em sessão futura
vectorstore_faiss = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True  # Necessário para carregar
)

# Usar exatamente igual a Chroma
retriever_faiss = vectorstore_faiss.as_retriever(search_kwargs={"k": 3})
```

**Diferenças práticas:**
- FAISS é geralmente 2-5x mais rápido que Chroma
- FAISS requer `save_local()` manual
- Chroma persiste automaticamente
- API é quase idêntica

---

## 4. Comparação: RAG Básico vs Avançado

### 4.1 Diferenças Fundamentais

| Aspecto | RAG Básico (Dia 3) | RAG Avançado (Dia 4) |
|---------|--------------------|-----------------------|
| **Busca** | BM25 (palavras-chave) | Embeddings (semântica) |
| **Entende sinônimos** | ❌ Não | ✅ Sim |
| **Entende contexto** | ❌ Limitado | ✅ Sim |
| **Escalabilidade** | 🟡 Milhares de docs | 🟢 Milhões de docs |
| **Performance** | 🟢 Rápido (setup) | 🟡 Médio (requer index) |
| **Complexidade** | 🟢 Simples | 🟡 Média |
| **Produção** | ⚠️ Protótipo | ✅ Production-ready |
| **Custo** | 🟢 Zero | 🟡 Embeddings (se usar API) |

### 4.2 Exemplo Comparativo

**Setup:**
- Documentos sobre carros
- Query: "Qual veículo é mais econômico?"

**RAG Básico (BM25):**
```python
# BM25 busca palavra "veículo" literalmente
# Se documento usa "carro" ou "automóvel", não encontra
# Resultado: Documentos que contêm palavra "veículo"
```

**RAG Avançado (Embeddings):**
```python
# Embeddings entendem:
# "veículo" ≈ "carro" ≈ "automóvel" ≈ "transporte"
# Resultado: Documentos sobre carros, automóveis, veículos
# Mesmo que não usem palavra exata "veículo"
```

### 4.3 Casos de Uso Recomendados

**Use RAG Básico (BM25) quando:**
- ✅ Prototipando rapidamente
- ✅ Busca literal é suficiente (documentos técnicos com termos exatos)
- ✅ Poucos documentos (< 100)
- ✅ Sem orçamento para embeddings
- ✅ Performance de setup é crítica

**Use RAG Avançado (Embeddings) quando:**
- ✅ Aplicação em produção
- ✅ Busca semântica necessária (linguagem natural)
- ✅ Muitos documentos (> 100)
- ✅ Qualidade de resposta é crítica
- ✅ Usuários usam sinônimos ou linguagem variada

### 4.4 Performance Comparativa

**Testes práticos (1000 documentos):**

| Métrica | BM25 | Chroma | FAISS |
|---------|------|--------|-------|
| **Setup inicial** | < 1s | ~10s | ~5s |
| **Busca (query)** | < 50ms | ~200ms | ~50ms |
| **Relevância** | 🟡 60% | 🟢 85% | 🟢 85% |
| **Memória** | ~10MB | ~200MB | ~100MB |

**Conclusão:**
- BM25: Mais rápido setup, menor relevância
- Chroma: Boa relevância, mais lento
- FAISS: Melhor equilíbrio (relevância + velocidade)

---

## 5. Troubleshooting

### 5.1 Problemas Comuns

#### Problema 1: Instalação do chromadb falha

**Erro:**
```
ERROR: Could not build wheels for chromadb
```

**Solução:**
```bash
# Atualizar pip e setuptools
pip install --upgrade pip setuptools wheel

# Instalar chromadb novamente
pip install chromadb

# Se ainda falhar (Windows), instalar Visual C++ Build Tools:
# https://visualstudio.microsoft.com/visual-cpp-build-tools/
```

#### Problema 2: sentence-transformers demora muito

**Erro:**
```
Downloading model... (taking forever)
```

**Explicação:**
- Primeira vez baixa modelo (~400MB)
- É normal demorar 2-5 minutos
- Cache: `~/.cache/huggingface/` (Linux/Mac) ou `%USERPROFILE%\.cache\huggingface\` (Windows)

**Solução:**
- Aguardar o download completar
- Próximas execuções usarão cache (rápido)

#### Problema 3: Busca semântica retorna documentos irrelevantes

**Sintomas:**
```python
query = "carros rápidos"
# Retorna documentos sobre computadores?!
```

**Causas possíveis:**
1. **Modelo de embeddings fraco:** Usar modelo melhor
2. **Chunks muito grandes:** Reduzir chunk_size
3. **Poucos documentos:** Adicionar mais exemplos
4. **Query muito genérica:** Ser mais específico

**Soluções:**
```python
# 1. Usar modelo melhor
embeddings = HuggingFaceEmbeddings(
    model_name="all-mpnet-base-v2"  # Melhor que MiniLM
)

# 2. Ajustar chunk size
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,  # Menor = mais granular
    chunk_overlap=50
)

# 3. Aumentar k (número de documentos)
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 5}  # Buscar mais documentos
)
```

#### Problema 4: FAISS - "allow_dangerous_deserialization"

**Erro:**
```
ValueError: Loading this object requires allow_dangerous_deserialization
```

**Solução:**
```python
vectorstore = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True  # Adicionar este parâmetro
)
```

**Explicação:**
- FAISS usa pickle para salvar
- pickle pode ser inseguro (código malicioso)
- Parâmetro confirma que você confia no arquivo

#### Problema 5: Memória insuficiente

**Sintomas:**
```
MemoryError: Unable to allocate array
```

**Causas:**
- Muitos documentos sendo processados de uma vez
- Modelo de embeddings muito grande

**Soluções:**
```python
# 1. Processar em batches
from tqdm import tqdm

batch_size = 100
for i in tqdm(range(0, len(chunks), batch_size)):
    batch = chunks[i:i+batch_size]
    vectorstore.add_documents(batch)

# 2. Usar modelo menor
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"  # Mais leve
)
```

### 5.2 Debugging Tips

**1. Verificar embeddings:**
```python
# Ver embedding de um texto
emb = embeddings.embed_query("teste")
print(f"Dimensões: {len(emb)}")  # Deve ser 384/768/1536
print(f"Valores: {emb[:5]}")  # Devem ser floats entre -1 e 1
```

**2. Verificar vector store:**
```python
# Contar documentos
print(f"Documentos no vector store: {vectorstore._collection.count()}")

# Buscar manualmente
results = vectorstore.similarity_search("teste", k=3)
for doc in results:
    print(doc.page_content[:100])
```

**3. Verbose mode:**
```python
# Ver o que está acontecendo
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3},
    verbose=True  # Mostra logs
)
```

---

## 6. Boas Práticas

### 6.1 Escolha de Modelo de Embeddings

**Critérios:**
1. **Dimensões:** Mais dimensões = melhor qualidade, mas mais lento
2. **Idioma:** Verificar se modelo foi treinado em português
3. **Domínio:** Alguns modelos são especializados (médico, legal, etc.)

**Recomendações:**

**Para Português:**
```python
# Opção 1: Multilingual (inclui português)
embeddings = HuggingFaceEmbeddings(
    model_name="paraphrase-multilingual-MiniLM-L12-v2"
)

# Opção 2: Específico português (melhor)
embeddings = HuggingFaceEmbeddings(
    model_name="neuralmind/bert-base-portuguese-cased"
)
```

**Para Inglês:**
```python
# Rápido e bom
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Melhor qualidade
embeddings = HuggingFaceEmbeddings(
    model_name="all-mpnet-base-v2"
)
```

### 6.2 Otimização de Chunk Size

**Regra geral:**
- Chunks muito pequenos: Perdem contexto
- Chunks muito grandes: Perdem granularidade

**Recomendações por tipo de documento:**

```python
# Documentos técnicos (precisão importante)
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

# Documentos narrativos (contexto importante)
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)

# Documentos estruturados (FAQ, etc.)
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=0  # Sem overlap se estrutura é clara
)
```

### 6.3 Número de Documentos Retrieval (k)

**Recomendações:**

```python
# Perguntas simples e diretas
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

# Perguntas complexas (precisam mais contexto)
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 5}
)

# Análise comparativa
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 10}  # Mais documentos para comparar
)
```

**Trade-off:**
- Mais documentos (k alto): Mais contexto, mas mais tokens = mais caro
- Menos documentos (k baixo): Menos contexto, pode perder informação

### 6.4 Persistência e Backup

**Chroma:**
```python
# Persistência é automática
vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)

# Backup: Copiar pasta chroma_db
# Windows: xcopy chroma_db chroma_db_backup /E /I
# Linux/Mac: cp -r chroma_db chroma_db_backup
```

**FAISS:**
```python
# Salvar manualmente
vectorstore.save_local("faiss_index")

# Carregar
vectorstore = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

# Backup: Copiar pasta faiss_index
```

### 6.5 Cache de Embeddings

**Problema:**
- Criar embeddings é lento
- Mesmos documentos são processados múltiplas vezes

**Solução: Cache**

```python
from functools import lru_cache

@lru_cache(maxsize=1000)
def cached_embed(text: str):
    return embeddings.embed_query(text)

# Usar cached_embed em vez de embeddings.embed_query
```

### 6.6 Monitoramento de Performance

**Medir tempo de busca:**
```python
import time

start = time.time()
results = retriever.invoke("query")
end = time.time()

print(f"Tempo de busca: {(end-start)*1000:.2f}ms")
```

**Medir relevância (manual):**
```python
# Para cada query, verificar se documentos retornados são relevantes
query = "carros rápidos"
results = retriever.invoke(query)

for i, doc in enumerate(results):
    print(f"\n{i+1}. {doc.page_content[:200]}")
    # Avaliar: Relevante? Sim/Não
```

---

## 📚 Recursos Adicionais

### Documentação Oficial:
- [LangChain Vector Stores](https://python.langchain.com/docs/modules/data_connection/vectorstores/)
- [LangChain Embeddings](https://python.langchain.com/docs/modules/data_connection/text_embedding/)
- [Chroma Docs](https://docs.trychroma.com/)
- [FAISS Wiki](https://github.com/facebookresearch/faiss/wiki)

### Papers:
- [Sentence-BERT](https://arxiv.org/abs/1908.10084) - Modelo de embeddings
- [Dense Passage Retrieval](https://arxiv.org/abs/2004.04906) - RAG research

### Tutoriais:
- [LangChain RAG Tutorial](https://python.langchain.com/docs/tutorials/rag/)
- [Chroma Quickstart](https://docs.trychroma.com/getting-started)

---

**Última atualização:** 4 Dez 2025  
**Versão:** 1.0  
**Autor:** Plano de Desenvolvimento 2 Meses Web + IA

