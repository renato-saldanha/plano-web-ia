from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_groq import ChatGroq


load_dotenv()


llm = ChatGroq(model="llama-3.1-8b-instant")

# ============================================================================
# Exercicio 3: CHAIN PARALELA
# ============================================================================
# Objetivo: Criar chain que analisa texto em múltiplas dimensões simultaneamente
#
# Passos:
# 1. Criar chain para análise de sentimento
# 2. Criar chain para resumo
# 3. Criar chain para extração de palavras-chave
# 4. Usar RunnableParallel para executar todas em paralelo
# 5. Retornar dicionário com todos os resultados
#
# Dica: Consulte exemplo_referencia.py seção 5


def parallel_chain():
    """
    Exercicio 3: Criar chain paralela

    Returns:
        Chain que executa múltiplas análises em paralelo
    """

    # Cria a chain para sumarizar o código
    summary_chain = (ChatPromptTemplate.from_template("Like a dedicated Experient Codebase Reviewer.Sumarize the following codebase: {codebase}. Return the summary in {language} in markdown format.")
                     | llm | StrOutputParser())
    # Cria a chain para analisar o código
    analysis_chain = (ChatPromptTemplate.from_template("Like a dedicated Experient System Analyst. Analyze the following codebase: {codebase}. Return the summary in {language} in markdown format.")
                      | llm | StrOutputParser())
    # Cria a chain para extração de palavras-chave
    keywords_chain = (ChatPromptTemplate.from_template("Like a dedicated Experient Keywords Extractor. Extract the keywords from the following codebase: {codebase}. Return the keywords in {language} in markdown format.")
                      | llm | StrOutputParser())

    # Cria a chain paralela
    parallel_chain = RunnableParallel({
        "summary": summary_chain,
        "analysis": analysis_chain,
        "keywords": keywords_chain
    })

    return parallel_chain


if __name__ == "__main__":
    # Cria o código de exemplo
    codebase = """
    import time

    def process_data(data):
        result = []
        for i in range(len(data)):
            time.sleep(0.01)  # simula operação lenta desnecessária
            for j in range(len(data)):  # loop redundante
                if data[i] == data[j]:  # comparação repetitiva
                    result.append(data[j])
        return result
    nums = list(range(200))
    output = process_data(nums)
    print("Itens processados:", len(output))
    """

    print("\nTestando chain paralela:")
    # Cria a chain paralela
    chain_par = parallel_chain()
    # Invoca a chain paralela com o código de exemplo
    result = chain_par.invoke({
        "codebase": codebase,
        "language": "PT-BR"
    })
    
    # Imprime os resultados
    print("Keywords:", result["keywords"])
    print("Analysis:", result["analysis"])
    print("Summary:", result["summary"])
