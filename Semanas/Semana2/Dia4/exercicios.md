# 🎯 Exercícios Práticos - RAG Avançado com Vector Databases

## 📋 Objetivo

Consolidar conhecimento através de exercícios práticos progressivos sobre:
- Embeddings e representação vetorial
- Vector databases (Chroma)
- Busca semântica
- Sistema RAG avançado completo

**Tempo estimado total: 20 minutos (parte da fase de Consolidação)**

---

## 📚 Antes de Começar

### Pré-requisitos:
- ✅ `template.py` completo e funcionando
- ✅ Chroma vector store criado com documentos
- ✅ Leitura de `GUIA_RAG_AVANCADO.md` completa

### Arquivos de Referência:
- `GUIA_RAG_AVANCADO.md` - Teoria e implementação
- `exemplo_referencia.py` - Código completo funcionando
- `template.py` - Seu código com TODOs completados

---

## 🏋️ Exercício 1: Embeddings Básicos (5min)

### Objetivo
Entender como embeddings representam texto e calcular similaridade.

### Tarefa
Crie um script que:
1. Cria embeddings de 4 textos diferentes
2. Calcula similaridade entre pares de textos
3. Identifica quais textos são mais similares

### Código Base
```python
from langchain_community.embeddings import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

# Criar modelo de embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Textos para testar
textos = [  
    "O cachorro late no quintal",
    "O cão está latindo",
    "O gato mia na casa",
    "O computador está ligado"
]

# TODO 1: Criar embeddings de todos os textos
# embs = [embeddings.embed_query(t) for t in textos]

# TODO 2: Calcular similaridade entre texto 1 e todos os outros
# for i in range(1, len(textos)):
#     sim = cosine_similarity([embs[0]], [embs[i]])[0][0]
#     print(f"Similaridade '{textos[0]}' vs '{textos[i]}': {sim:.4f}")

# TODO 3: Identificar qual texto é mais similar ao texto 1
```

### Critérios de Aceitação
- [ x] Embeddings criados para todos os textos
- [ x] Similaridade calculada corretamente
- [ X] Texto 2 ("O cão está latindo") é o mais similar ao texto 1 ✅
- [ X] Texto 4 ("O computador...") é o menos similar ao texto 1 ✅

### Resposta Esperada
```
Similaridade 'O cachorro late no quintal' vs 'O cão está latindo': 0.5428
Similaridade 'O cachorro late no quintal' vs 'O gato mia na casa': 0.5161
Similaridade 'O cachorro late no quintal' vs 'O computador está ligado': 0.4778
Similaridade 'O cachorro late no quintal' vs 'A vaca está na casa': 0.4299
Similaridade 'O cachorro late no quintal' vs 'O pato está no quintal': 0.6952

Texto mais similar: "O cão está latindo" (sinônimo!)
```

### Dica
- Se similaridade não faz sentido: Verificar se modelo está carregado corretamente
- Embeddings são arrays grandes (384 números), normalização é importante

---

## 🏋️ Exercício 2: FAISS Vector Store e Busca Semântica (10min)

### Objetivo
Praticar criação de vector store e comparar busca literal vs semântica.

### Tarefa
1. Criar vector store com documentos de teste
2. Realizar buscas usando palavras exatas
3. Realizar buscas usando sinônimos
4. Comparar resultados

### Código Base
```python
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

# Criar embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Documentos de teste
docs = [
    Document(page_content="O carro vermelho é muito rápido", metadata={"id": 1}),
    Document(page_content="O automóvel azul é econômico", metadata={"id": 2}),
    Document(page_content="O veículo verde é espaçoso", metadata={"id": 3}),
    Document(page_content="O computador está quebrado", metadata={"id": 4}),
    Document(page_content="A bicicleta é um meio de transporte", metadata={"id": 5})
]

# TODO 1: Criar vector store
# vectorstore = Chroma.from_documents(
#     documents=docs,
#     embedding=embeddings,
#     persist_directory="./chroma_exercicio2"
# )

# TODO 2: Criar retriever
# retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# TODO 3: Buscar com palavra exata
print("=== Busca 1: Palavra exata 'carro' ===")
# results = retriever.invoke("carro")
# for doc in results:
#     print(f"- {doc.page_content}")

# TODO 4: Buscar com sinônimo 'veículo'
print("\n=== Busca 2: Sinônimo 'veículo' ===")
# results = retriever.invoke("veículo")
# for doc in results:
#     print(f"- {doc.page_content}")

# TODO 5: Buscar com conceito 'transporte rápido'
print("\n=== Busca 3: Conceito 'transporte rápido' ===")
# results = retriever.invoke("transporte rápido")
# for doc in results:
#     print(f"- {doc.page_content}")
```

### Critérios de Aceitação
- [ X] Vector store criado com sucesso
- [ X] Busca 1 ("carro"): Retorna docs 1, 2, 3 (sobre carros/automóveis/veículos) ✅
- [ X] Busca 2 ("veículo"): Retorna docs 1, 2, 3 mesmo sem palavra "veículo" em alguns ✅
- [ X] Busca 3 ("transporte rápido"): Retorna doc 1 (carro rápido) no topo ✅
- [ X] Doc 4 (computador) nunca aparece nas buscas sobre transporte ✅

### Resultado Esperado
```
Busca 1 (carro):
- O carro vermelho é muito rápido ✅
- O automóvel azul é econômico ✅ (sinônimo!)
- O veículo verde é espaçoso ✅ (sinônimo!)

Busca 2 (veículo):
- O veículo verde é espaçoso ✅
- O carro vermelho é muito rápido ✅ (entendeu que carro=veículo!)
- O automóvel azul é econômico ✅ (entendeu que automóvel=veículo!)

Busca 3 (transporte rápido):
- O carro vermelho é muito rápido ✅ (perfeito!)
- A bicicleta é um meio de transporte ✅ (transporte, mas não rápido)
- O veículo verde é espaçoso ✅ (transporte, mas não sobre velocidade)
```

### Análise
**Por que busca semântica é superior:**
- ✅ Entende sinônimos (carro = automóvel = veículo)
- ✅ Entende conceitos (transporte rápido → carro rápido)
- ✅ Não se limita a palavras exatas
- ✅ Ordena por relevância semântica

---

## 🏋️ Exercício 3: RAG Avançado Completo (5min)

### Objetivo
Integrar tudo: embeddings + vector store + LLM em sistema RAG completo.

### Tarefa
Usar o vector store do Exercício 2 para criar RAG chain e responder perguntas.

### Código Base
```python
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

# Usar vector store do Exercício 2
# (ou criar novo se preferir)

# TODO 1: Configurar LLM
# llm = ChatGroq(
#     model="llama-3.1-70b-versatile",
#     api_key=os.getenv("GROQ_API_KEY")
# )

# TODO 2: Criar prompt template
# template = """Responda baseado apenas no contexto:
#
# Contexto:
# {context}
#
# Pergunta: {question}
#
# Resposta:"""
#
# prompt = ChatPromptTemplate.from_template(template)

# TODO 3: Função para formatar documentos
# def format_docs(docs):
#     return "\n\n".join([doc.page_content for doc in docs])

# TODO 4: Criar RAG chain
# rag_chain = (
#     {"context": retriever | format_docs, "question": RunnablePassthrough()}
#     | prompt
#     | llm
#     | StrOutputParser()
# )

# TODO 5: Testar com perguntas
perguntas = [
    "Qual veículo é rápido?",
    "Fale sobre automóveis econômicos",
    "Existe algum transporte espaçoso?"
]

# for pergunta in perguntas:
#     print(f"\n❓ {pergunta}")
#     resposta = rag_chain.invoke(pergunta)
#     print(f"💡 {resposta}")
```

### Critérios de Aceitação
- [ X] RAG chain criada com sucesso
- [ X] Pergunta 1: Responde "carro vermelho" (identificou "rápido") ✅
- [ X] Pergunta 2: Responde "automóvel azul" (entendeu sinônimo) ✅
- [ X] Pergunta 3: Responde "veículo verde" (identificou "espaçoso") ✅
- [ X] Respostas baseadas no contexto, não inventadas ✅

### Resultado Esperado
```
❓ Qual veículo é rápido?
💡 O carro vermelho é muito rápido.

❓ Fale sobre automóveis econômicos
💡 O automóvel azul é econômico.

❓ Existe algum transporte espaçoso?
💡 Sim, o veículo verde é espaçoso.
```

### Validação
**Sistema RAG está funcionando se:**
- ✅ Retriever encontra documentos relevantes (busca semântica)
- ✅ LLM usa apenas contexto fornecido (não inventa)
- ✅ Respostas são precisas e baseadas nos documentos
- ✅ Sistema entende sinônimos e conceitos

**Resultado esperado:**
- FAISS geralmente 2-5x mais rápido em buscas
- Chroma mais fácil de usar (persist automático)

### Desafio 2: RAG com Múltiplos Documentos (20min)

**Objetivo:** Trabalhar com vector store grande e queries complexas.

**Tarefa:**
1. Adicionar 20+ documentos sobre diferentes tópicos
2. Criar RAG system
3. Fazer queries que requerem informação de múltiplos docs
4. Avaliar qualidade das respostas

**Exemplo de query complexa:**
"Compare motores a gasolina com motores elétricos em termos de economia e meio ambiente"

**Critério de sucesso:**
- RAG deve buscar docs sobre gasolina E elétricos
- Resposta deve comparar ambos
- Informação de múltiplos chunks deve ser integrada

### Desafio 3: Embeddings Multilíngues (15min)

**Objetivo:** Testar embeddings com documentos em português.

**Tarefa:**
1. Usar modelo multilíngue: `paraphrase-multilingual-MiniLM-L12-v2`
2. Criar docs em português
3. Comparar com modelo em inglês (`all-MiniLM-L6-v2`)
4. Avaliar qual funciona melhor para português

**Hipótese:**
- Modelo multilíngue deve ter melhor performance em português
- Mas pode ser mais lento

---

## 📊 Resumo dos Exercícios

| Exercício | Tempo | Foco | Critério de Sucesso |
|-----------|-------|------|---------------------|
| 1. Embeddings | 5min | Similaridade | Calcular similaridade corretamente |
| 2. Chroma + Busca | 10min | Vector DB | Busca semântica funciona com sinônimos |
| 3. RAG Completo | 5min | Integração | RAG responde queries corretamente |
| **Total** | **20min** | **Consolidação** | **Sistema RAG funcionando** |

---

## ✅ Checklist de Validação

Após completar os exercícios, você deve ser capaz de:

### Conhecimento Teórico:
- [ X] Explicar o que são embeddings
- [ X] Explicar como vector databases funcionam
- [ X] Explicar diferença entre busca literal e semântica
- [ ] Explicar quando usar Chroma vs FAISS

### Habilidades Práticas:
- [ X] Criar embeddings de textos
- [ X] Calcular similaridade entre embeddings
- [ X] Configurar FAISS vector store
- [ X] Criar retriever semântico
- [ X] Construir RAG chain completa com LCEL
- [ X] Comparar RAG básico vs avançado

### Competências:
- [ X] Escolher chunk_size apropriado
- [ X] Debugar problemas com embeddings
- [ X] Otimizar número de documentos (k) retornados
- [ X] Avaliar qualidade de busca semântica

---

## 🎯 Próximos Passos

Após completar estes exercícios:

1. **Revisar `journal.md`:**
   - Documentar o que aprendeu
   - Anotar dificuldades encontradas
   - Registrar insights importantes

2. **Comparar com Dia 3:**
   - Executar mesmas queries em RAG básico (Dia 3)
   - Executar mesmas queries em RAG avançado (Dia 4)
   - Documentar diferenças observadas

3. **Preparar para Dia 5:**
   - Revisar conceitos de RAG avançado
   - Pensar em como RAG pode ser usado como ferramenta
   - Ler sobre Agents (preview do Dia 5)

---

## 💡 Dicas Finais

### Se travar em algum exercício:
1. **Consultar `GUIA_RAG_AVANCADO.md`** seção correspondente
2. **Ver `exemplo_referencia.py`** código completo
3. **Comparar com `template.py`** sua implementação
4. **Testar partes isoladamente** (embeddings → vector store → RAG)

### Debugging:
```python
# Verificar embeddings
emb = embeddings.embed_query("teste")
print(f"Dimensões: {len(emb)}")  # Deve ser 384

# Verificar vector store
print(f"Docs no vector store: {vectorstore._collection.count()}")

# Verificar retriever
docs = retriever.invoke("teste")
print(f"Docs encontrados: {len(docs)}")
```

### Performance:
- Primeira execução demora (download de modelo + criação de índice)
- Execuções seguintes são rápidas (usa cache)
- Se muito lento: Reduzir número de documentos ou usar modelo menor

---

**Bom trabalho nos exercícios! 🚀**

**Última atualização:** 4 Dez 2025

