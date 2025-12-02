from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

# Função principal


def main():
    """
    Função principal que cria uma instância do modelo Groq e envia uma mensagem de teste.
    """
    # Cria uma instância do modelo Groq
    llm = ChatGroq(model="llama-3.3-70b-versatile")
    # Cria uma mensagem de teste
    human_message = HumanMessage(
        content="Olá, estou usando langchain, como você está?")
    # Envia a mensagem para o modelo e recebe a resposta
    response = llm.invoke([human_message])
    # Imprime a mensagem do usuário e a resposta do modelo
    print("--------------------------------")
    print(f"Mensagem do usuário: {human_message.content}")
    print(f"Resposta do LLM: {response.content}")
    print("--------------------------------")


if __name__ == "__main__":
    main()
