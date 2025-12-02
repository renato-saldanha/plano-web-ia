import datetime
import logging
import time
import os
import pdfplumber
from pdfminer.pdfparser import PDFSyntaxError

from Semanas.Semana1.Dia4.util.config import criar_llm_response
from Semanas.Semana1.Dia4.util.util import criar_diretorio, salvar_arquivo

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S',
)


# Função para extrair texto de um PDF
def extrair_texto_pdf(caminho_pdf: str) -> str:
    """
    Extrair o texto de um PDF.

    Args:
        caminho_pdf: str - O caminho do arquivo PDF

    Returns:
        str - O texto extraído do PDF
    """
    logging.info(f"Extraindo texto do PDF: {caminho_pdf}")
    try:
        caminho_completo = os.path.join(os.path.dirname(__file__), caminho_pdf)
        pdf_file = pdfplumber.open(caminho_completo)

        chunks = []
        for page in pdf_file.pages:
            chunks.append(page.extract_text())

        return "\n".join(chunks)
    except PDFSyntaxError as e:
        logging.error(
            f"❌ PDF corrompido ou inválido! \n Caminho do PDF: {caminho_pdf}")
    except PermissionError as e:
        logging.error(
            f"❌ Sem permissão para ler o arquivo \n Caminho do PDF: {caminho_pdf}")
    except Exception as e:
        logging.error(f"❌ Erro ao extrair texto do PDF: {e}")


# Função para resumir texto com Groq
def resumir_com_groq(texto: str) -> str:
    """
    Resumir o texto do PDF usando o modelo de Groq.

    Args:
        texto: str - O texto do PDF

    Returns:
        str - O resumo do texto
    """
    logging.info(f"Resumindo texto com Groq")
    try:
        prompt = f"""
        Resuma o seguinte texto:
        {texto}
        """
        response = criar_llm_response(prompt, "groq")

        if not response:
            raise Exception(
                "Não foi possível encontrar um resumo válido, verifique a API.")

        resumo = response.choices[0].message.content.strip()

        return resumo
    except Exception as e:
        logging.error(f"❌ Erro ao resumir texto com Groq: {e}")
        return None


# Função para resumir texto com Gemini
def resumir_com_gemini(texto: str) -> str:
    """
    Resumir o texto do PDF usando o modelo de Gemini.

    Args:
        texto: str - O texto do PDF

    Returns:
        str - O resumo do texto
    """
    logging.info(f"Resumindo texto com Gemini")
    try:
        prompt = f"""
        Resuma o seguinte texto em 100 tokens:
        {texto}
        """

        response = criar_llm_response(prompt, "gemini")

        if not response:
            raise Exception(
                "Não foi possível encontrar um resumo válido, verifique a API.")

        resumo = response.text.strip()

        return resumo
    except Exception as e:
        logging.error(f"❌ Erro ao resumir texto com Gemini: {e}")
        return None


# Função para resumir PDF
def resumir_pdf(caminho_arquivo: str, llm: str) -> str:
    """
    Resumir o texto do PDF usando o modelo de LLM especif icado.

    Args:
        caminho_arquivo: str - O caminho do arquivo PDF
        llm: str - O modelo de LLM a ser usado

    Returns:
        str - O resumo do texto
    """

    try:    
        texto = extrair_texto_pdf(caminho_arquivo)

        if not texto:
            raise Exception("Não foi possível extrair o texto do PDF.")

        match llm:
            case 'groq':
                logging.info(f"Resumindo texto com Groq")
                resumo = resumir_com_groq(texto)
            case 'gemini':
                logging.info(f"Resumindo texto com Gemini")
                resumo = resumir_com_gemini(texto)
            case _:
                raise ValueError("Modelo de LLM inválido.")

        salvar_resumo_markdown(resumo, texto, llm, caminho_arquivo)
        return resumo
    except Exception as e:
        logging.error(f"❌ Erro ao resumir PDF: {e}")
        return None


# Função para comparar resumos
def comparar_resumos(caminho_arquivo: str) -> dict:
    """
    Compara resultados ussando métricas objetivas.

    Args:
        caminho_arquivo: str - O caminho do arquivo PDF

    Returns:
        dict - O dicionário com os resultados da comparação
    """

    logging.info(f"Iniciando comparação de resumos")
    logging.info("=" * 60 + "\n")
    try:
        resumo_groq = resumir_pdf(caminho_arquivo, "groq")
        resumo_gemini = resumir_pdf(caminho_arquivo, "gemini")

        logging.info("=" * 60 + "\n")
        logging.info(f"Resumo Groq: {resumo_groq}")
        logging.info("=" * 60 + "\n")
        logging.info(f"Resumo Gemini: {resumo_gemini}")
        logging.info("=" * 60 + "\n")

        comparacao = {
            "groq": {
                "resumo": resumo_groq,
                "comprimento": len(resumo_groq),
                "palavras": len(resumo_groq.split()),
                "sentencas": resumo_groq.count(".") + resumo_groq.count("!") + resumo_groq.count("?"),
            },
            "gemini": {
                "resumo": resumo_gemini,
                "comprimento": len(resumo_gemini),
                "palavras": len(resumo_gemini.split()),
                "sentencas": resumo_gemini.count(".") + resumo_gemini.count("!") + resumo_gemini.count("?"),
            },
        }

        # Comparações
        comparacao["diferenca_palavras"] = abs(
            comparacao["groq"]["palavras"] - comparacao["gemini"]["palavras"])
        comparacao["mais_detalhado"] = "groq" if comparacao["groq"]["comprimento"] > comparacao["gemini"]["comprimento"] else "gemini"

        return comparacao
    except Exception as e:
        logging.error(f"❌ Erro ao comparar resumos: {e}")


# Função para salvar resultados em markdown
def salvar_resultado_markdown(comparacao: dict) -> None:
    """
    Salva os resultados da comparação em markdown.

    Args:
        comparacao: dict - O dicionário com os resultados da comparação
    """

    logging.info(f"Salvando resultados em markdown")
    try:
        diretorio_script = os.path.dirname(os.path.abspath(__file__))
        nome_pasta = "resultado_comparacao"
        nome_arquivo = f"comparacao_resumos{time.time()}.md"
        caminho_pasta = os.path.join(diretorio_script, nome_pasta)

        criar_diretorio(caminho_pasta)

        caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)
        
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

        salvar_arquivo(caminho_arquivo, texto_markdown)

        logging.info(f"✅ Resultado salvo com sucesso em: {caminho_arquivo}")
    except PermissionError as e:
        logging.error(
            f"❌ Sem permissão para ler o arquivo \n Caminho do arquivo: {caminho_arquivo}")
    except Exception as e:
        logging.error(f"❌ Erro ao salvar resultados em markdown: {e}")


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

    logging.info(f"Salvando resumo em markdown")
    try:
        diretorio_script = os.path.dirname(os.path.abspath(__file__))
        nome_pasta = "resumos"
        nome_arquivo = f"resumo{time.time()}.md"
        caminho_pasta = os.path.join(diretorio_script, nome_pasta)

        criar_diretorio(caminho_pasta)

        nome_arquivo = os.path.splitext(os.path.basename(caminho_pdf))[0]
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        nome_arquivo = f"resumo_{nome_arquivo}_{timestamp}.md"
        caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)

        tamanho_original = len(texto_original)
        tamanho_resumo = len(resumo)
        palavras_original = len(texto_original.split())
        palavras_resumo = len(resumo.split())
        taxa_compressao = (1 - tamanho_resumo / tamanho_original) * \
            100 if tamanho_original > 0 else 0

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

        salvar_arquivo(caminho_arquivo, texto_markdown)

        logging.info(
            f"✅ Resumo {llm_usado.upper()} salvo com sucesso em: {caminho_arquivo}")   
    except Exception as e:
        logging.error(f"❌ Erro ao salvar resumo em markdown: {e}")
        return


if __name__ == "__main__":
    diretorio_script = os.path.dirname(os.path.abspath(__file__))
    caminho_pasta_pdf = os.path.join(diretorio_script, "pdfs/")

    for arquivo in os.listdir(caminho_pasta_pdf):
        caminho = os.path.join(caminho_pasta_pdf, arquivo)

        comparacao = comparar_resumos(caminho)
        salvar_resultado_markdown(comparacao)