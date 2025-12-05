
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda, RunnablePassthrough
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant")

# ============================================================================
# Exercicio 4: CHAIN COMPLEXA (BÔNUS)
# ============================================================================
# Objetivo: Combinar todas as chains anteriores em uma pipeline completa
#
# Passos:
# 1. Usar chain sequencial para gerar conteúdo
# 2. Usar chain paralela para analisar conteúdo gerado
# 3. Combinar usando operador |
# 4. Testar pipeline completa
#
# Dica: Consulte exemplo_referencia.py seção 6


def complex_chain():
    """
    Exercicio 4: Criar chain complexa combinando outras chains

    Returns:
        Chain que gera e analisa conteúdo
    """

    # Cria a chain para gerar o resumo
    generate_chain = (ChatPromptTemplate.from_template("Gere um resumo sobre {topic}.")
                      | llm | StrOutputParser())
    # Cria a chain para analisar o resumo
    analysis_chain = (ChatPromptTemplate.from_template("Analise o seguinte resumo: {summary}. Retorne um resumo mais detalhado e completo.")
                      | llm | StrOutputParser())
    # Cria a chain para extrair as palavras-chave
    keywords_chain = (ChatPromptTemplate.from_template("Extraia as palavras-chave do seguinte resumo: {summary}. Retorne as palavras-chave em formato markdown.")
                      | llm | StrOutputParser())

    text = {"summary": RunnablePassthrough()}

    # Cria chain paralela
    parallel_chain = RunnableParallel({            
            "analysis": analysis_chain,
            "keywords": keywords_chain
        })

    # Cria a pipeline complexa
    content_pipeline = (
        generate_chain
        # Passa o resumo para a próxima chain
        | text
        | parallel_chain)

    return content_pipeline


if __name__ == "__main__":
    print("\nTestando chain complexa:")
    
    # Cria a chain complexa
    complex_chain = complex_chain()
    # Invoca a chain complexa com o tópico "IA"
    result = complex_chain.invoke({"topic": "IA"})

    # Imprime os resultados
    print("Análise:", result["analysis"])
    print("Palavras-chave:", result["keywords"])
