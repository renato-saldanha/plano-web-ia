# 🔗 Guia Completo: Chains e LangChain Expression Language (LCEL)

Este guia explica como criar chains (cadeias) de operações no LangChain usando LCEL, a sintaxe moderna e poderosa do framework.

---

## 📚 Índice

1. [O que são Chains?](#o-que-são-chains)
2. [LangChain Expression Language (LCEL)](#langchain-expression-language-lcel)
3. [Chains Sequenciais](#chains-sequenciais)
4. [Chains Condicionais](#chains-condicionais)
5. [Chains Paralelas](#chains-paralelas)
6. [Composição de Chains](#composição-de-chains)
7. [Streaming com Chains](#streaming-com-chains)
8. [Boas Práticas](#boas-práticas)

---

## O que são Chains?

### Conceito

Uma **Chain** é uma sequência de operações conectadas que processam dados de forma sequencial ou paralela. No contexto do LangChain, chains conectam LLMs, prompts, parsers e outras operações.

### Por que usar Chains?

**Sem Chains (código manual):**
```python
# Código verboso e difícil de manter
prompt = "Gere um resumo sobre Python"
response1 = llm.invoke(prompt)
formatted = format_response(response1.content)
final = translate(formatted, "pt")
```

**Com Chains:**
```python
# Código declarativo e reutilizável
chain = prompt | llm | format_response | translate
final = chain.invoke({"input": "Gere um resumo sobre Python"})
```

**Vantagens:**
- ✅ **Composição:** Reutilizar chains em outras chains
- ✅ **Legibilidade:** Código mais limpo e declarativo
- ✅ **Manutenibilidade:** Fácil de modificar e debugar
- ✅ **Streaming:** Suporte nativo a respostas incrementais
- ✅ **Type Safety:** Type hints completos

---

## LangChain Expression Language (LCEL)

### O que é LCEL?

**LCEL** é uma sintaxe declarativa para criar chains no LangChain. Usa o operador `|` (pipe) para conectar operações, similar ao pipe do Unix.

### Sintaxe Básica

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

# Criar chain usando LCEL
chain = ChatPromptTemplate.from_template("Diga: {input}") | ChatGroq()

# Invocar chain
result = chain.invoke({"input": "Olá!"})
```

### Componentes Básicos

1. **Prompts:** `ChatPromptTemplate`, `PromptTemplate`
2. **LLMs:** `ChatGroq`, `ChatGoogleGenerativeAI`, `ChatAnthropic`
3. **Parsers:** `StrOutputParser`, `JsonOutputParser`
4. **Runnables:** Qualquer objeto que implementa interface `Runnable`

---

## Chains Sequenciais

### Conceito

Chains sequenciais executam operações uma após a outra, passando o resultado de uma para a próxima.

### Exemplo Básico

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

# Criar chain sequencial
chain = (
    ChatPromptTemplate.from_template("Resuma: {text}")
    | ChatGroq(model="llama-3.1-8b-instant")
    | StrOutputParser()
)

# Usar chain
result = chain.invoke({"text": "Python é uma linguagem de programação..."})
print(result)
```

### Fluxo de Dados

```
Input → Prompt Template → LLM → Parser → Output
```

### Exemplo com Múltiplas Operações

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_groq import ChatGroq

# Chain que: gera conteúdo → formata
generate_chain = (
    ChatPromptTemplate.from_template("Gere um parágrafo sobre {topic}")
    | ChatGroq(model="llama-3.1-8b-instant")
    | StrOutputParser()  # Retorna uma STRING
)

format_chain = (
    ChatPromptTemplate.from_template("Formate este texto em markdown:\n\n{text}")
    | ChatGroq(model="llama-3.1-8b-instant")
    | StrOutputParser()
)

# Combinar chains CORRETAMENTE
# ⚠️ IMPORTANTE: generate_chain retorna string, mas format_chain espera dict com "text"
# Por isso precisamos converter a string em um dicionário
full_chain = (
    generate_chain 
    | RunnableLambda(lambda x: {"text": x})  # Converte string → dict
    | format_chain
)

result = full_chain.invoke({"topic": "Inteligência Artificial"})
print(result)
```

**Explicação:**
- `generate_chain` retorna uma **string** (por causa do `StrOutputParser()`)
- `format_chain` espera um **dicionário** com a chave `"text"` (porque o template usa `{text}`)
- `RunnableLambda(lambda x: {"text": x})` converte a string em um dicionário compatível

---

## Chains Condicionais

### Conceito

Chains condicionais executam diferentes operações baseadas em condições ou no conteúdo do input.

### Usando RunnableBranch

```python
from langchain_core.runnables import RunnableBranch
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

# Definir diferentes chains baseadas em condição
short_chain = (
    ChatPromptTemplate.from_template("Resposta curta: {input}")
    | ChatGroq(model="llama-3.1-8b-instant")
    | StrOutputParser()
)

long_chain = (
    ChatPromptTemplate.from_template("Resposta detalhada: {input}")
    | ChatGroq(model="llama-3.1-8b-instant")
    | StrOutputParser()
)

# Função para decidir qual chain usar
def route(input_dict):
    text = input_dict.get("input", "")
    if len(text) < 50:
        return "short"
    return "long"

# Criar chain condicional
conditional_chain = RunnableBranch(
    (lambda x: len(x.get("input", "")) < 50, short_chain),
    long_chain
)

result = conditional_chain.invoke({"input": "Explique Python"})
```

### Usando RunnableLambda

```python
from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

# Chain que decide qual LLM usar baseado no idioma
def choose_llm(input_dict):
    language = input_dict.get("language", "en")
    if language == "pt":
        return ChatGroq(model="llama-3.1-8b-instant")
    else:
        return ChatGroq(model="mixtral-8x7b-32768")

chain = (
    ChatPromptTemplate.from_template("{input}")
    | RunnableLambda(choose_llm)
)

result = chain.invoke({"input": "Olá!", "language": "pt"})
```

---

## Chains Paralelas

### Conceito

Chains paralelas executam múltiplas operações simultaneamente e combinam os resultados.

### Usando RunnableParallel

```python
from langchain_core.runnables import RunnableParallel
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

# Criar múltiplas chains
sentiment_chain = (
    ChatPromptTemplate.from_template("Analise o sentimento: {text}")
    | ChatGroq(model="llama-3.1-8b-instant")
    | StrOutputParser()
)

summary_chain = (
    ChatPromptTemplate.from_template("Resuma: {text}")
    | ChatGroq(model="llama-3.1-8b-instant")
    | StrOutputParser()
)

keywords_chain = (
    ChatPromptTemplate.from_template("Extraia palavras-chave: {text}")
    | ChatGroq(model="llama-3.1-8b-instant")
    | StrOutputParser()
)

# Executar em paralelo
parallel_chain = RunnableParallel({
    "sentiment": sentiment_chain,
    "summary": summary_chain,
    "keywords": keywords_chain
})

result = parallel_chain.invoke({"text": "Python é incrível!"})
print(result)
# {
#   "sentiment": "positivo",
#   "summary": "Texto sobre Python...",
#   "keywords": "Python, programação, linguagem"
# }
```

### Vantagens

- ⚡ **Performance:** Executa operações simultaneamente
- 🔄 **Eficiência:** Reduz tempo total de execução
- 📊 **Flexibilidade:** Combina múltiplas análises

---

## Composição de Chains

### Conceito

Chains podem ser compostas em outras chains, criando hierarquias complexas.

### Exemplo Prático

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableBranch
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

# Chain 1: Gerar conteúdo
generate_chain = (
    ChatPromptTemplate.from_template("Gere conteúdo sobre {topic}")
    | ChatGroq(model="llama-3.1-8b-instant")
    | StrOutputParser()
)

# Chain 2: Revisar conteúdo
review_chain = (
    ChatPromptTemplate.from_template("Revise este texto: {text}")
    | ChatGroq(model="llama-3.1-8b-instant")
    | StrOutputParser()
)

# Chain 3: Formatar
format_chain = (
    ChatPromptTemplate.from_template("Formate em markdown: {text}")
    | ChatGroq(model="llama-3.1-8b-instant")
    | StrOutputParser()
)

# Combinar todas as chains
# ⚠️ IMPORTANTE: generate_chain retorna string, mas as outras chains esperam dict com "text"
from langchain_core.runnables import RunnablePassthrough

content_pipeline = (
    generate_chain
    | {"text": RunnablePassthrough()}  # Converte string → dict com chave "text"
    | RunnableParallel({
        "reviewed": review_chain,
        "formatted": format_chain
    })
)

result = content_pipeline.invoke({"topic": "IA Generativa"})
```

---

## Streaming com Chains

### Conceito

Chains suportam streaming nativo, permitindo receber respostas incrementalmente.

### Exemplo de Streaming

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

chain = (
    ChatPromptTemplate.from_template("Conte uma história sobre {topic}")
    | ChatGroq(model="llama-3.1-8b-instant", streaming=True)
)

# Stream de resposta
for chunk in chain.stream({"topic": "Python"}):
    print(chunk.content, end="", flush=True)
```

### Vantagens do Streaming

- ⚡ **UX melhor:** Usuário vê resposta em tempo real
- 🎯 **Feedback imediato:** Não precisa esperar resposta completa
- 💡 **Eficiência:** Processa enquanto recebe

---

## Boas Práticas

### 1. Nomear Chains Claramente

```python
# ✅ Bom
content_generation_chain = prompt | llm | parser

# ❌ Ruim
chain1 = prompt | llm | parser
```

### 2. Documentar Chains Complexas

```python
"""
Chain que gera conteúdo, revisa e formata.

Fluxo:
1. Gera conteúdo baseado em tópico
2. Revisa conteúdo gerado
3. Formata em markdown
"""
content_pipeline = generate_chain | review_chain | format_chain
```

### 3. Reutilizar Chains

```python
# Criar chain reutilizável
base_chain = prompt_template | llm | parser

# Usar em diferentes contextos
chain_a = base_chain | formatter
chain_b = base_chain | translator
```

### 4. Tratamento de Erros

```python
from langchain_core.runnables import RunnableLambda

def safe_invoke(chain):
    try:
        return chain.invoke(input)
    except Exception as e:
        return {"error": str(e)}

safe_chain = RunnableLambda(safe_invoke)
```

### 5. Testar Chains Incrementalmente

```python
# Testar cada parte separadamente
prompt_result = prompt_template.invoke({"input": "test"})
llm_result = llm.invoke(prompt_result)
parser_result = parser.invoke(llm_result)

# Depois testar chain completa
full_result = chain.invoke({"input": "test"})
```

---

## 📚 Recursos Adicionais

- [LangChain Expression Language Docs](https://python.langchain.com/docs/expression_language/)
- [LCEL Get Started](https://python.langchain.com/docs/expression_language/get_started)
- [Runnable Interface](https://python.langchain.com/docs/expression_language/interface)
- [Streaming Guide](https://python.langchain.com/docs/expression_language/streaming)

---

## 🎯 Próximos Passos

Agora que você entendeu chains básicas, você está pronto para:
- Dia 3: RAG básico (usará chains para buscar e gerar)
- Dia 4: RAG avançado (chains com vector databases)
- Dia 5: Agents (chains autônomas que decidem ações)

---

**Última atualização:** 2 Dez 2025  
**Referências:** Baseado em documentação LangChain de julho de 2025 em diante

