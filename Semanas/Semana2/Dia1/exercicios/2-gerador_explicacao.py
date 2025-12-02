from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from colorama import Fore, Style

load_dotenv()

# Função para gerar uma explicação sobre um tópico


def gerar_explicacao(topic: str) -> str:
    """
    Função para gerar uma explicação sobre um tópico usando o modelo Groq.
    Args:
        topic: str - O tópico sobre o qual a explicação será gerada.
    Returns:
        str - A explicação gerada formatada com cores.        
    """
    # Cria uma mensagem de sistema que informa que o usuário é um especialista em um determinado tópico.
    system_message = SystemMessage(
        content=f"Você é um especialista em {topic}.."
        "Explique de forma clara e didática."
    )
    # Cria uma mensagem de usuário que solicita uma explicação sobre o tópico.
    human_message = HumanMessage(
        content=f"Explique o que é {topic} em 3 frases."
    )
    # Cria uma instância do modelo Groq.
    llm = ChatGroq(model="llama-3.3-70b-versatile")
    # Envia a mensagem para o modelo e recebe a resposta.
    response = llm.invoke([system_message, human_message])
    # Retorna a explicação gerada formatada com cores.

    return f"{Fore.BLUE}Explicação: {Fore.RESET}{Fore.CYAN}{response.content}{Fore.RESET}"


if __name__ == "__main__":
    # Solicita ao usuário sobre qual tópico ele quer uma explicação.
    topic = input(
        f"{Fore.YELLOW}Olá! \nSobre qual tópico você quer uma explicação? {Fore.RESET}")
    # Imprime a explicação gerada.
    print(gerar_explicacao(topic))
