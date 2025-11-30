import os
import time
from dotenv import load_dotenv
from groq import Groq
from google import genai
from google.genai import types
from openai import OpenAI
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S',
)

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY não encontrada no .env")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY não encontrada no .env")

OPEN_API_KEY = os.getenv("OPEN_API_KEY")
if not OPEN_API_KEY:
    raise ValueError("OPEN_API_KEY não encontrada no .env")

llm_gemini = genai.Client(api_key=GEMINI_API_KEY)
llm_groq = Groq(api_key=GROQ_API_KEY)
llm_openai = OpenAI(api_key=OPEN_API_KEY)


# Função para analisar sentimento com Groq
def analisar_sentimento_groq(prompt: str, texto: str) -> str:
    """
    Analisa o sentimento de um texto usando Groq.
    Args:
        prompt: str - O prompt para analisar o sentimento
        texto: str - O texto a ser analisado
    Returns:
        str - O sentimento do texto
    """

    logging.info(f"Analisando sentimento com Groq: {texto}")
    try:
        inicio_ms = time.perf_counter() * 1000
        response = llm_groq.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,
            max_tokens=10
        )

        fim_ms = time.perf_counter() * 1000
        sentimento_texto = response.choices[0].message.content.strip().lower()
        tempo_resposta_ms = fim_ms - inicio_ms
        tokens = response.usage.total_tokens

        if not sentimento_texto:
            raise Exception("Não foi possível encontrar um sentimento válido."
                            "Verifique a API.")

        return sentimento_texto, tempo_resposta_ms, tokens
    except Exception as e:
        logging.error(f"Erro ao analisar sentimento com Groq: {e}")
        logging.error("=" * 50)
        return None


# Função para analisar sentimento com Gemini
def analisar_sentimento_gemini(prompt: str, texto: str) -> str:
    """
    Analisa o sentimento de um texto usando Gemini.
    Args:
        prompt: str - O prompt para analisar o sentimento
        texto: str - O texto a ser analisado
    Returns:
        str - O sentimento do texto
    """

    logging.info(f"Analisando sentimento com Gemini: {texto}")
    logging.info("-" * 50)
    try:
        inicio_ms = time.perf_counter() * 1000
        config = types.GenerateContentConfig(
            temperature=0.3,
            # max_output_tokens=100,
            # top_p=0.1,
            # top_k=100,
        )
        response = llm_gemini.models.generate_content(
            model="gemini-2.5-flash",
            contents=[prompt],
            config=config
        )

        fim_ms = time.perf_counter() * 1000
        sentimento_texto = response.text.strip().lower()
        tempo_resposta_ms = fim_ms - inicio_ms
        tokens = response.usage_metadata.prompt_token_count

        if not sentimento_texto:
            raise Exception(
                "Não foi possível encontrar um sentimento válido, verifique a API.")

        return sentimento_texto, tempo_resposta_ms,  tokens
    except Exception as e:
        logging.error(f"Erro ao analisar sentimento com Gemini: {e}")
        logging.error("=" * 50)
        return None


# Função para efetuar a análise de sentimentos
def efetuar_analise_sentimentos(reviews: list):
    """
    Efetua a análise de sentimentos com Groq e Gemini.    
    Args:
        reviews: list - Lista de reviews a serem analisadas        
    Returns:
        list - Lista de resultados da análise de sentimentos
    """

    logging.info(
        f"Efetuando análise de sentimentos com {len(reviews)} reviews")
    resultados_groq = []
    resultados_gemini = []

    for review in reviews:
        prompt_analise_sentimento = f"""
        Analise o sentimento do seguinte texto: {review}
        Retorne APENAS se o sentimento foi: Positivo, Negativo ou Neutro.
        """

        resultado_groq, tempo_resposta_ms_groq, tokens_groq = analisar_sentimento_groq(
            prompt_analise_sentimento, review)
        resultados_groq.append({
            "review": review.strip(),
            "sentimento": resultado_groq,
            "tempo_resposta_ms": tempo_resposta_ms_groq,
            "tokens": tokens_groq,
        })

        resultado_gemini, tempo_resposta_ms_gemini, tokens_gemini = analisar_sentimento_gemini(
            prompt_analise_sentimento, review)
        resultados_gemini.append({
            "review": review.strip(),
            "sentimento": resultado_gemini,
            "tempo_resposta_ms": tempo_resposta_ms_gemini,
            "tokens": tokens_gemini,
        })

    return resultados_groq, resultados_gemini


# Função para ler as reviews
def ler_reviews() -> list:
    """
    Lê as reviews de um arquivo.    
    Args:
        arquivo: str - O nome do arquivo de reviews        
    Returns:
        list - Lista de reviews
    """

    arquivo = "reviews/reviews.txt"
    logging.info(f"Lendo reviews do arquivo: {arquivo}")
    try:
        diretorio_script = os.path.dirname(os.path.abspath(__file__))
        caminho_completo = os.path.join(diretorio_script, arquivo)

        with open(caminho_completo, "r", encoding="utf-8") as arquivo:
            reviews = arquivo.readlines()
            return reviews
    except Exception as e:
        logging.error(f"Erro ao ler reviews do arquivo: {e}")
        logging.error("=" * 50)
        return None


# Função para salvar os resultados da comparação
def salvar_resultados_comparacao(resultados: str) -> None:
    """
    Salva os resultados da comparação em arquivo markdown.    
    Args:
        resultados: String com o conteúdo markdown a ser salvo
    Returns:
        None
    """
    try:
        diretorio_script = os.path.dirname(os.path.abspath(__file__))

        nome_pasta = "resultado_comparacao"
        nome_arquivo = "comparacao_llms.md"

        caminho_pasta = os.path.join(diretorio_script, nome_pasta)

        if not os.path.exists(caminho_pasta):
            os.makedirs(caminho_pasta, exist_ok=True)
            logging.info(f"✅ Diretório criado: {caminho_pasta}")

        caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)

        try:
            if os.path.exists(caminho_arquivo):
                with open(caminho_arquivo, "r", encoding="utf-8") as f:
                    # Tenta ler 1 caractere para verificar se está bloqueado
                    f.read(1)
        except PermissionError:
            logging.error(
                f"⚠️ Arquivo está aberto ou bloqueado: {caminho_arquivo}")
            logging.error("   Feche o arquivo no editor e tente novamente.")
            return

        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            f.write(resultados)

        logging.info(f"✅ Arquivo salvo com sucesso em: {caminho_arquivo}")

    except PermissionError as e:
        logging.error(f"❌ Erro de permissão: {e}")
        logging.error("   Possíveis causas:")
        logging.error(
            "   1. Arquivo está aberto em outro programa (VS Code, Notepad, etc.)")
        logging.error("   2. Sem permissão de escrita na pasta")
        logging.error("   3. Antivírus bloqueando a operação")
        logging.error(f"   Tente fechar o arquivo: {caminho_arquivo}")
    except Exception as e:
        logging.error(f"❌ Erro ao salvar resultados: {e}")
        logging.error("=" * 50)


# Função para comparar as reviews
def comparar_reviews_llm(reviews: list) -> dict:
    """
    Compara as reviews com Groq e Gemini.    
    Args:
        reviews: list - Lista de reviews a serem comparadas        
    Returns:
        dict - Dicionário com os resultados da comparação
    """

    logging.info("-" * 50)
    logging.info("Comparando reviews")
    logging.info("=" * 50)
    
    try:
        resultados_groq, resultados_gemini = efetuar_analise_sentimentos(
            reviews)

        comparacoes = []
        total_concordantes = 0
        tempo_medio_groq = 0
        tempo_medio_gemini = 0

        for i in range(len(resultados_groq)):
            sentimento_groq = resultados_groq[i]['sentimento']
            sentimento_gemini = resultados_gemini[i]['sentimento']

            concordancia = sentimento_groq == sentimento_gemini
            if concordancia:
                total_concordantes += 1

            tempo_groq = resultados_groq[i]['tempo_resposta_ms']
            tempo_gemini = resultados_gemini[i]['tempo_resposta_ms']
            tokens_groq = resultados_groq[i]['tokens']
            tokens_gemini = resultados_gemini[i]['tokens']

            tempo_medio_groq += tempo_groq
            tempo_medio_gemini += tempo_gemini

            comparacoes.append({
                "review": resultados_groq[i]['review'],
                "sentimento_groq": sentimento_groq,
                "sentimento_gemini": sentimento_gemini,
                "concordancia": concordancia,
                "tempo_resposta_ms_groq": tempo_groq,
                "tempo_resposta_ms_gemini": tempo_gemini,
                "tokens_groq": tokens_groq,
                "tokens_gemini": tokens_gemini,
            })

        total_reviews = len(resultados_groq)
        percentual_concordancia = (
            total_concordantes / total_reviews) * 100 if total_reviews > 0 else 0

        tempo_medio_groq = tempo_medio_groq / total_reviews if total_reviews > 0 else 0
        tempo_medio_gemini = tempo_medio_gemini / \
            total_reviews if total_reviews > 0 else 0

        tabela = "# Comparação de Análise de Sentimentos\n\n"
        tabela += f"**Data:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        tabela += "| # | Review | Sentimento Groq | Sentimento Gemini | Concordância |    Groq (ms)    |    Gemini (ms)    |    Tokens gastos Groq    |    Tokens gastos Gemini    |\n"
        tabela += "|---|--------|-----------------|-------------------|--------------|-----------------|-------------------|--------------------------|----------------------------|\n"

        for i, comp in enumerate(comparacoes, start=1):
            review = comp['review']
            if len(review) > 50:
                review = review[:47] + "..."

            concordancia = "✅ SIM" if comp['concordancia'] else "❌ NÃO"

            linha = f"| {i} | {review} | {comp['sentimento_groq']} | {comp['sentimento_gemini']} | {concordancia} | {comp['tempo_resposta_ms_groq']:.0f} | {comp['tempo_resposta_ms_gemini']:.0f} |   {comp['tokens_groq']}   |   {comp['tokens_gemini']}   |\n"
            tabela += linha

        tabela += "\n## 📈 Estatísticas\n\n"
        tabela += f"- **Total de Reviews:** {total_reviews}\n"
        tabela += f"- **Concordâncias:** {total_concordantes}/{total_reviews}\n"
        tabela += f"- **Percentual de Concordância:** {percentual_concordancia:.1f}%\n"
        tabela += f"- **LLM Mais Rápido:** {'Groq' if tempo_medio_groq < tempo_medio_gemini else 'Gemini'}\n"
        tabela += f"- **Tempo Médio Groq:** {tempo_medio_groq:.0f}ms\n"
        tabela += f"- **Tempo Médio Gemini:** {tempo_medio_gemini:.0f}ms\n"

        return tabela
    except Exception as e:
        logging.error(f"Erro ao comparar reviews: {e}")
        logging.error("=" * 50)
        return None


if __name__ == "__main__":
    reviews = ler_reviews()

    comparacao = comparar_reviews_llm(reviews)
    logging.info(comparacao)
    if comparacao:
        salvar_resultados_comparacao(comparacao)
    else:
        logging.error("Não foi possível comparar reviews")
        logging.error("=" * 50)
