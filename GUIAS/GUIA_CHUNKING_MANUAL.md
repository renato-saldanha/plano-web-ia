# 📦 Guia: Dividir Texto em Chunks (Sem LangChain)

## 🎯 Por que dividir em chunks?

- PDFs podem ter milhares de caracteres
- APIs têm limite de tokens (ex: 4000 tokens)
- Processar tudo de uma vez pode falhar
- Chunks permitem processar por partes

---

## ✅ Método 1: Chunking Simples por Caracteres

### Dividir em pedaços de tamanho fixo:

```python
def dividir_em_chunks(texto: str, tamanho_chunk: int = 3000) -> list[str]:
    """
    Divide texto em chunks de tamanho fixo.
    
    Args:
        texto: Texto a ser dividido
        tamanho_chunk: Tamanho de cada chunk em caracteres
    
    Returns:
        Lista de strings (chunks)
    
    Example:
        >>> texto = "Texto muito longo..." * 100
        >>> chunks = dividir_em_chunks(texto, 1000)
        >>> print(f"Total de chunks: {len(chunks)}")
    """
    chunks = []
    
    for i in range(0, len(texto), tamanho_chunk):
        chunk = texto[i:i + tamanho_chunk]
        chunks.append(chunk)
    
    return chunks

# Uso:
texto = "Texto muito longo..." * 1000
chunks = dividir_em_chunks(texto, 3000)

for i, chunk in enumerate(chunks, 1):
    print(f"Chunk {i}: {len(chunk)} caracteres")
```

**Problema:** Pode cortar palavras no meio.

---

## ✅ Método 2: Chunking por Palavras (Recomendado)

### Dividir sem cortar palavras no meio:

```python
def dividir_em_chunks_por_palavras(texto: str, tamanho_chunk: int = 3000) -> list[str]:
    """
    Divide texto em chunks sem cortar palavras no meio.
    
    Args:
        texto: Texto a ser dividido
        tamanho_chunk: Tamanho aproximado de cada chunk em caracteres
    
    Returns:
        Lista de strings (chunks)
    """
    chunks = []
    palavras = texto.split()
    chunk_atual = ""
    
    for palavra in palavras:
        # Verificar se adicionar palavra ultrapassa o limite
        if len(chunk_atual) + len(palavra) + 1 <= tamanho_chunk:
            # Adiciona palavra ao chunk atual
            if chunk_atual:
                chunk_atual += " " + palavra
            else:
                chunk_atual = palavra
        else:
            # Chunk atual está cheio, salvar e começar novo
            if chunk_atual:
                chunks.append(chunk_atual)
            chunk_atual = palavra
    
    # Adicionar último chunk se houver
    if chunk_atual:
        chunks.append(chunk_atual)
    
    return chunks

# Uso:
texto = "Este é um texto muito longo que precisa ser dividido em pedaços menores."
chunks = dividir_em_chunks_por_palavras(texto, 20)

for i, chunk in enumerate(chunks, 1):
    print(f"Chunk {i} ({len(chunk)} chars): {chunk}")
```

**Vantagem:** Não corta palavras no meio.

---

## ✅ Método 3: Chunking com Overlap (Sobreposição)

### Útil para manter contexto entre chunks:

```python
def dividir_em_chunks_com_overlap(texto: str, tamanho_chunk: int = 3000, overlap: int = 200) -> list[str]:
    """
    Divide texto em chunks com sobreposição entre eles.
    
    Args:
        texto: Texto a ser dividido
        tamanho_chunk: Tamanho de cada chunk
        overlap: Número de caracteres de sobreposição entre chunks
    
    Returns:
        Lista de strings (chunks)
    """
    chunks = []
    inicio = 0
    
    while inicio < len(texto):
        fim = inicio + tamanho_chunk
        
        # Se não é o último chunk, tenta terminar em espaço
        if fim < len(texto):
            # Procurar último espaço antes do fim
            ultimo_espaco = texto.rfind(" ", inicio, fim)
            if ultimo_espaco > inicio:
                fim = ultimo_espaco
        
        chunk = texto[inicio:fim]
        chunks.append(chunk.strip())
        
        # Próximo chunk começa com overlap
        inicio = fim - overlap
        if inicio < 0:
            inicio = fim
    
    return chunks

# Uso:
texto = "Texto muito longo..." * 100
chunks = dividir_em_chunks_com_overlap(texto, 1000, 100)

for i, chunk in enumerate(chunks, 1):
    print(f"Chunk {i}: {len(chunk)} caracteres")
```

**Vantagem:** Mantém contexto entre chunks.

---

## ✅ Método 4: Chunking por Sentenças

### Divide respeitando pontuação:

```python
import re

def dividir_em_chunks_por_sentencas(texto: str, tamanho_chunk: int = 3000) -> list[str]:
    """
    Divide texto em chunks respeitando sentenças completas.
    
    Args:
        texto: Texto a ser dividido
        tamanho_chunk: Tamanho aproximado de cada chunk
    
    Returns:
        Lista de strings (chunks)
    """
    # Dividir por pontuação de fim de sentença
    sentencas = re.split(r'([.!?]\s+)', texto)
    
    # Reagrupar sentenças com pontuação
    sentencas_completas = []
    for i in range(0, len(sentencas) - 1, 2):
        if i + 1 < len(sentencas):
            sentencas_completas.append(sentencas[i] + sentencas[i + 1])
        else:
            sentencas_completas.append(sentencas[i])
    
    chunks = []
    chunk_atual = ""
    
    for sentenca in sentencas_completas:
        # Verificar se adicionar sentença ultrapassa limite
        if len(chunk_atual) + len(sentenca) <= tamanho_chunk:
            chunk_atual += sentenca
        else:
            # Chunk cheio, salvar e começar novo
            if chunk_atual:
                chunks.append(chunk_atual.strip())
            chunk_atual = sentenca
    
    # Adicionar último chunk
    if chunk_atual:
        chunks.append(chunk_atual.strip())
    
    return chunks

# Uso:
texto = "Primeira sentença. Segunda sentença! Terceira sentença? Quarta sentença."
chunks = dividir_em_chunks_por_sentencas(texto, 30)

for i, chunk in enumerate(chunks, 1):
    print(f"Chunk {i}: {chunk}")
```

**Vantagem:** Mantém sentenças completas.

---

## ✅ Método 5: Chunking Inteligente (Híbrido)

### Combina múltiplas estratégias:

```python
import re

def dividir_texto_inteligente(texto: str, tamanho_chunk: int = 3000, overlap: int = 200) -> list[str]:
    """
    Divide texto de forma inteligente, respeitando sentenças e palavras.
    
    Args:
        texto: Texto a ser dividido
        tamanho_chunk: Tamanho máximo de cada chunk
        overlap: Sobreposição entre chunks
    
    Returns:
        Lista de strings (chunks)
    """
    # Se texto é menor que o chunk, retorna inteiro
    if len(texto) <= tamanho_chunk:
        return [texto]
    
    chunks = []
    inicio = 0
    
    while inicio < len(texto):
        fim = inicio + tamanho_chunk
        
        # Se não é o último chunk
        if fim < len(texto):
            # Tentar terminar em fim de sentença
            padrao_sentenca = r'[.!?]\s+'
            match = list(re.finditer(padrao_sentenca, texto[inicio:fim]))
            
            if match:
                # Usar último fim de sentença encontrado
                ultimo_match = match[-1]
                fim = inicio + ultimo_match.end()
            else:
                # Se não encontrou sentença, tentar terminar em espaço
                ultimo_espaco = texto.rfind(" ", inicio, fim)
                if ultimo_espaco > inicio:
                    fim = ultimo_espaco
        
        chunk = texto[inicio:fim].strip()
        if chunk:
            chunks.append(chunk)
        
        # Próximo chunk com overlap
        inicio = max(fim - overlap, inicio + 1)
    
    return chunks

# Uso:
texto = "Primeira sentença. Segunda sentença! Terceira sentença? Quarta sentença."
chunks = dividir_texto_inteligente(texto, 30, 5)

for i, chunk in enumerate(chunks, 1):
    print(f"Chunk {i} ({len(chunk)} chars): {chunk[:50]}...")
```

**Vantagem:** Melhor qualidade, mantém contexto.

---

## 🎯 Aplicação no seu código (Resumidor de PDF)

### Versão completa com chunking:

```python
from typing import List, Optional
import re

def dividir_texto_em_chunks(texto: str, tamanho_chunk: int = 3000, overlap: int = 200) -> List[str]:
    """
    Divide texto em chunks inteligentes para processamento.
    
    Args:
        texto: Texto a ser dividido
        tamanho_chunk: Tamanho máximo de cada chunk
        overlap: Sobreposição entre chunks (para manter contexto)
    
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


def resumir_texto_em_chunks(texto: str, llm_client, tamanho_chunk: int = 3000) -> Optional[str]:
    """
    Resumir texto dividindo em chunks se necessário.
    
    Args:
        texto: Texto a ser resumido
        llm_client: Cliente LLM (Groq, Gemini, etc)
        tamanho_chunk: Tamanho máximo de cada chunk
    
    Returns:
        Resumo completo do texto
    """
    # Dividir em chunks se necessário
    if len(texto) <= tamanho_chunk:
        # Texto cabe em um chunk, processar direto
        return resumir_chunk(texto, llm_client)
    
    # Texto muito grande, dividir e processar por partes
    chunks = dividir_texto_em_chunks(texto, tamanho_chunk)
    print(f"📦 Texto dividido em {len(chunks)} chunks")
    
    resumos_chunks = []
    
    for i, chunk in enumerate(chunks, 1):
        print(f"📄 Processando chunk {i}/{len(chunks)}...")
        resumo_chunk = resumir_chunk(chunk, llm_client)
        
        if resumo_chunk:
            resumos_chunks.append(resumo_chunk)
        else:
            print(f"⚠️  Erro ao processar chunk {i}")
    
    if not resumos_chunks:
        return None
    
    # Se temos múltiplos resumos, resumir novamente
    if len(resumos_chunks) > 1:
        print("🔄 Combinando resumos dos chunks...")
        texto_combinado = "\n\n".join(resumos_chunks)
        return resumir_chunk(texto_combinado, llm_client)
    
    return resumos_chunks[0]


def resumir_chunk(chunk: str, llm_client) -> Optional[str]:
    """
    Resumir um único chunk de texto.
    """
    prompt = f"""
    Resuma o seguinte texto de forma clara e concisa:
    
    {chunk}
    
    Resumo:
    """
    
    try:
        response = llm_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=200,
        )
        
        return response.choices[0].message.content.strip()
        
    except Exception as e:
        print(f"❌ Erro ao resumir chunk: {e}")
        return None
```

---

## 📊 Comparação dos Métodos

| Método | Vantagem | Desvantagem | Quando Usar |
|--------|----------|-------------|-------------|
| **Por caracteres** | Simples e rápido | Corta palavras | Texto não estruturado |
| **Por palavras** | Não corta palavras | Pode perder contexto | Texto normal |
| **Com overlap** | Mantém contexto | Mais tokens usados | Texto longo importante |
| **Por sentenças** | Mantém estrutura | Mais complexo | Texto bem formatado |
| **Inteligente** | Melhor qualidade | Mais lento | Produção/qualidade |

---

## 💡 Exemplo Prático Completo

```python
from typing import List
import re

def dividir_pdf_em_chunks(texto_pdf: str, max_caracteres: int = 3000) -> List[str]:
    """
    Divide texto de PDF em chunks para processamento.
    """
    if len(texto_pdf) <= max_caracteres:
        return [texto_pdf]
    
    chunks = []
    inicio = 0
    
    while inicio < len(texto_pdf):
        fim = inicio + max_caracteres
        
        if fim < len(texto_pdf):
            # Tentar terminar em ponto final
            ultimo_ponto = texto_pdf.rfind(".", inicio, fim)
            if ultimo_ponto > inicio:
                fim = ultimo_ponto + 1
            else:
                # Se não encontrou ponto, terminar em espaço
                ultimo_espaco = texto_pdf.rfind(" ", inicio, fim)
                if ultimo_espaco > inicio:
                    fim = ultimo_espaco
        
        chunk = texto_pdf[inicio:fim].strip()
        if chunk:
            chunks.append(chunk)
        
        inicio = fim
    
    return chunks

# Uso no seu código:
texto = extrair_texto_pdf("documento.pdf")

if texto and len(texto) > 3000:
    chunks = dividir_pdf_em_chunks(texto, 3000)
    
    for i, chunk in enumerate(chunks, 1):
        print(f"Processando chunk {i}/{len(chunks)}...")
        resumo = resumir_com_groq(chunk)
        # ... salvar ou combinar resumos
else:
    resumo = resumir_com_groq(texto)
```

---

## 🎯 Recomendação para seu Dia 4

**Use o Método 2 (por palavras) ou Método 5 (inteligente):**

```python
def dividir_texto_em_chunks(texto: str, tamanho: int = 3000) -> list[str]:
    """Divide texto sem cortar palavras."""
    if len(texto) <= tamanho:
        return [texto]
    
    chunks = []
    palavras = texto.split()
    chunk_atual = ""
    
    for palavra in palavras:
        if len(chunk_atual) + len(palavra) + 1 <= tamanho:
            chunk_atual = chunk_atual + " " + palavra if chunk_atual else palavra
        else:
            if chunk_atual:
                chunks.append(chunk_atual)
            chunk_atual = palavra
    
    if chunk_atual:
        chunks.append(chunk_atual)
    
    return chunks
```

**Simples, eficiente e não corta palavras!** ✅

