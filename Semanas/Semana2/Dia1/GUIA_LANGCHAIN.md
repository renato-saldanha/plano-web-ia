# 📚 Guia Completo: LangChain Básico

Este guia fornece uma introdução detalhada ao LangChain, o framework mais popular para criar aplicações com LLMs (Large Language Models).

---

## 📋 Índice

1. [O que é LangChain?](#-o-que-é-langchain)
2. [Por que usar LangChain?](#-por-que-usar-langchain)
3. [Instalação e Setup](#-instalação-e-setup)
4. [Conceitos Básicos](#-conceitos-básicos)
5. [Primeiro Exemplo](#-primeiro-exemplo)
6. [Comparação com Código Manual](#-comparação-com-código-manual)
7. [Próximos Passos](#-próximos-passos)

---

## 🎯 O que é LangChain?

**LangChain** é um framework Python de código aberto criado para facilitar o desenvolvimento de aplicações com LLMs (Large Language Models).

### Definição Simples

Pense no LangChain como uma **camada de abstração** que simplifica o uso de LLMs. Em vez de escrever código manual para cada API diferente (Groq, OpenAI, Gemini, Claude), você usa uma interface unificada.

### Analogia

Imagine que você precisa dirigir carros diferentes:
- **Sem LangChain:** Precisa aprender como ligar, acelerar e frear cada modelo específico
- **Com LangChain:** Todos os carros têm os mesmos controles básicos, você só muda o "motor" (LLM)

---

## 💡 Por que usar LangChain?

### Problemas do Código Manual (Semana 1)

Na Semana 1, aprendemos a usar APIs diretamente. Isso funcionou, mas:

1. **Código Repetitivo**
   ```python
   # Sempre precisa criar cliente, fazer chamada, tratar resposta
   client = Groq(api_key=api_key)
   response = client.chat.completions.create(...)
   result = response.choices[0].message.content
   ```

2. **Difícil Trocar LLMs**
   - Cada API tem sintaxe diferente
   - Precisa reescrever código para cada LLM
   - Difícil comparar resultados

3. **Sem Padrões**
   - Cada desenvolvedor faz diferente
   - Difícil manter e escalar
   - Não aproveita padrões da indústria

### Vantagens do LangChain

1. **✅ Menos Código**
   - Reduz boilerplate significativamente
   - Código mais limpo e legível

2. **✅ Trocar LLMs Facilmente**
   - Mesma interface para todos os LLMs
   - Trocar de Groq para Gemini = mudar 1 linha

3. **✅ Padrão da Indústria**
   - Framework mais usado
   - Comunidade grande e ativa
   - Documentação excelente

4. **✅ Funcionalidades Avançadas**
   - Chains (sequências de operações)
   - RAG (Retrieval-Augmented Generation)
   - Agents (agentes autônomos)
   - Memory (memória entre conversas)

---

## 🔧 Instalação e Setup

### Passo 1: Instalar LangChain

```bash
# Ativar ambiente virtual primeiro
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

# Instalar LangChain e integrações
pip install langchain langchain-groq langchain-google-genai langchain-anthropic
```

### Passo 2: Verificar Instalação

```bash
python -c "import langchain; print(langchain.__version__)"
```

Deve mostrar a versão instalada (ex: `0.1.0`).

### Passo 3: Configurar Variáveis de Ambiente

Certifique-se de que seu arquivo `.env` (na raiz do projeto) contém:

```env
GROQ_API_KEY=sua_chave_groq_aqui
GEMINI_API_KEY=sua_chave_gemini_aqui
ANTHROPIC_API_KEY=sua_chave_anthropic_aqui
```

**Nota:** Você já configurou isso na Semana 1! ✅

---

## 📚 Conceitos Básicos

### 1. LLM (Large Language Model)

**O que é:** Um modelo de linguagem (Groq, Gemini, Claude, GPT-4, etc.)

**No LangChain:** Representado por classes como `ChatGroq`, `ChatGoogleGenerativeAI`, `ChatAnthropic`

**Exemplo:**
```python
from langchain_groq import ChatGroq

llm = ChatGroq(model="llama-3.1-8b-instant")
```

### 2. Prompt

**O que é:** A entrada (pergunta/texto) que você envia para o LLM

**No LangChain:** Pode ser string simples ou `PromptTemplate` (mais avançado)

**Exemplo:**
```python
prompt = "Explique o que é Python em 2 frases"
```

### 3. Chain

**O que é:** Sequência de operações conectadas

**No LangChain:** Conecta múltiplas operações (prompt → LLM → processamento → resposta)

**Exemplo:**
```python
# Chain simples: Prompt → LLM → Resposta
chain = prompt | llm
```

**Nota:** Chains serão exploradas em detalhes no Dia 2.

### 4. Message

**O que é:** Mensagem estruturada para conversas

**No LangChain:** `HumanMessage` (usuário), `AIMessage` (assistente), `SystemMessage` (sistema)

**Exemplo:**
```python
from langchain_core.messages import HumanMessage

message = HumanMessage(content="Olá!")
```

---

## 🚀 Primeiro Exemplo

Vamos criar um exemplo simples comparando código manual vs LangChain.

### Código Manual (Semana 1)

```python
# hello_ai_groq.py (Semana 1)
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

response = client.chat.completions.create(
    messages=[{"role": "user", "content": "Olá! Me apresente."}],
    model="llama-3.1-8b-instant"
)

print(response.choices[0].message.content)
```

**Linhas de código:** ~10 linhas  
**Complexidade:** Média (precisa entender estrutura da API)

### Código com LangChain

```python
# exemplo_langchain_basico.py
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

load_dotenv()

# Criar LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

# Criar mensagem
message = HumanMessage(content="Olá! Me apresente.")

# Invocar LLM
response = llm.invoke([message])

print(response.content)
```

**Linhas de código:** ~15 linhas (similar)  
**Complexidade:** Baixa (mais intuitivo)  
**Vantagem:** Mesma sintaxe funciona para qualquer LLM!

### Trocar LLM (Vantagem Real)

**Código Manual:** Precisa reescrever tudo
```python
# Trocar para Gemini = código completamente diferente
from google import generativeai
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("Olá!")
```

**LangChain:** Trocar 1 linha
```python
# Trocar para Gemini = mudar apenas a classe
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-pro")  # Só mudou esta linha!
response = llm.invoke([message])  # Resto igual!
```

---

## 🔍 Comparação com Código Manual

### Tabela Comparativa

| Aspecto | Código Manual | LangChain |
|---------|---------------|-----------|
| **Linhas de código** | ~10-15 | ~10-15 |
| **Legibilidade** | Média | Alta |
| **Trocar LLM** | Difícil (reescrever) | Fácil (1 linha) |
| **Padrões** | Cada um faz diferente | Padrão da indústria |
| **Funcionalidades avançadas** | Implementar manualmente | Já incluídas (Chains, RAG, Agents) |
| **Curva de aprendizado** | Média | Baixa (após setup inicial) |

### Quando Usar Cada Abordagem?

**Use Código Manual quando:**
- Projeto muito simples (1-2 chamadas)
- Precisa de controle total sobre requisições
- Não quer dependências extras

**Use LangChain quando:**
- Projeto vai crescer
- Precisa trocar LLMs facilmente
- Quer usar Chains, RAG, Agents
- Quer seguir padrões da indústria

---

## 📖 Estrutura de um Script LangChain

### Padrão Básico

```python
# 1. Imports
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os

# 2. Configuração
load_dotenv()

# 3. Criar LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

# 4. Criar mensagem
message = HumanMessage(content="Seu prompt aqui")

# 5. Invocar LLM
response = llm.invoke([message])

# 6. Processar resposta
print(response.content)
```

### Explicação de Cada Parte

1. **Imports:** Importar classes necessárias
2. **Configuração:** Carregar variáveis de ambiente
3. **Criar LLM:** Instanciar o modelo desejado
4. **Criar mensagem:** Preparar entrada para o LLM
5. **Invocar:** Enviar mensagem e receber resposta
6. **Processar:** Usar resposta conforme necessário

---

## 🎯 Parâmetros Comuns

### Temperature

**O que é:** Controla criatividade/aleatoriedade (0.0 a 1.0)

**Valores:**
- `0.0`: Determinístico, sempre mesma resposta
- `0.7`: Balanceado (padrão recomendado)
- `1.0`: Muito criativo, respostas variadas

**Exemplo:**
```python
llm = ChatGroq(temperature=0.7)  # Balanceado
```

### Max Tokens

**O que é:** Limite máximo de tokens na resposta

**Exemplo:**
```python
llm = ChatGroq(max_tokens=500)  # Máximo 500 tokens
```

### Model

**O que é:** Qual modelo usar (depende do LLM)

**Exemplos:**
```python
# Groq
llm = ChatGroq(model="llama-3.1-8b-instant")

# Gemini
llm = ChatGoogleGenerativeAI(model="gemini-pro")

# Claude
llm = ChatAnthropic(model="claude-3-sonnet-20240229")
```

---

## 🔄 Próximos Passos

Agora que você entendeu o básico:

1. **Execute o exemplo:** `exemplo_langchain_basico.py`
2. **Complete os exercícios:** `exercicios_langchain.md`
3. **Compare com código manual:** Veja diferenças práticas
4. **Dia 2:** Aprender Chains e sequências

---

## 📚 Recursos Adicionais

### Documentação Oficial
- [LangChain Docs](https://python.langchain.com/)
- [LangChain Quickstart](https://python.langchain.com/docs/get_started/introduction)
- [LangChain LLMs](https://python.langchain.com/docs/integrations/llms/)

### Tutoriais
- [LangChain YouTube](https://www.youtube.com/@LangChain)
- [LangChain Tutorials](https://python.langchain.com/docs/tutorials)

### Comunidade
- [LangChain Discord](https://discord.gg/langchain)
- [LangChain GitHub](https://github.com/langchain-ai/langchain)

---

## ❓ Perguntas Frequentes

### Preciso aprender tudo de uma vez?

**Não!** Comece com o básico (hoje). Chains, RAG e Agents vêm nos próximos dias.

### LangChain é obrigatório?

**Não!** Mas é altamente recomendado para projetos profissionais. Código manual funciona, mas LangChain facilita muito.

### Posso misturar código manual com LangChain?

**Sim!** LangChain é flexível. Você pode usar onde faz sentido.

### Qual LLM usar?

**Para começar:** Groq (gratuito e rápido)  
**Para produção:** Depende do caso. Teste vários e escolha o melhor.

---

**Última atualização:** 1 Dez 2025  
**Próximo:** Execute `exemplo_langchain_basico.py` e complete os exercícios!

