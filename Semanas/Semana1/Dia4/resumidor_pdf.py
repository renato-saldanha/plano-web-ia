import datetime
import time
from groq import Groq
from google.genai import types
from google import genai
from openai import OpenAI
from dotenv import load_dotenv
import os
import pdfplumber
from pdfminer.pdfparser import PDFSyntaxError

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

# Função para extrair texto de um PDF
def extrair_texto_pdf(caminho_pdf: str) -> str:
    print(f"Extraindo texto do PDF: {caminho_pdf}")
    try:
        caminho_completo = os.path.join(os.path.dirname(__file__), caminho_pdf)
        pdf_file = pdfplumber.open(caminho_completo)

        pdf_text = ""

        for page in pdf_file.pages:
            pdf_text += page.extract_text() + '\n'      
        
        return pdf_text[:900]
    except PDFSyntaxError as e:
        print(f"PDF corrompido ou inválido! \n Caminho do PDF: {caminho_pdf}")    
    except PermissionError as e:
        print(f"Sem permissão para ler o arquivo \n Caminho do PDF: {caminho_pdf}")
    except Exception as e:
        print(f"Erro ao extrair texto do PDF: {e}")    

# Função para resumir texto com Groq
def resumir_com_groq(texto: str) -> str:    
    print(f"Resumindo texto com Groq")
    try:
        prompt = f"""
        Resuma o seguinte texto em 100 tokens:
        {texto}
        """
        response = llm_groq.chat.completions.create(
            model = "llama-3.3-70b-versatile",
            messages = [
                {
                    "role" : "user",
                    "content" : prompt,
                }
            ],
            temperature=0.3,
            max_tokens=100,
        )

        if not response:
            raise Exception("Não foi possível encontrar um resumo válido, verifique a API.")

        resumo = response.choices[0].message.content.strip()

        return resumo
    except Exception as e:
        print(f"Erro ao resumir texto com Groq: {e}")
        return None

# Função para resumir texto com Gemini
def resumir_com_gemini(texto: str) -> str:    
    print(f"Resumindo texto com Gemini")
    try:
        prompt = f"""
        Resuma o seguinte texto em 100 tokens:
        {texto}
        """

        config = types.GenerateContentConfig(
            temperature = 0.3,
        )

        response = llm_gemini.models.generate_content(
            model = "gemini-2.5-flash",
            contents = [prompt],
            config = config
        )

        if not response:
            raise Exception("Não foi possível encontrar um resumo válido, verifique a API.")

        resumo = response.text.strip()

        return resumo
    except Exception as e:
        print(f"Erro ao resumir texto com Gemini: {e}")
        return None

# Função para resumir PDF
def resumir_pdf(texto: str, caminho_arquivo: str, llm: str = ["groq", "gemini"]) -> dict:
    try:
        match llm:
            case "groq":
                resumo = resumir_com_groq(texto)
            case "gemini":
                resumo = resumir_com_gemini(texto)
            case _:
                raise ValueError("Modelo de LLM inválido.")

        salvar_resumo_markdown(resumo, texto, llm, caminho_arquivo)
        return resumo
    except Exception as e:
        print(f"Erro ao resumir PDF: {e}")
        return None

# Função para comparar resumos
def comparar_resumos(caminho_arquivo: str) -> dict:   
    print(f"Comparando resumos")
    """
        Compara resultados ussando métricas objetivas.
    """
    try:
        texto = extrair_texto_pdf(caminho_arquivo)

        if not texto:
            raise Exception("Não foi possível extrair o texto do PDF.")

        resumo_groq = resumir_pdf(texto, caminho_arquivo, "groq")
        resumo_gemini = resumir_pdf(texto, caminho_arquivo, "gemini")
        
        print("=" * 60 + "\n")
        print(f"Resumo Groq: {resumo_groq}")
        print("=" * 60 + "\n")    
        print(f"Resumo Gemini: {resumo_gemini}")
        print("=" * 60 + "\n")

        comparacao = {
            "groq" : {
                "resumo" : resumo_groq,
                "comprimento" : len(resumo_groq),
                "palavras" : len(resumo_groq.split()),
                "sentencas" : resumo_groq.count(".") + resumo_groq.count("!") + resumo_groq.count("?"),
            },
            "gemini" : {
                "resumo" : resumo_gemini,
                "comprimento" : len(resumo_gemini),
                "palavras" : len(resumo_gemini.split()),
                "sentencas" : resumo_gemini.count(".") + resumo_gemini.count("!") + resumo_gemini.count("?"),
            },
        }

        #Comparações
        comparacao["diferenca_palavras"] = abs(comparacao["groq"]["palavras"] - comparacao["gemini"]["palavras"])
        comparacao["mais_detalhado"] = "groq" if comparacao["groq"]["comprimento"] > comparacao["gemini"]["comprimento"] else "gemini"

        return comparacao
    except Exception as e:
        print(f"Erro ao comparar resumos: {e}")

# Função para salvar resultados em markdown
def salvar_resultado_markdown(comparacao: dict) -> None:
    print(f"Salvando resultados em markdown")
    try:
        diretorio_script = os.path.dirname(os.path.abspath(__file__))
        nome_pasta = "resultado_comparacao"
        nome_arquivo = f"comparacao_resumos{time.time()}.md"
        caminho_pasta = os.path.join(diretorio_script, nome_pasta)

        if not os.path.exists(caminho_pasta):
            os.makedirs(caminho_pasta, exist_ok=True)
            print(f"✅ Diretório criado: {caminho_pasta}")
        
        caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)

        try:
            if os.path.exists(caminho_arquivo):
                with open(caminho_arquivo, "r", encoding="utf-8") as f:
                    f.read(1)  # Tenta ler 1 caractere para verificar se está bloqueado
        except PermissionError:
            print(f"⚠️ Arquivo está aberto ou bloqueado: {caminho_arquivo}")
            print("   Feche o arquivo no editor e tente novamente.")
            return

        texto_markdown = f"""
        # Resultado da Comparação
        ## Comparacao entre Groq e Gemini
        ### Resumo Groq: {comparacao['groq']['resumo']}\n
        ### Resumo Gemini: {comparacao['gemini']['resumo']}\n
        ### Comprimento: {comparacao['groq']['comprimento']} vs {comparacao['gemini']['comprimento']}
        ### Palavras: {comparacao['groq']['palavras']} vs {comparacao['gemini']['palavras']}
        ### Sentenças: {comparacao['groq']['sentencas']} vs {comparacao['gemini']['sentencas']}
        ### Diferença de palavras: {comparacao['diferenca_palavras']}
        ### Mais detalhado: {comparacao['mais_detalhado']}
        """

        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            f.write(texto_markdown)

        print(f"✅ Arquivo salvo com sucesso em: {caminho_arquivo}")
    except PermissionError as e:
        print(f"Sem permissão para ler o arquivo \n Caminho do arquivo: {caminho_arquivo}")
    except Exception as e:
        print(f"Erro ao salvar resultados em markdown: {e}")

# Função para salvar o resumo em arquivo markdown
def salvar_resumo_markdown(resumo: str, texto_original: str, llm_usado: str, caminho_pdf: str) -> None:
    """
    Salva o resumo em arquivo markdown.

    Args:
        resumo: str - O resumo do texto
        texto_original: str - O texto original
        llm_usado: str - O LLM usado
        caminho_pdf: str - O caminho do PDF 
    """

    print(f"Salvando resumo em markdown")
    try:
        diretorio_script = os.path.dirname(os.path.abspath(__file__))
        nome_pasta = "resumos"
        nome_arquivo = f"resumo{time.time()}.md"
        caminho_pasta = os.path.join(diretorio_script, nome_pasta)

        if not os.path.exists(caminho_pasta):
            os.makedirs(caminho_pasta, exist_ok=True)
            print(f"✅ Diretório criado: {caminho_pasta}")

        nome_arquivo = os.path.splitext(os.path.basename(caminho_pdf))[0]
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        nome_arquivo =f"resumo_{nome_arquivo}_{timestamp}.md"
        caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)

        tamanho_original = len(texto_original)
        tamanho_resumo = len(resumo)
        palavras_original = len(texto_original.split())
        palavras_resumo = len(resumo.split())
        taxa_compressao = (1 - tamanho_resumo / tamanho_original) * 100 if tamanho_original > 0 else 0

        try:
            if os.path.exists(caminho_arquivo):
                with open(caminho_arquivo, "r", encoding="utf-8") as f:
                    f.read(1)  # Tenta ler 1 caractere para verificar se está bloqueado
        except PermissionError:
            print(f"⚠️ Arquivo está aberto ou bloqueado: {caminho_arquivo}")
            print("   Feche o arquivo no editor e tente novamente.")
            return

        texto_markdown = f"""
        # Resumo do PDF
        ## {resumo}
        # Metadados
        - Data: {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
        - LLM usado: {llm_usado}
        - Tamanho original: {tamanho_original} bytes
        - Tamanho resumo: {tamanho_resumo} bytes
        - Palavras original: {palavras_original}
        - Palavras resumo: {palavras_resumo}
        - Taxa de compressão: {taxa_compressao}%
        """

        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            f.write(texto_markdown)

        print(f"✅ Arquivo salvo com sucesso em: {caminho_arquivo}")
    except PermissionError:
        print(f"⚠️ Arquivo está aberto ou bloqueado: {caminho_arquivo}")
        print("   Feche o arquivo no editor e tente novamente.")
        return
    except Exception as e:
        print(f"Erro ao salvar resumo em markdown: {e}")
        return

if __name__ == "__main__":
    diretorio_script = os.path.dirname(os.path.abspath(__file__))
    caminho_pasta_pdf = os.path.join(diretorio_script, "pdfs/")

    for arquivo in os.listdir(caminho_pasta_pdf):
        caminho_arquivo = os.path.join(caminho_pasta_pdf, arquivo)
        
        comparacao = comparar_resumos(caminho_arquivo)
        salvar_resultado_markdown(comparacao)
