# 💾 Como Gravar Arquivos em Python

Guia rápido para gravar arquivos em Python (não precisa instalar biblioteca externa!).

---

## 📝 Método 1: `open()` - Básico (Built-in)

### Gravar Texto Simples

```python
# Gravar arquivo .txt
with open("arquivo.txt", "w", encoding="utf-8") as f:
    f.write("Conteúdo do arquivo")

# Gravar arquivo .md (Markdown)
with open("arquivo.md", "w", encoding="utf-8") as f:
    f.write("# Título\n\nConteúdo aqui")
```

### Adicionar ao Final (Append)

```python
# Adicionar ao final do arquivo
with open("arquivo.txt", "a", encoding="utf-8") as f:
    f.write("\nNova linha adicionada")
```

---

## 📋 Modos de Abertura

| Modo | Descrição |
|------|-----------|
| `"w"` | **Write** - Escreve (sobrescreve se existir) |
| `"a"` | **Append** - Adiciona ao final |
| `"x"` | **Exclusive** - Cria novo (erro se existir) |
| `"r"` | **Read** - Apenas leitura |

---

## 🎯 Exemplo Completo para seu Script

```python
import os
from datetime import datetime

def salvar_conteudo(tema: str, conteudo: str, pasta: str = "resultados"):
    """
    Salva o conteúdo gerado em um arquivo.
    
    Args:
        tema: Tema do conteúdo
        conteudo: Conteúdo gerado pela IA
        pasta: Pasta onde salvar (padrão: "resultados")
    """
    # Criar pasta se não existir
    if not os.path.exists(pasta):
        os.makedirs(pasta)
        print(f"📁 Pasta '{pasta}' criada!")
    
    # Criar nome do arquivo (remover caracteres especiais)
    nome_arquivo = tema.lower().replace(" ", "_")
    nome_arquivo = "".join(c for c in nome_arquivo if c.isalnum() or c == "_")
    nome_arquivo = f"{nome_arquivo}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    
    # Caminho completo
    caminho_arquivo = os.path.join(pasta, nome_arquivo)
    
    # Gravar arquivo
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        f.write(f"# {tema}\n\n")
        f.write(f"**Data de geração:** {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n")
        f.write("---\n\n")
        f.write(conteudo)
    
    print(f"💾 Arquivo salvo: {caminho_arquivo}")
    return caminho_arquivo
```

---

## 📄 Exemplos Práticos

### 1. Gravar Arquivo .txt

```python
conteudo = "Meu conteúdo aqui"

with open("resultado.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(conteudo)
```

### 2. Gravar Arquivo .md (Markdown)

```python
conteudo = "# Título\n\nParágrafo aqui."

with open("resultado.md", "w", encoding="utf-8") as arquivo:
    arquivo.write(conteudo)
```

### 3. Gravar Múltiplas Linhas

```python
linhas = [
    "Linha 1",
    "Linha 2",
    "Linha 3"
]

with open("resultado.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("\n".join(linhas))
    # ou
    # for linha in linhas:
    #     arquivo.write(linha + "\n")
```

### 4. Gravar com Formatação

```python
tema = "Inteligência Artificial"
conteudo = "Texto gerado pela IA..."

with open("resultado.md", "w", encoding="utf-8") as arquivo:
    arquivo.write(f"# {tema}\n\n")
    arquivo.write(f"**Data:** {datetime.now().strftime('%d/%m/%Y')}\n\n")
    arquivo.write("---\n\n")
    arquivo.write(conteudo)
```

---

## 🔧 Funções Úteis

### Criar Pasta se Não Existir

```python
import os

pasta = "resultados"
if not os.path.exists(pasta):
    os.makedirs(pasta)
```

### Criar Nome de Arquivo Seguro

```python
def nome_arquivo_seguro(texto: str) -> str:
    """Remove caracteres especiais do nome do arquivo."""
    # Substituir espaços por underscore
    nome = texto.lower().replace(" ", "_")
    # Remover caracteres especiais
    nome = "".join(c for c in nome if c.isalnum() or c in ("_", "-"))
    return nome

# Uso
nome = nome_arquivo_seguro("Inteligência Artificial!")
# Resultado: "inteligencia_artificial"
```

### Adicionar Timestamp

```python
from datetime import datetime

nome_arquivo = f"conteudo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
# Resultado: "conteudo_20241125_143022.md"
```

---

## ⚠️ Importante: Encoding UTF-8

**SEMPRE use `encoding="utf-8"`** para suportar caracteres especiais (acentos, emojis, etc.):

```python
# ✅ Correto
with open("arquivo.txt", "w", encoding="utf-8") as f:
    f.write("Ação e reação")

# ❌ Pode dar erro com acentos
with open("arquivo.txt", "w") as f:
    f.write("Ação e reação")  # Pode gerar erro
```

---

## 📚 Bibliotecas Opcionais (Não Necessárias)

### Se precisar de funcionalidades avançadas:

- **`pathlib`** (built-in Python 3.4+) - Manipulação de caminhos mais moderna
- **`json`** (built-in) - Para arquivos JSON
- **`csv`** (built-in) - Para arquivos CSV
- **`pickle`** (built-in) - Para objetos Python

---

## ✅ Resumo

**Para gravar arquivos em Python:**
- ✅ **Não precisa instalar nada!** Use `open()` built-in
- ✅ **Sempre use `encoding="utf-8"`** para caracteres especiais
- ✅ **Use `with open()`** para garantir fechamento automático
- ✅ **Modo `"w"`** para escrever, `"a"` para adicionar

---

**É isso! Python já tem tudo que você precisa!** 🎉

