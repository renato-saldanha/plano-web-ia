"""
Exemplo Prático: Dividir Texto em Chunks
=========================================

Este arquivo mostra como dividir texto em chunks sem LangChain,
aplicado ao resumidor de PDFs.
"""

from typing import List, Optional
import re


def dividir_texto_em_chunks(texto: str, tamanho_chunk: int = 3000, overlap: int = 200) -> List[str]:
    """
    Divide texto em chunks inteligentes sem cortar palavras no meio.
    
    Args:
        texto: Texto a ser dividido
        tamanho_chunk: Tamanho máximo de cada chunk em caracteres
        overlap: Sobreposição entre chunks (para manter contexto)
    
    Returns:
        Lista de strings (chunks)
    
    Example:
        >>> texto = "Texto muito longo..." * 100
        >>> chunks = dividir_texto_em_chunks(texto, 1000)
        >>> print(f"Total de chunks: {len(chunks)}")
    """
    # Se texto cabe em um chunk, retorna inteiro
    if len(texto) <= tamanho_chunk:
        return [texto]
    
    chunks = []
    inicio = 0
    
    while inicio < len(texto):
        fim = inicio + tamanho_chunk
        
        # Se não é o último chunk, tentar terminar em lugar inteligente
        if fim < len(texto):
            # 1. Tentar terminar em fim de sentença (. ! ?)
            padrao_sentenca = r'[.!?]\s+'
            matches = list(re.finditer(padrao_sentenca, texto[inicio:fim]))
            
            if matches:
                # Usar último fim de sentença encontrado
                fim = inicio + matches[-1].end()
            else:
                # 2. Se não encontrou sentença, terminar em espaço
                ultimo_espaco = texto.rfind(" ", inicio, fim)
                if ultimo_espaco > inicio:
                    fim = ultimo_espaco
        
        # Extrair chunk
        chunk = texto[inicio:fim].strip()
        
        if chunk:
            chunks.append(chunk)
        
        # Próximo chunk começa com overlap (sobreposição)
        inicio = max(fim - overlap, inicio + 1)
    
    return chunks


def dividir_por_palavras(texto: str, tamanho_chunk: int = 3000) -> List[str]:
    """
    Versão mais simples: divide por palavras sem cortar no meio.
    
    Args:
        texto: Texto a ser dividido
        tamanho_chunk: Tamanho aproximado de cada chunk
    
    Returns:
        Lista de chunks
    """
    if len(texto) <= tamanho_chunk:
        return [texto]
    
    chunks = []
    palavras = texto.split()
    chunk_atual = ""
    
    for palavra in palavras:
        # Verificar se adicionar palavra ultrapassa limite
        tamanho_com_palavra = len(chunk_atual) + len(palavra) + 1  # +1 para espaço
        
        if tamanho_com_palavra <= tamanho_chunk:
            # Adiciona palavra ao chunk atual
            if chunk_atual:
                chunk_atual += " " + palavra
            else:
                chunk_atual = palavra
        else:
            # Chunk cheio, salvar e começar novo
            if chunk_atual:
                chunks.append(chunk_atual)
            chunk_atual = palavra
    
    # Adicionar último chunk
    if chunk_atual:
        chunks.append(chunk_atual)
    
    return chunks


# ============================================
# EXEMPLO DE USO NO SEU CÓDIGO
# ============================================

def resumir_texto_com_chunks(texto: str, resumir_funcao, tamanho_chunk: int = 3000) -> Optional[str]:
    """
    Resumir texto dividindo em chunks se necessário.
    
    Args:
        texto: Texto a ser resumido
        resumir_funcao: Função que recebe texto e retorna resumo
        tamanho_chunk: Tamanho máximo de cada chunk
    
    Returns:
        Resumo completo do texto
    """
    # Verificar se precisa dividir
    if len(texto) <= tamanho_chunk:
        # Texto cabe em um chunk, processar direto
        print("✅ Texto cabe em um chunk, processando direto...")
        return resumir_funcao(texto)
    
    # Texto muito grande, dividir
    print(f"📦 Texto muito grande ({len(texto)} chars). Dividindo em chunks...")
    chunks = dividir_texto_em_chunks(texto, tamanho_chunk)
    print(f"✅ Dividido em {len(chunks)} chunks")
    
    # Processar cada chunk
    resumos_chunks = []
    
    for i, chunk in enumerate(chunks, 1):
        print(f"📄 Processando chunk {i}/{len(chunks)} ({len(chunk)} chars)...")
        resumo_chunk = resumir_funcao(chunk)
        
        if resumo_chunk:
            resumos_chunks.append(resumo_chunk)
        else:
            print(f"⚠️  Erro ao processar chunk {i}")
    
    if not resumos_chunks:
        print("❌ Nenhum chunk foi processado com sucesso")
        return None
    
    # Se temos apenas um resumo, retornar
    if len(resumos_chunks) == 1:
        return resumos_chunks[0]
    
    # Se temos múltiplos resumos, combinar e resumir novamente
    print(f"🔄 Combinando {len(resumos_chunks)} resumos...")
    texto_combinado = "\n\n".join(resumos_chunks)
    
    # Se texto combinado ainda é muito grande, dividir novamente
    if len(texto_combinado) > tamanho_chunk:
        print("📦 Texto combinado ainda é grande, dividindo novamente...")
        return resumir_texto_com_chunks(texto_combinado, resumir_funcao, tamanho_chunk)
    
    # Resumir texto combinado
    print("📝 Gerando resumo final...")
    return resumir_funcao(texto_combinado)


# ============================================
# EXEMPLO DE TESTE
# ============================================

if __name__ == "__main__":
    # Simular texto muito longo
    texto_longo = """
    Este é um parágrafo de exemplo. 
    Este é outro parágrafo de exemplo.
    Este é mais um parágrafo de exemplo.
    """ * 500  # Repetir 500 vezes para criar texto longo
    
    print(f"Texto original: {len(texto_longo)} caracteres\n")
    
    # Testar divisão
    chunks = dividir_texto_em_chunks(texto_longo, 1000)
    
    print(f"Total de chunks: {len(chunks)}\n")
    
    for i, chunk in enumerate(chunks, 1):
        print(f"Chunk {i}: {len(chunk)} caracteres")
        print(f"  Preview: {chunk[:50]}...")
        print()
    
    # Testar versão simples
    print("\n" + "="*60)
    print("Versão Simples (por palavras):")
    print("="*60 + "\n")
    
    chunks_simples = dividir_por_palavras(texto_longo, 1000)
    
    for i, chunk in enumerate(chunks_simples, 1):
        print(f"Chunk {i}: {len(chunk)} caracteres")

