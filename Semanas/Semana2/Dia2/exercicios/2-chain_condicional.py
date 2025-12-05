import os
from typing import Any
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda, RunnablePassthrough
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant")

# ============================================================================
# Exercicio 2: CHAIN CONDICIONAL
# ============================================================================
# Objetivo: Criar chain que escolhe estratégia baseada no tamanho do input
#
# Passos:
# 1. Criar chain para inputs curtos (< 50 caracteres)
# 2. Criar chain para inputs longos (>= 50 caracteres)
# 3. Usar RunnableBranch para escolher qual usar
# 4. Testar com inputs de diferentes tamanhos
#
# Dica: Consulte exemplo_referencia.py seção 4


def conditional_chain():
    """
    Exercicio 2: Criar chain condicional

    Returns:
        Chain que escolhe estratégia baseada em condição
    """

    # Cria instância dos templates do prompt
    short_template = ChatPromptTemplate.from_template("Resposta longa sobre {input}")
    long_template = ChatPromptTemplate.from_template("Resposta curta sobre {input}")

    # Cria a chain para inputs longos
    long_chain = ( short_template
                  | llm
                  | StrOutputParser())
    # Cria a chain para inputs curtos
    short_chain = ( long_template
                   | llm
                   | StrOutputParser())

    # Cria a chain condicional
    conditional_chain = RunnableBranch(
        (lambda x: len(x.get("input", "")) < 50, short_chain),
        long_chain
    )

    return conditional_chain


if __name__ == "__main__":
    print("Testando chain condicional:")
    cond_chain = conditional_chain()
    result = cond_chain.invoke({"input": "Python"})
    print(result)
