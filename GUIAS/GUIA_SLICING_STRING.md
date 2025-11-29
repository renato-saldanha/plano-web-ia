# 📝 Guia: Como Retornar Parte de um Texto em Python

## 🎯 Slicing (Fatiamento) de Strings

Em Python, você usa **slicing** (fatiamento) para pegar parte de um texto.

### Sintaxe Básica:
```python
texto[inicio:fim]  # Pega do índice 'inicio' até 'fim' (não inclui 'fim')
```

---

## 📚 Exemplos Práticos

### 1. **Primeiros N caracteres**
```python
texto = "Este é um texto muito longo"
primeiros_10 = texto[:10]  # "Este é um"
print(primeiros_10)
```

### 2. **Últimos N caracteres**
```python
texto = "Este é um texto muito longo"
ultimos_10 = texto[-10:]  # "to longo"
print(ultimos_10)
```

### 3. **Do índice X até Y**
```python
texto = "Este é um texto muito longo"
parte = texto[5:15]  # "é um texto"
print(parte)
```

### 4. **Limitar tamanho máximo**
```python
texto = "Este é um texto muito longo"
max_caracteres = 20
texto_limitado = texto[:max_caracteres]  # "Este é um texto muit"
print(texto_limitado)
```

---

## 🎯 Para seu caso (PDF muito grande)

### Problema:
PDFs podem ter milhares de caracteres, mas APIs têm limite de tokens.

### Solução: Limitar texto antes de enviar

```python
def resumir_com_groq(texto: str, max_caracteres: int = 3000) -> str:
    """
    Resumir texto, limitando o tamanho antes de enviar para API.
    """
    # Limitar texto se for muito grande
    if len(texto) > max_caracteres:
        texto_limitado = texto[:max_caracteres]
        print(f"⚠️  Texto muito grande ({len(texto)} chars). Limitando para {max_caracteres} chars")
    else:
        texto_limitado = texto
    
    prompt = f"""
    Resuma o seguinte texto em 200 palavras:
    {texto_limitado}
    Resumo:
    """
    # ... resto do código
```

---

## 📋 Exemplos Completos

### Exemplo 1: Limitar texto para API
```python
texto_completo = "Texto muito longo..." * 1000  # 20.000 caracteres

# Limitar para 3000 caracteres
texto_limitado = texto_completo[:3000]
print(f"Original: {len(texto_completo)} chars")
print(f"Limitado: {len(texto_limitado)} chars")
```

### Exemplo 2: Pegar primeiros N caracteres
```python
texto = extrair_texto_pdf("documento.pdf")

# Mostrar primeiros 500 caracteres
if texto:
    preview = texto[:500]
    print(f"Preview: {preview}...")
```

### Exemplo 3: Dividir texto em chunks
```python
def dividir_texto_em_chunks(texto: str, tamanho_chunk: int = 3000) -> list:
    """
    Divide texto em pedaços menores.
    """
    chunks = []
    for i in range(0, len(texto), tamanho_chunk):
        chunk = texto[i:i + tamanho_chunk]
        chunks.append(chunk)
    return chunks

# Uso:
texto = "Texto muito longo..."
chunks = dividir_texto_em_chunks(texto, 3000)
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}: {len(chunk)} caracteres")
```

---

## 🔧 Funções Úteis

### 1. **Limitar tamanho com "..."**
```python
def limitar_texto(texto: str, max_caracteres: int = 100) -> str:
    """
    Limita texto e adiciona "..." se foi cortado.
    """
    if len(texto) <= max_caracteres:
        return texto
    return texto[:max_caracteres] + "..."
```

### 2. **Pegar primeiras N palavras**
```python
def primeiras_palavras(texto: str, n: int = 50) -> str:
    """
    Retorna primeiras N palavras do texto.
    """
    palavras = texto.split()
    return " ".join(palavras[:n])
```

### 3. **Cortar por palavras (não cortar palavra no meio)**
```python
def limitar_por_palavras(texto: str, max_caracteres: int = 100) -> str:
    """
    Limita texto sem cortar palavras no meio.
    """
    if len(texto) <= max_caracteres:
        return texto
    
    # Cortar e procurar último espaço
    texto_cortado = texto[:max_caracteres]
    ultimo_espaco = texto_cortado.rfind(" ")
    
    if ultimo_espaco > 0:
        return texto_cortado[:ultimo_espaco] + "..."
    return texto_cortado + "..."
```

---

## 💡 Para seu código do Dia 4

### Versão melhorada da função `resumir_com_groq`:

```python
def resumir_com_groq(texto: str, max_caracteres: int = 3000) -> str:
    """
    Resumir texto usando Groq, limitando tamanho se necessário.
    
    Args:
        texto: Texto a ser resumido
        max_caracteres: Tamanho máximo do texto a enviar (padrão: 3000)
    
    Returns:
        Resumo do texto
    """
    # Limitar texto se for muito grande
    if len(texto) > max_caracteres:
        texto_limitado = texto[:max_caracteres]
        print(f"⚠️  Texto muito grande ({len(texto)} chars). Limitando para {max_caracteres} chars")
    else:
        texto_limitado = texto
    
    prompt = f"""
    Resuma o seguinte texto em 200 palavras:
    {texto_limitado}
    Resumo:
    """
    
    try:
        response = llm_groq.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=0.3,
            max_tokens=200,
        )
        
        resumo = response.choices[0].message.content.strip()
        
        if not resumo:
            raise Exception("Não foi possível encontrar um resumo válido")
        
        return resumo
        
    except Exception as e:
        print(f"Erro ao resumir texto com Groq: {e}")
        return None
```

---

## 📊 Tabela de Referência Rápida

| Sintaxe | Significado | Exemplo |
|---------|-------------|---------|
| `texto[:10]` | Primeiros 10 caracteres | `"Olá mundo"[:5]` → `"Olá m"` |
| `texto[5:]` | Do índice 5 até o fim | `"Olá mundo"[4:]` → `"mundo"` |
| `texto[5:10]` | Do índice 5 até 10 (não inclui 10) | `"Olá mundo"[4:9]` → `"mund"` |
| `texto[-5:]` | Últimos 5 caracteres | `"Olá mundo"[-5:]` → `"mundo"` |
| `texto[:]` | Texto completo (cópia) | `"Olá mundo"[:]` → `"Olá mundo"` |

---

## 🎯 Resumo

**Para retornar parte de um texto, use slicing:**

```python
# Primeiros N caracteres
texto[:N]

# Últimos N caracteres  
texto[-N:]

# Do índice X até Y
texto[X:Y]

# Limitar tamanho máximo
texto[:max_caracteres]
```

**No seu caso específico (limitar texto para API):**
```python
if len(texto) > 3000:
    texto = texto[:3000]  # Limita para 3000 caracteres
```

