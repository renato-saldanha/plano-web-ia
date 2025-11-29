"""
Resumidor de PDF com Chunking - Versão Completa
================================================

Esta versão mostra como integrar chunking no resumidor de PDFs.
"""

from typing import List, Optional
from groq import Groq
from dotenv import load_dotenv
import os
import pdfplumber
import re
from google import genai


load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY não encontrada no .env")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY não encontrada no .env")

llm_groq = Groq(api_key=GROQ_API_KEY)
llm_gemini = genai.Client(api_key=GEMINI_API_KEY)

def dividir_texto_em_chunks(texto: str, tamanho_chunk: int = 3000, overlap: int = 200) -> List[str]:
    """
    Divide texto em chunks inteligentes sem cortar palavras.
    
    Args:
        texto: Texto a ser dividido
        tamanho_chunk: Tamanho máximo de cada chunk
        overlap: Sobreposição entre chunks
    
    Returns:
        Lista de chunks
    """
    if len(texto) <= tamanho_chunk:
        return [texto]
    
    chunks = []
    inicio = 0
    
    while inicio < len(texto):
        fim = inicio + tamanho_chunk
        
        if fim < len(texto):
            # Tentar terminar em fim de sentença
            padrao = r'[.!?]\s+'
            matches = list(re.finditer(padrao, texto[inicio:fim]))
            
            if matches:
                fim = inicio + matches[-1].end()
            else:
                # Terminar em espaço
                ultimo_espaco = texto.rfind(" ", inicio, fim)
                if ultimo_espaco > inicio:
                    fim = ultimo_espaco
        
        chunk = texto[inicio:fim].strip()
        if chunk:
            chunks.append(chunk)
        
        inicio = max(fim - overlap, inicio + 1)
    
    return chunks


def extrair_texto_pdf(caminho_pdf: str) -> Optional[str]:
    """Extrai texto de um PDF."""
    try:
        with pdfplumber.open(caminho_pdf) as pdf:
            texto = ""
            for pagina in pdf.pages:
                texto_pagina = pagina.extract_text()
                if texto_pagina:
                    texto += texto_pagina + "\n"
            return texto.strip() if texto.strip() else None
    except Exception as e:
        print(f"❌ Erro ao extrair PDF: {e}")
        return None


def resumir_chunk(chunk: str) -> Optional[str]:
    """
    Resumir um único chunk de texto.
    
    Args:
        chunk: Texto a ser resumido
    
    Returns:
        Resumo do chunk ou None
    """
    prompt = f"""
    Resuma o seguinte texto de forma clara e concisa em até 100 palavras:
    
    {chunk}
    
    Resumo:
    """
    
    try:
        response = llm_groq.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=150,
        )
        
        resumo = response.choices[0].message.content.strip()
        return resumo if resumo else None
        
    except Exception as e:
        print(f"❌ Erro ao resumir chunk: {e}")
        return None


def resumir_texto_com_chunks(texto: str, tamanho_chunk: int = 3000) -> Optional[str]:
    """
    Resumir texto dividindo em chunks se necessário.
    
    Args:
        texto: Texto a ser resumido
        tamanho_chunk: Tamanho máximo de cada chunk
    
    Returns:
        Resumo completo do texto
    """
    # Verificar se precisa dividir
    if len(texto) <= tamanho_chunk:
        print("✅ Texto cabe em um chunk, processando direto...")
        return resumir_chunk(texto)
    
    # Dividir em chunks
    print(f"📦 Texto muito grande ({len(texto)} chars). Dividindo...")
    chunks = dividir_texto_em_chunks(texto, tamanho_chunk)
    print(f"✅ Dividido em {len(chunks)} chunks\n")
    
    # Processar cada chunk
    resumos_chunks = []
    
    for i, chunk in enumerate(chunks, 1):
        print(f"📄 Chunk {i}/{len(chunks)} ({len(chunk)} chars)...", end=" ")
        resumo = resumir_chunk(chunk)
        
        if resumo:
            resumos_chunks.append(resumo)
            print("✅")
        else:
            print("❌")
    
    if not resumos_chunks:
        print("❌ Nenhum chunk foi processado")
        return None
    
    # Se apenas um resumo, retornar
    if len(resumos_chunks) == 1:
        return resumos_chunks[0]
    
    # Combinar resumos
    print(f"\n🔄 Combinando {len(resumos_chunks)} resumos...")
    texto_combinado = "\n\n".join(resumos_chunks)
    
    # Se ainda é grande, processar recursivamente
    if len(texto_combinado) > tamanho_chunk:
        return resumir_texto_com_chunks(texto_combinado, tamanho_chunk)
    
    # Resumir texto combinado
    print("📝 Gerando resumo final...")
    return resumir_chunk(texto_combinado)


def resumir_pdf(caminho_pdf: str) -> Optional[str]:
    """
    Função principal: extrai texto do PDF e gera resumo.
    
    Args:
        caminho_pdf: Caminho para o arquivo PDF
    
    Returns:
        Resumo do PDF ou None
    """
    print(f"📄 Extraindo texto de: {caminho_pdf}")
    texto = extrair_texto_pdf(caminho_pdf)
    
    if not texto:
        print("❌ Não foi possível extrair texto do PDF")
        return None
    
    print(f"✅ Texto extraído: {len(texto)} caracteres\n")
    
    # Resumir (com chunking automático se necessário)
    resumo = resumir_texto_com_chunks(texto)
    
    return resumo


if __name__ == "__main__":
    # Teste
    caminho = "pdfs_teste/documento.pdf"
    
    resumo = resumir_pdf(caminho)
    
    if resumo:
        print("\n" + "="*60)
        print("RESUMO FINAL:")
        print("="*60)
        print(resumo)
        print("="*60)
    else:
        print("\n❌ Não foi possível gerar resumo")

