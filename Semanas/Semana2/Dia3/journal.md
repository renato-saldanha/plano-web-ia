# 📝 Journal - Dia 3 (Quarta-feira, 3 Dez 2025)

## 🎯 Objetivo do Dia
RAG básico - Busca e geração com LangChain. Criar sistema que busca informações em documentos antes de gerar resposta.

---

## ✅ O que foi feito hoje?

### Manhã/Tarde
- [ X] Leitura do GUIA_RAG_BASICO.md
- [ X] Execução do exemplo_referencia.py
- [ X] Criação de sistema RAG simples
- [ X] Criação de sistema RAG com documentos reais
- [ X] Criação de sistema RAG completo
- [ X] Completar exercícios guiados

### Detalhes das Tarefas
Estudei sobre os conteitos de RAG, aplique no template e fiz os exercícios

## 🎓 O que aprendi hoje?

### Conceitos Novos
- **RAG (Retrieval-Augmented Generation):**
  - O que é: Uma forma de obter informações privadas sem precisar retreinar um modelo.
  - Por que usar: Responde em cima do contexto fornecido evitando alucinações.
  - Quando usar: Na necessidade de ter um produto onde se precisa de informações sensíveis ou então informações especícifcas.

- **Document Loaders:**
  - O que são: Biblioteca do LangChain usada para ler arquivos web, txt, PDF, etc...
  - Como funcionam: Ao Definir o loader usa-se o evento load() para carregar o arquivo.
  - Exemplos práticos: 
     loader = TextLoader(arquivo, encoding = "utf-8")
     documento = loader.load()

- **Text Splitters:**
  - O que são: Usado para criar chunks a partir de um arquivo carregado.
  - Por que dividir documentos: Quando eles são muito grandes.
  - Como funcionam: Após definir o splitter, define os chunks usando o evento splitter_documents()

- **Retrievers:**
  - O que são: 
  - Como funcionam: 
  - Diferença entre busca simples e busca semântica: 

- **Chain RAG:**
  - Como criar: 
  - Quando usar: 
  - Exemplo prático: 

### Ferramentas Utilizadas
- LangChain versão: 1.1.0
- Componentes utilizados: 
    import os
    import random
    import time
    from dotenv import load_dotenv  
    from langchain_community.document_loaders import TextLoader
    from langchain_core.tools import retriever
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    from langchain_community.retrievers import BM25Retriever
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.runnables import RunnablePassthrough
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_groq import ChatGroq
    from concurrent.futures import ThreadPoolExecutor 

- LLMs testados: 
  Groq
### Desafios Enfrentados
- Assimilar o modo como funcionava a estrutura do Chain com map reduce

---

## 💡 Insights e Reflexões

### O que funcionou bem?
- toda a logica

### O que poderia ser melhorado?
- tratamento de erros



**Vantagens do RAG:**
1. Busca dados direcionados.


**Quando usar cada abordagem:**
- Geração simples: Busca sem necessidade de resultados sensíveis
- RAG: Busca onde necessite de um contexto sensível ou direcionado.


## 📊 Métricas do Dia

- **Tempo total:** 4 horas (meta: 2h a 2h30min)
- **Exercícios completados:** 3 / 3
- **Sistemas RAG criados:** 3
- **Commits:** 1
- **Linhas de código:** 600+

---

## 🔗 Links e Referências Úteis

- [LangChain RAG Tutorial](https://python.langchain.com/docs/use_cases/question_answering/)
- [Document Loaders](https://python.langchain.com/docs/modules/data_connection/document_loaders/)
- 

---

## 📝 Notas Adicionais

_(Espaço livre para anotações)_

---

**Data:** 3 Dez 2025  
**Status:** 🟡 Em progresso

