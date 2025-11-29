"""
Exemplo de código do Dia 4 com Type Hints e Docstrings
=======================================================

Este arquivo mostra como aplicar type hints e docstrings
no resumidor de PDFs.
"""

from typing import Optional, Tuple
from groq import Groq
from google.genai import types
from google import genai
from dotenv import load_dotenv
import os
import pdfplumber

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY não encontrada no .env")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY não encontrada no .env")

llm_gemini = genai.Client(api_key=GEMINI_API_KEY)
llm_groq = Groq(api_key=GROQ_API_KEY)


def extrair_texto_pdf(caminho_pdf: str) -> Optional[str]:
    """
    Extrai texto de um arquivo PDF.
    
    Args:
        caminho_pdf: Caminho completo ou relativo para o arquivo PDF
    
    Returns:
        String com todo o texto extraído do PDF, ou None em caso de erro
    
    Raises:
        FileNotFoundError: Se o arquivo PDF não existir
        PermissionError: Se não tiver permissão para ler o arquivo
        Exception: Se o PDF estiver corrompido ou protegido
    
    Example:
        >>> texto = extrair_texto_pdf("documento.pdf")
        >>> if texto:
        ...     print(f"Texto extraído: {len(texto)} caracteres")
    """
    try:
        with pdfplumber.open(caminho_pdf) as pdf_file:
            texto_completo = ""
            
            for pagina in pdf_file.pages:
                texto_pagina = pagina.extract_text()
                if texto_pagina:
                    texto_completo += texto_pagina + "\n"
            
            return texto_completo.strip()
            
    except FileNotFoundError:
        print(f"❌ Arquivo não encontrado: {caminho_pdf}")
        return None
    except PermissionError:
        print(f"❌ Sem permissão para ler o arquivo: {caminho_pdf}")
        return None
    except Exception as e:
        print(f"❌ Erro ao extrair texto do PDF: {e}")
        return None


def resumir_com_groq(texto: str, tamanho: str = "médio") -> Optional[Tuple[str, float, int]]:
    """
    Gera resumo de um texto usando Groq API.
    
    Args:
        texto: Texto a ser resumido
        tamanho: Tamanho do resumo desejado ("curto", "médio", "longo")
                 Padrão: "médio"
    
    Returns:
        Tupla com (resumo, tempo_ms, tokens) ou None em caso de erro
        - resumo: Texto resumido
        - tempo_ms: Tempo de resposta em milissegundos
        - tokens: Número de tokens utilizados
    
    Raises:
        ValueError: Se o texto estiver vazio
        Exception: Se houver erro na API do Groq
    
    Example:
        >>> resultado = resumir_com_groq("Texto muito longo...", "curto")
        >>> if resultado:
        ...     resumo, tempo, tokens = resultado
        ...     print(f"Resumo: {resumo}")
    """
    if not texto or not texto.strip():
        raise ValueError("Texto não pode estar vazio")
    
    # Definir max_tokens baseado no tamanho
    tamanhos = {
        "curto": 100,
        "médio": 200,
        "longo": 400
    }
    max_tokens = tamanhos.get(tamanho.lower(), 200)
    
    prompt = f"""
    Resuma o seguinte texto de forma clara e concisa.
    O resumo deve:
    - Capturar os pontos principais
    - Manter informações importantes
    - Ser objetivo e direto
    - Tamanho: {tamanho}
    
    Texto:
    {texto[:3000]}  # Limitar para não exceder tokens
    """
    
    try:
        import time
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
            max_tokens=max_tokens
        )
        
        fim_ms = time.perf_counter() * 1000
        resumo = response.choices[0].message.content.strip()
        tempo_ms = fim_ms - inicio_ms
        tokens = response.usage.total_tokens
        
        return resumo, tempo_ms, tokens
        
    except Exception as e:
        print(f"❌ Erro ao gerar resumo com Groq: {e}")
        return None


def resumir_com_gemini(texto: str, tamanho: str = "médio") -> Optional[Tuple[str, float, int]]:
    """
    Gera resumo de um texto usando Gemini API.
    
    Args:
        texto: Texto a ser resumido
        tamanho: Tamanho do resumo desejado ("curto", "médio", "longo")
                 Padrão: "médio"
    
    Returns:
        Tupla com (resumo, tempo_ms, tokens) ou None em caso de erro
        - resumo: Texto resumido
        - tempo_ms: Tempo de resposta em milissegundos
        - tokens: Número de tokens utilizados
    
    Raises:
        ValueError: Se o texto estiver vazio
        Exception: Se houver erro na API do Gemini
    
    Example:
        >>> resultado = resumir_com_gemini("Texto muito longo...", "médio")
        >>> if resultado:
        ...     resumo, tempo, tokens = resultado
        ...     print(f"Resumo: {resumo}")
    """
    if not texto or not texto.strip():
        raise ValueError("Texto não pode estar vazio")
    
    prompt = f"""
    Resuma o seguinte texto de forma clara e concisa.
    O resumo deve:
    - Capturar os pontos principais
    - Manter informações importantes
    - Ser objetivo e direto
    - Tamanho: {tamanho}
    
    Texto:
    {texto[:3000]}
    """
    
    try:
        import time
        inicio_ms = time.perf_counter() * 1000
        
        config = types.GenerateContentConfig(
            temperature=0.3,
        )
        
        response = llm_gemini.models.generate_content(
            model="gemini-2.5-flash",
            contents=[prompt],
            config=config
        )
        
        fim_ms = time.perf_counter() * 1000
        resumo = response.text.strip()
        tempo_ms = fim_ms - inicio_ms
        tokens = response.usage_metadata.prompt_token_count
        
        return resumo, tempo_ms, tokens
        
    except Exception as e:
        print(f"❌ Erro ao gerar resumo com Gemini: {e}")
        return None


def resumir_pdf(caminho_pdf: str, llm: str = "groq", tamanho: str = "médio") -> Optional[dict]:
    """
    Extrai texto de um PDF e gera resumo usando o LLM especificado.
    
    Args:
        caminho_pdf: Caminho para o arquivo PDF
        llm: LLM a ser usado ("groq" ou "gemini"). Padrão: "groq"
        tamanho: Tamanho do resumo ("curto", "médio", "longo"). Padrão: "médio"
    
    Returns:
        Dicionário com informações do resumo ou None em caso de erro:
        {
            "texto_original": str,
            "resumo": str,
            "llm_usado": str,
            "tempo_ms": float,
            "tokens": int,
            "tamanho_original": int,  # caracteres
            "tamanho_resumo": int     # caracteres
        }
    
    Raises:
        ValueError: Se o LLM especificado não for suportado
        FileNotFoundError: Se o PDF não existir
    
    Example:
        >>> resultado = resumir_pdf("documento.pdf", "groq", "curto")
        >>> if resultado:
        ...     print(f"Resumo: {resultado['resumo']}")
        ...     print(f"Tempo: {resultado['tempo_ms']:.0f}ms")
    """
    # Extrair texto do PDF
    texto = extrair_texto_pdf(caminho_pdf)
    if not texto:
        return None
    
    # Gerar resumo com LLM escolhido
    if llm.lower() == "groq":
        resultado = resumir_com_groq(texto, tamanho)
        llm_usado = "Groq (llama-3.3-70b-versatile)"
    elif llm.lower() == "gemini":
        resultado = resumir_com_gemini(texto, tamanho)
        llm_usado = "Gemini (gemini-2.5-flash)"
    else:
        raise ValueError(f"LLM '{llm}' não suportado. Use 'groq' ou 'gemini'")
    
    if not resultado:
        return None
    
    resumo, tempo_ms, tokens = resultado
    
    return {
        "texto_original": texto,
        "resumo": resumo,
        "llm_usado": llm_usado,
        "tempo_ms": tempo_ms,
        "tokens": tokens,
        "tamanho_original": len(texto),
        "tamanho_resumo": len(resumo)
    }


def salvar_resumo(caminho_pdf: str, resultado: dict, pasta_saida: str = "resumos") -> bool:
    """
    Salva o resumo gerado em arquivo markdown.
    
    Args:
        caminho_pdf: Caminho original do PDF
        resultado: Dicionário retornado por resumir_pdf()
        pasta_saida: Nome da pasta onde salvar (padrão: "resumos")
    
    Returns:
        True se salvou com sucesso, False caso contrário
    
    Raises:
        PermissionError: Se não tiver permissão para escrever
    
    Example:
        >>> resultado = resumir_pdf("doc.pdf")
        >>> if resultado:
        ...     salvar_resumo("doc.pdf", resultado)
    """
    if not resultado:
        print("❌ Nenhum resultado para salvar")
        return False
    
    try:
        # Criar pasta se não existir
        if not os.path.exists(pasta_saida):
            os.makedirs(pasta_saida)
        
        # Nome do arquivo baseado no PDF original
        nome_base = os.path.splitext(os.path.basename(caminho_pdf))[0]
        caminho_arquivo = os.path.join(pasta_saida, f"resumo_{nome_base}.md")
        
        # Criar conteúdo markdown
        from datetime import datetime
        conteudo = f"""# Resumo: {nome_base}

**Data:** {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
**LLM usado:** {resultado['llm_usado']}
**Tamanho original:** {resultado['tamanho_original']} caracteres
**Tamanho resumo:** {resultado['tamanho_resumo']} caracteres
**Tempo de processamento:** {resultado['tempo_ms']:.0f}ms
**Tokens utilizados:** {resultado['tokens']}

---

## Resumo

{resultado['resumo']}

---

## Metadados

- PDF original: `{caminho_pdf}`
- Redução: {((1 - resultado['tamanho_resumo']/resultado['tamanho_original']) * 100):.1f}%
"""
        
        # Salvar arquivo
        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            f.write(conteudo)
        
        print(f"✅ Resumo salvo em: {caminho_arquivo}")
        return True
        
    except PermissionError:
        print(f"❌ Sem permissão para escrever em: {pasta_saida}")
        return False
    except Exception as e:
        print(f"❌ Erro ao salvar resumo: {e}")
        return False


if __name__ == "__main__":
    # Exemplo de uso
    caminho = "pdfs_teste/exemplo.pdf"
    
    # Resumir com Groq
    resultado = resumir_pdf(caminho, "groq", "médio")
    if resultado:
        print(f"Resumo gerado em {resultado['tempo_ms']:.0f}ms")
        salvar_resumo(caminho, resultado)

