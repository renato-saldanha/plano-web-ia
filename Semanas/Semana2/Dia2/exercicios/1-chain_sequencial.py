from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant")

# ============================================================================
# Exercicio 1: CHAIN SEQUENCIAL SIMPLES
# ============================================================================
# Objetivo: Criar uma chain que recebe um tópico e gera uma explicação curta
#
# Passos:
# 1. Criar ChatPromptTemplate com template que aceita {topic}
# 2. Conectar com llm usando operador |
# 3. Conectar com StrOutputParser() para obter string
# 4. Invocar chain com {"topic": "Python"}
#
# Dica: Consulte exemplo_referencia.py seção 2


def sequencial_chain():
    """
    Exercicio 1: Criar chain sequencial simples

    Returns:
        Chain que gera explicação sobre um tópico
    """

    # Cria o prompt com o ChatPromptTemplate com template que aceita {topic}
    prompt = ChatPromptTemplate.from_template(
        "Me diga uma curiosidade sobre {topic}")

    # Conecta o prompt com o llm usando o operador |
    sequencial_chain = prompt | llm | StrOutputParser()

    return sequencial_chain


if __name__ == "__main__":
    print("Testando chain sequencial:")

    # Cria a chain sequencial
    seq_chain = sequencial_chain()

    # Invoca a chain com {"topic": "Python"}
    result = seq_chain.invoke({"topic": "Python"})
    print(result)
