import os
from dotenv import load_dotenv
from groq import Groq
import time
from datetime import datetime
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S',
)

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY não encontrada no arquivo .env")

client = Groq(api_key=groq_api_key)


# Função para gerar conteúdo para um tema de blog
def gerar_conteudo_tema(tema: str):
    """
    Gerar conteúdo para um tema de blog usando Groq.

    Args:
        tema: str - O tema do blog

    Returns:
        str - O conteúdo gerado para o tema de blog
    """

    if not tema:
        raise ValueError("Favor escolher um tema.")

    prompt = f"""
    Você é um blogueiro inteirado sobre o mundo da tecnologia.
    Gere um parágrafo introdutório para um blog sobre o tema: {tema}.
    O parágrafo deve ser em markdown formatado.
    O parágrafo deve ser escrito como se o blogueiro estivesse em um mundo de
    RPG(Role Playing Game) com tema de tecnologia.
    """

    logging.info(f"Prompt: {prompt}")
    logging.info("--------------------------------")

    try:
        inicio_ms = time.perf_counter() * 1000

        llm_response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=0.45,
            max_tokens=200,
        )

        if not llm_response:
            raise ValueError(
                "Não foi possível encontrar um modelo disponível."
                "Verifique a API."
            )

        resposta = llm_response.choices[0].message.content
        fim_ms = time.perf_counter() * 1000
        tempo_resposta_ms = fim_ms - inicio_ms
        velocidade = llm_response.usage.total_tokens / (tempo_resposta_ms/1000)

        logging.info("=" * 60)
        logging.info(f"Modelo usado: {llm_response.model}")
        logging.info(f"Tokens usados: {llm_response.usage.total_tokens}")
        logging.info(f"Tempo de resposta: {tempo_resposta_ms:.0f} ms "
                     f"({tempo_resposta_ms/1000:.3f} segundos)")
        logging.info(f"   - Velocidade: {velocidade:.1f} tokens/segundo")
        logging.info("=" * 60)

        salvar_arquivo_tema_blog(tema, resposta)
        return resposta + "\n" + "=" * 60
    except Exception as e:
        logging.error(f"Erro ao gerar conteúdo para o tema: {tema}")
        logging.error(f"Erro: {e}")
        return None


# Função para salvar o conteúdo gerado em um arquivo markdown
def salvar_arquivo_tema_blog(tema: str, conteudo: str):
    """
    Salvar o conteúdo gerado em um arquivo markdown.

    Args:
        tema: str - O tema do blog
        conteudo: str - O conteúdo gerado para o tema de blog

    Returns:
        None
    """

    try:
        if not os.path.exists("resultado_blog"):
            os.makedirs("resultado_blog")
    except Exception as e:
        logging.error(f"Erro ao criar diretório de resultados: {e}")
        return None

    data_geracao = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    try:
        caminho_arquivo = f"resultado_blog/{tema}.md"
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(f"# {tema}\n\n")
            arquivo.write(f"**Data de geração:** {data_geracao}\n\n")
            arquivo.write("---\n\n")
            arquivo.write(conteudo)
    except Exception as e:
        logging.error(f"Erro ao salvar conteúdo em : {e}")
        return None


if __name__ == "__main__":
    logging.info(gerar_conteudo_tema("Inteligência Artificial"))
    logging.info(gerar_conteudo_tema("Python"))
    logging.info(gerar_conteudo_tema("Web Development"))

