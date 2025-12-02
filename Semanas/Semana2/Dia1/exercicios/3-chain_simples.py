import os
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from colorama import Fore, Style

load_dotenv()


def gerar_explicacao(topic: str, numero_frases: int) -> str:
    """
    Função para gerar uma explicação sobre um tópico usando o modelo Google Generative AI.
    Args:
        topic: str - O tópico sobre o qual a explicação será gerada.
    Returns:
        str - A explicação gerada.
    """

    prompt = ChatPromptTemplate.from_template(
        "Explique o que é {topic} em {numero_frases} frases"
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
    )

    chain = prompt | llm

    response = chain.invoke({
        "topic": topic,
        "numero_frases": numero_frases,
    })

    return f"{Fore.BLUE}{Style.BRIGHT}Explicação: {Fore.RESET}{Fore.CYAN}{response.content}{Fore.RESET}"


def main():
    # # Solicita ao usuário sobre qual tópico ele quer uma explicação.
    # topic = input(
    #     f"{Fore.YELLOW}Olá! \nSobre qual tópico você quer uma explicação? {Fore.RESET}")
    # # Solicita ao usuário sobre quantas frases ele quer na explicação.
    # numero_frases = input(
    #     f"{Fore.YELLOW}Quantas frases você quer na explicação? {Fore.RESET}")


    topicos = [
        {"conceito": "Python", "num_frases": 3},
        {"conceito": "Machine Learning", "num_frases": 5},
        {"conceito": "Web Development", "num_frases": 2}
    ]

 
    for topico in topicos:
        print(gerar_explicacao(topico["conceito"], topico["num_frases"]))


if __name__ == "__main__":
    main()
