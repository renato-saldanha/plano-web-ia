import os
from dotenv import load_dotenv
from groq import Groq
import time
from datetime import datetime

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY não encontrada no arquivo .env")

client = Groq(api_key=groq_api_key)


def gerar_conteudo_tema(tema: str): 
    if not tema:
        raise ValueError("Favor escolher um tema.")

    prompt = f"""
    Você é um blogueiro inteirado sobre o mundo da tecnologia.
    Gere um parágrafo introdutório para um blog sobre o tema: {tema}.
    O parágrafo deve ser em markdown formatado.
    O parágrafo deve ser escrito como se o blogueiro estivesse em um mundo de RPG(Role Playing Game) com tema de tecnologia.
    """

    print("Prompt:", prompt)
    print("--------------------------------")

    try:
        inicio_ms = time.perf_counter() * 1000

        llm_response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages = [
                {
                    "role" : "user",
                    "content": prompt,                    
                }
            ],
            temperature = 0.45,
            max_tokens = 200,            
        )

        if not llm_response:
            raise Exception("Não foi possível encontrar um modelo disponível, verifique a API.")


        resposta = llm_response.choices[0].message.content
        fim_ms = time.perf_counter() * 1000
        tempo_resposta_ms = fim_ms - inicio_ms

        print("=" * 60)
        print(f"Modelo usado: {llm_response.model}")
        print(f"Tokens usados: {llm_response.usage.total_tokens}")
        print(f"Tempo de resposta: {tempo_resposta_ms:.0f} ms ({tempo_resposta_ms/1000:.3f} segundos)")
        print(f"   - Velocidade: {llm_response.usage.total_tokens / (tempo_resposta_ms/1000):.1f} tokens/segundo")
        print("=" * 60)

        salvar_arquivo_tema_blog(tema, resposta)
        return resposta + "\n" + "=" * 60        
    except Exception as e:
        print(f"Erro ao gerar conteúdo para o tema: {tema}")
        print(f"Erro: {e}")
        return None

def salvar_arquivo_tema_blog(tema: str, conteudo: str):
    if not os.path.exists("resultado_blog"):
        os.makedirs("resultado_blog")

    with open(f"resultado_blog/{tema}.md", "w", encoding="utf-8") as arquivo:
        arquivo.write(f"# {tema}\n\n")
        arquivo.write(f"**Data de geração:** {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n")
        arquivo.write("---\n\n")
        arquivo.write(conteudo)


if __name__ == "__main__":
    print(gerar_conteudo_tema("Inteligência Artificial"))
    print(gerar_conteudo_tema("Python"))
    print(gerar_conteudo_tema("Web Development"))