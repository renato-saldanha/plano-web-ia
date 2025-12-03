#!/usr/bin/env python3
"""
Exemplo de Referência: Chains e LCEL no LangChain

Este arquivo demonstra como criar diferentes tipos de chains usando
LangChain Expression Language (LCEL).

Uso:
    python exemplo_referencia.py
"""

import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_groq import ChatGroq

# ============================================================================
# SEÇÃO 1: CONFIGURAÇÃO
# ============================================================================
load_dotenv()

# Criar instância do LLM (reutilizável)
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

# ============================================================================
# SEÇÃO 2: CHAIN SEQUENCIAL SIMPLES
# ============================================================================
# Esta é a forma mais básica de chain: prompt → LLM → parser

print("=" * 60)
print("EXEMPLO 1: Chain Sequencial Simples")
print("=" * 60)

# Criar chain usando LCEL (operador |)
simple_chain = (
    ChatPromptTemplate.from_template("Explique {topic} em 2 frases.")
    | llm
    | StrOutputParser()
)

# Invocar chain
result = simple_chain.invoke({"topic": "Python"})
print(f"Resultado: {result}\n")

# ============================================================================
# SEÇÃO 3: CHAIN COM MÚLTIPLAS OPERAÇÕES
# ============================================================================
# Chain que gera conteúdo e depois formata

print("=" * 60)
print("EXEMPLO 2: Chain com Múltiplas Operações")
print("=" * 60)

# Primeira parte: gerar conteúdo
generate_prompt = ChatPromptTemplate.from_template(
    "Gere um parágrafo curto sobre {topic}"
)

# Segunda parte: formatar em markdown
format_prompt = ChatPromptTemplate.from_template(
    "Formate este texto em markdown com título:\n\n{text}"
)

# Combinar chains
multi_step_chain = (
    generate_prompt
    | llm
    | StrOutputParser()
    | format_prompt
    | llm
    | StrOutputParser()
)

result = multi_step_chain.invoke({"topic": "Inteligência Artificial"})
print(f"Resultado:\n{result}\n")

# ============================================================================
# SEÇÃO 4: CHAIN CONDICIONAL
# ============================================================================
# Chain que escolhe qual operação executar baseado em condição

print("=" * 60)
print("EXEMPLO 3: Chain Condicional")
print("=" * 60)

# Chain para textos curtos
short_chain = (
    ChatPromptTemplate.from_template("Resposta curta: {input}")
    | llm
    | StrOutputParser()
)

# Chain para textos longos
long_chain = (
    ChatPromptTemplate.from_template("Resposta detalhada: {input}")
    | llm
    | StrOutputParser()
)

# Criar chain condicional usando RunnableBranch
conditional_chain = RunnableBranch(
    (lambda x: len(x.get("input", "")) < 50, short_chain),
    long_chain
)

# Testar com texto curto
result_short = conditional_chain.invoke({"input": "Python"})
print(f"Texto curto: {result_short}\n")

# Testar com texto longo
result_long = conditional_chain.invoke({
    "input": "Explique detalhadamente como funciona a programação orientada a objetos em Python, incluindo classes, herança e polimorfismo"
})
print(f"Texto longo: {result_long}\n")

# ============================================================================
# SEÇÃO 5: CHAIN PARALELA
# ============================================================================
# Chain que executa múltiplas operações simultaneamente

print("=" * 60)
print("EXEMPLO 4: Chain Paralela")
print("=" * 60)

# Criar múltiplas chains para análise paralela
sentiment_chain = (
    ChatPromptTemplate.from_template("Analise o sentimento deste texto (positivo/negativo/neutro): {text}")
    | llm
    | StrOutputParser()
)

summary_chain = (
    ChatPromptTemplate.from_template("Resuma este texto em uma frase: {text}")
    | llm
    | StrOutputParser()
)

keywords_chain = (
    ChatPromptTemplate.from_template("Extraia 3 palavras-chave deste texto: {text}")
    | llm
    | StrOutputParser()
)

# Executar todas em paralelo usando RunnableParallel
parallel_chain = RunnableParallel({
    "sentiment": sentiment_chain,
    "summary": summary_chain,
    "keywords": keywords_chain
})

texto_teste = "Python é uma linguagem de programação incrível! É fácil de aprender e muito poderosa."
result = parallel_chain.invoke({"text": texto_teste})

print(f"Texto analisado: {texto_teste}\n")
print(f"Sentimento: {result['sentiment']}")
print(f"Resumo: {result['summary']}")
print(f"Palavras-chave: {result['keywords']}\n")

# ============================================================================
# SEÇÃO 6: CHAIN COMPLEXA (COMPOSIÇÃO)
# ============================================================================
# Combinar sequencial + condicional + paralela

print("=" * 60)
print("EXEMPLO 5: Chain Complexa (Composição)")
print("=" * 60)

# Primeiro: gerar conteúdo
generate_chain = (
    ChatPromptTemplate.from_template("Gere um parágrafo sobre {topic}")
    | llm
    | StrOutputParser()
)

# Depois: analisar em paralelo
analysis_chain = RunnableParallel({
    "sentiment": sentiment_chain,
    "summary": summary_chain,
    "keywords": keywords_chain
})

# Combinar: gerar → analisar
complex_chain = (
    generate_chain
    | {"text": lambda x: x}  # Transformar output em formato esperado
    | analysis_chain
)

result = complex_chain.invoke({"topic": "Machine Learning"})
print(f"Análise do conteúdo gerado:")
print(f"  Sentimento: {result['sentiment']}")
print(f"  Resumo: {result['summary']}")
print(f"  Palavras-chave: {result['keywords']}\n")

# ============================================================================
# SEÇÃO 7: STREAMING COM CHAINS
# ============================================================================
# Chain com streaming de resposta

print("=" * 60)
print("EXEMPLO 6: Streaming com Chain")
print("=" * 60)

# Criar chain com streaming habilitado
streaming_llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7,
    streaming=True
)

streaming_chain = (
    ChatPromptTemplate.from_template("Conte uma história curta sobre {topic}")
    | streaming_llm
)

print("Streaming de resposta:")
for chunk in streaming_chain.stream({"topic": "Python"}):
    if hasattr(chunk, 'content'):
        print(chunk.content, end="", flush=True)
print("\n")

print("=" * 60)
print("Todos os exemplos executados com sucesso!")
print("=" * 60)

