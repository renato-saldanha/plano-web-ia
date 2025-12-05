# 📚 Guia Completo: RAG Básico com LangChain

Este guia explica o conceito de RAG (Retrieval-Augmented Generation) e como implementá-lo usando LangChain.

---

## 🎯 O que é RAG?

**RAG (Retrieval-Augmented Generation)** é uma técnica que combina:
1. **Retrieval (Busca):** Busca informações relevantes em documentos/dados
2. **Augmentation (Aumento):** Adiciona essas informações ao prompt
3. **Generation (Geração):** LLM gera resposta baseada no contexto encontrado

### Por que RAG é importante?

**Problemas dos LLMs sem RAG:**
- ❌ Conhecimento limitado (só sabem o que foi treinado até uma data)
- ❌ Sem acesso a dados privados (seus documentos, banco de dados)
- ❌ Podem alucinar (inventar informações quando não sabem)

**Soluções do RAG:**
- ✅ Respostas baseadas em dados reais
- ✅ Acesso a documentos privados
- ✅ Menos alucinações (tem contexto real)
- ✅ Atualização fácil (adicione documentos sem retreinar)

---

## 🔧 Componentes Básicos do RAG

### 1. Document Loaders

**O que são:** Carregam documentos de diferentes fontes (texto, PDF, web, etc.)

**Exemplo básico:**
```python
from langchain_community.document_loaders import TextLoader

# Carregar arquivo de texto
loader = TextLoader("documento.txt")
documents = loader.load()
```

**Loaders comuns:**
- `TextLoader` - Arquivos de texto (.txt)
- `PyPDFLoader` - PDFs (.pdf)
- `DirectoryLoader` - Todos arquivos de uma pasta
- `WebBaseLoader` - Páginas web

### 2. Text Splitters

**O que são:** Dividem documentos grandes em chunks (pedaços) menores

**Por que dividir:**
- LLMs têm limite de tokens
- Chunks menores são mais fáceis de buscar
- Melhor precisão na busca

**Exemplo básico:**
```python
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

# Primeiro, carregar documentos
loader_exemplo = TextLoader("documento.txt")
docs_exemplo = loader_exemplo.load()

# Criar splitter
text_splitter_exemplo = CharacterTextSplitter(
    chunk_size=1000,      # Tamanho de cada chunk
    chunk_overlap=200,     # Sobreposição entre chunks
    separator="\n"         # Separador
)

# Dividir documentos
chunks_exemplo = text_splitter_exemplo.split_documents(docs_exemplo)
```

**Splitters comuns:**
- `CharacterTextSplitter` - Divide por caracteres (um separador fixo)
- `RecursiveCharacterTextSplitter` - Divide recursivamente (recomendado) ⭐
- `TokenTextSplitter` - Divide por tokens (mais preciso, mas mais lento)

### Por que RecursiveCharacterTextSplitter é recomendado?

**Problema do CharacterTextSplitter:**
```python
# CharacterTextSplitter com separator="\n"
texto = "Parágrafo 1\n\nParágrafo 2 muito longo que não cabe em um chunk..."

# Se o parágrafo 2 for maior que chunk_size, ele será cortado no meio!
# Resultado: Chunk quebrado no meio de uma frase/ideia
```

**Solução do RecursiveCharacterTextSplitter:**
```python
# RecursiveCharacterTextSplitter tenta múltiplos separadores em ordem
separators = ["\n\n", "\n", ". ", " ", ""]  # Ordem de prioridade

# 1. Tenta dividir por "\n\n" (parágrafos)
# 2. Se ainda muito grande, tenta "\n" (linhas)
# 3. Se ainda muito grande, tenta ". " (frases)
# 4. Se ainda muito grande, tenta " " (palavras)
# 5. Último recurso: divide por caracteres
```

**Vantagens:**
- ✅ **Preserva estrutura:** Tenta manter parágrafos/frases inteiras
- ✅ **Flexível:** Adapta-se automaticamente ao tipo de texto
- ✅ **Inteligente:** Usa separadores hierárquicos (parágrafo → linha → frase → palavra)
- ✅ **Menos quebras ruins:** Evita cortar no meio de ideias
- ✅ **Funciona com qualquer texto:** Código, markdown, prosa, etc.

**Exemplo prático:**
```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Criar splitter recursivo
recursive_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50,
    # Separadores em ordem de prioridade (padrão já é bom)
    separators=["\n\n", "\n", ". ", " ", ""]
)

# Texto com parágrafos de tamanhos diferentes
texto_exemplo = """
Parágrafo curto.

Parágrafo muito longo que tem várias frases e precisa ser dividido de forma inteligente para não quebrar no meio de uma ideia importante que está sendo explicada aqui.

Outro parágrafo.
"""

# Dividir texto
chunks_recursivos = recursive_splitter.split_text(texto_exemplo)
# Resultado: Chunks que respeitam estrutura (parágrafos → frases → palavras)
```

### 3. Retrievers

**O que são:** Buscam chunks relevantes baseado em uma query (pergunta)

**Busca simples (exemplo básico):**
```python
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.retrievers import BM25Retriever

# Carregar e dividir documentos primeiro
loader_retriever = TextLoader("documento.txt")
docs_retriever = loader_retriever.load()

splitter_retriever = RecursiveCharacterTextSplitter(chunk_size=500)
chunks_retriever = splitter_retriever.split_documents(docs_retriever)

# Criar retriever simples
bm25_retriever = BM25Retriever.from_documents(chunks_retriever)
bm25_retriever.k = 3  # Retornar top 3 chunks

# Buscar chunks relevantes
pergunta_exemplo = "sua pergunta aqui"
chunks_relevantes = bm25_retriever.get_relevant_documents(pergunta_exemplo)
```

**Tipos de retrievers:**
- Busca simples (BM25) - Busca por palavras-chave
- Busca semântica (Vector DB) - Busca por significado (Dia 4)

---

## 🔗 Chain RAG Completa

### Estrutura Básica

```python
from langchain_groq import ChatGroq
from langchain_community.chains import RetrievalQA
from langchain_community.retrievers import BM25Retriever
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
import os

load_dotenv()

# Configurar componentes necessários
llm_basico = ChatGroq(
    model_name="llama-3.1-8b-instant",
    temperature=0,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

# Carregar e preparar documentos
loader_basico = TextLoader("documento.txt")
docs_basico = loader_basico.load()
splitter_basico = RecursiveCharacterTextSplitter(chunk_size=500)
chunks_basico = splitter_basico.split_documents(docs_basico)

# Criar retriever
retriever_basico = BM25Retriever.from_documents(chunks_basico)
retriever_basico.k = 3

# Criar chain RAG
qa_chain_basica = RetrievalQA.from_chain_type(
    llm=llm_basico,
    chain_type="stuff",
    retriever=retriever_basico,
    return_source_documents=True
)

# Fazer pergunta
pergunta_basica = "sua pergunta aqui"
resultado_basico = qa_chain_basica.invoke({"query": pergunta_basica})
print(resultado_basico["result"])
```

### Usando LCEL (LangChain Expression Language)

```python
from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.retrievers import BM25Retriever
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
import os

load_dotenv()

# Configurar LLM
llm_lcel = ChatGroq(
    model_name="llama-3.1-8b-instant",
    temperature=0,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

# Carregar e preparar documentos
loader_lcel = TextLoader("documento.txt")
docs_lcel = loader_lcel.load()
splitter_lcel = RecursiveCharacterTextSplitter(chunk_size=500)
chunks_lcel = splitter_lcel.split_documents(docs_lcel)

# Criar retriever
retriever_lcel = BM25Retriever.from_documents(chunks_lcel)
retriever_lcel.k = 3

# Criar prompt template
prompt_lcel = ChatPromptTemplate.from_template(
    """Responda a seguinte pergunta baseado apenas no contexto fornecido:
    
    Contexto: {context}
    
    Pergunta: {input}
    
    Resposta:"""
)

# Criar chain de documentos
document_chain_lcel = create_stuff_documents_chain(llm_lcel, prompt_lcel)

# Criar chain RAG completa
rag_chain_lcel = create_retrieval_chain(retriever_lcel, document_chain_lcel)

# Fazer pergunta
pergunta_lcel = "sua pergunta aqui"
resultado_lcel = rag_chain_lcel.invoke({"input": pergunta_lcel})
print(resultado_lcel["answer"])
```

---

## 📝 Exemplo Completo Passo a Passo

### Passo 1: Carregar Documentos

```python
from langchain_community.document_loaders import TextLoader

# Criar documento de exemplo (ou carregar arquivo)
with open("documento_python.txt", "w", encoding="utf-8") as f:
    f.write("""
    Python é uma linguagem de programação de alto nível.
    Foi criada por Guido van Rossum em 1991.
    Python é conhecida por sua sintaxe simples e legível.
    """)

# Carregar documento
loader_passo1 = TextLoader("documento_python.txt")
docs_passo1 = loader_passo1.load()
```

### Passo 2: Dividir em Chunks

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Criar splitter
splitter_passo2 = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=50
)

# Dividir documentos
chunks_passo2 = splitter_passo2.split_documents(docs_passo1)
print(f"Total de chunks: {len(chunks_passo2)}")
```

### Passo 3: Criar Retriever

```python
from langchain_community.retrievers import BM25Retriever

# Criar retriever simples
retriever_passo3 = BM25Retriever.from_documents(chunks_passo2)
retriever_passo3.k = 2  # Retornar top 2 chunks

# Testar busca
pergunta_teste = "Quem criou Python?"
chunks_teste = retriever_passo3.get_relevant_documents(pergunta_teste)
print(f"Chunks encontrados: {len(chunks_teste)}")
```

### Passo 4: Criar Chain RAG

```python
from langchain_groq import ChatGroq
from langchain_community.chains import RetrievalQA
from dotenv import load_dotenv
import os

load_dotenv()

# Criar LLM
llm_passo4 = ChatGroq(
    model_name="llama-3.1-8b-instant",
    temperature=0,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

# Criar chain RAG (usa retriever_passo3 criado no passo anterior)
qa_chain_passo4 = RetrievalQA.from_chain_type(
    llm=llm_passo4,
    chain_type="stuff",
    retriever=retriever_passo3,  # Usa retriever do passo 3
    return_source_documents=True
)

# Fazer pergunta
pergunta_passo4 = "Quem criou Python?"
resultado_passo4 = qa_chain_passo4.invoke({"query": pergunta_passo4})
print(f"Resposta: {resultado_passo4['result']}")
print(f"\nFontes: {len(resultado_passo4['source_documents'])} documentos")
```

---

## 🎯 Tipos de Chains RAG

### 1. "Stuff" Chain
- **Como funciona:** Coloca todos os chunks relevantes no prompt
- **Vantagem:** Simples e direto
- **Limitação:** Limitado pelo tamanho do contexto do LLM
- **Quando usar:** Poucos chunks pequenos

### 2. "Map-Reduce" Chain
- **Como funciona:** Processa cada chunk separadamente, depois combina
- **Vantagem:** Funciona com muitos chunks
- **Limitação:** Mais lento, mais chamadas ao LLM
- **Quando usar:** Muitos chunks grandes

### 3. "Refine" Chain
- **Como funciona:** Refina resposta iterativamente com cada chunk
- **Vantagem:** Respostas mais precisas
- **Limitação:** Mais lento, mais chamadas ao LLM
- **Quando usar:** Precisão é mais importante que velocidade

---

## 💡 Boas Práticas

### 1. Tamanho dos Chunks
- **Muito pequeno:** Perde contexto
- **Muito grande:** Difícil de buscar precisamente
- **Recomendado:** 500-1000 caracteres com overlap de 100-200

### 2. Número de Chunks Retornados
- **Muito poucos:** Pode perder informação importante
- **Muitos:** Pode confundir o LLM
- **Recomendado:** 3-5 chunks para maioria dos casos

### 3. Prompts
- Sempre inclua instrução para usar apenas o contexto fornecido
- Peça para citar fontes quando possível
- Seja claro sobre o que fazer quando não encontrar informação

### 4. Tratamento de Erros
- Sempre verifique se encontrou chunks relevantes
- Trate casos onde nenhum chunk é encontrado
- Valide respostas do LLM

---

## 🔍 Debugging e Melhorias

### Verificar Chunks Encontrados
```python
from langchain_groq import ChatGroq
from langchain_community.chains import RetrievalQA
from langchain_community.retrievers import BM25Retriever
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
import os

load_dotenv()

# Configurar sistema RAG completo para debug
llm_debug = ChatGroq(
    model_name="llama-3.1-8b-instant",
    temperature=0,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

loader_debug = TextLoader("documento.txt")
docs_debug = loader_debug.load()
splitter_debug = RecursiveCharacterTextSplitter(chunk_size=500)
chunks_debug = splitter_debug.split_documents(docs_debug)

retriever_debug = BM25Retriever.from_documents(chunks_debug)
retriever_debug.k = 3

qa_chain_debug = RetrievalQA.from_chain_type(
    llm=llm_debug,
    chain_type="stuff",
    retriever=retriever_debug,
    return_source_documents=True
)

# Ver quais chunks foram encontrados
pergunta_debug = "sua pergunta"
resultado_debug = qa_chain_debug.invoke({"query": pergunta_debug})

print(f"Resposta: {resultado_debug['result']}\n")
print("Chunks usados como fonte:")
for i, doc in enumerate(resultado_debug['source_documents'], 1):
    print(f"\nChunk {i}:")
    print(doc.page_content[:200])  # Primeiros 200 caracteres
```

### Ajustar Parâmetros
```python
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.retrievers import BM25Retriever

# Carregar documentos
loader_ajuste = TextLoader("documento.txt")
docs_ajuste = loader_ajuste.load()

# Exemplo 1: Ajustar tamanho de chunks
splitter_original = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks_original = splitter_original.split_documents(docs_ajuste)

splitter_ajustado = RecursiveCharacterTextSplitter(
    chunk_size=500,  # Reduzir para chunks menores (mais precisos)
    chunk_overlap=100  # Ajustar overlap para melhor continuidade
)
chunks_ajustados = splitter_ajustado.split_documents(docs_ajuste)

print(f"Chunks originais: {len(chunks_original)}, Chunks ajustados: {len(chunks_ajustados)}")

# Exemplo 2: Ajustar número de chunks retornados pelo retriever
retriever_ajuste = BM25Retriever.from_documents(chunks_ajustados)
retriever_ajuste.k = 5  # Aumentar de padrão (3) para 5 chunks (mais contexto)

# Testar diferença
pergunta_ajuste = "sua pergunta"
chunks_encontrados = retriever_ajuste.get_relevant_documents(pergunta_ajuste)
print(f"Chunks retornados: {len(chunks_encontrados)}")
```

---

## 📚 Próximos Passos

Depois de dominar RAG básico:
- **Dia 4:** RAG avançado com vector databases (busca semântica)
- **Embeddings:** Representar texto como vetores
- **Vector Stores:** Armazenar e buscar embeddings eficientemente
- **Melhorias:** Re-ranking, filtros, metadados

---

## 🔗 Referências

- [LangChain RAG Tutorial](https://python.langchain.com/docs/use_cases/question_answering/)
- [Document Loaders](https://python.langchain.com/docs/modules/data_connection/document_loaders/)
- [Text Splitters](https://python.langchain.com/docs/modules/data_connection/text_splitters/)
- [Retrievers](https://python.langchain.com/docs/modules/data_connection/retrievers/)

---

**Última atualização:** 3 Dez 2025  
**Referências:** Baseado em documentação LangChain de julho de 2025 em diante

