# 📚 Guia: Type Hints e Docstrings em Python

## 🎯 O que são?

### Type Hints (Anotações de Tipo)
- Indicam o **tipo** dos parâmetros e retorno de funções
- Ajudam IDEs a dar autocomplete melhor
- Facilitam leitura e manutenção do código
- **NÃO afetam a execução** (Python ignora se não tiver ferramentas de tipo)

### Docstrings
- Documentação **dentro** do código
- Explicam o que a função faz, parâmetros, retorno e exemplos
- Aparecem quando você usa `help(funcao)` ou no hover do IDE

---

## 📝 Exemplo 1: Função Simples (Dia 2)

### ❌ ANTES (sem type hints e docstrings):
```python
def gerar_conteudo_tema(tema: str): 
    if not tema:
        raise ValueError("Favor escolher um tema.")
    # ... resto do código
    return resposta + "\n" + "=" * 60
```

### ✅ DEPOIS (com type hints e docstrings):
```python
from typing import Optional

def gerar_conteudo_tema(tema: str) -> Optional[str]:
    """
    Gera conteúdo de blog sobre um tema específico usando Groq API.
    
    Args:
        tema: Tema do conteúdo a ser gerado (ex: "Python", "IA")
    
    Returns:
        String com o conteúdo gerado formatado, ou None em caso de erro
    
    Raises:
        ValueError: Se o tema estiver vazio ou None
    
    Example:
        >>> conteudo = gerar_conteudo_tema("Python")
        >>> print(conteudo)
    """
    if not tema:
        raise ValueError("Favor escolher um tema.")
    # ... resto do código
    return resposta + "\n" + "=" * 60
```

**Explicação:**
- `-> Optional[str]`: Indica que retorna `str` ou `None`
- `Optional[str]` = `str | None` (Python 3.10+) ou `Union[str, None]`
- Docstring explica o que faz, parâmetros, retorno e exceções

---

## 📝 Exemplo 2: Função que Retorna Múltiplos Valores (Dia 3)

### ❌ ANTES:
```python
def analisar_sentimento_groq(prompt: str, texto: str) -> str:
    # ... código ...
    return sentimento_texto, tempo_resposta_ms, tokens
```

### ✅ DEPOIS:
```python
from typing import Tuple, Optional

def analisar_sentimento_groq(prompt: str, texto: str) -> Optional[Tuple[str, float, int]]:
    """
    Analisa o sentimento de um texto usando Groq API.
    
    Args:
        prompt: Prompt formatado para análise de sentimentos
        texto: Texto a ser analisado
    
    Returns:
        Tupla com (sentimento, tempo_ms, tokens) ou None em caso de erro
        - sentimento: "positivo", "negativo" ou "neutro"
        - tempo_ms: Tempo de resposta em milissegundos
        - tokens: Número de tokens utilizados
    
    Raises:
        Exception: Se não conseguir obter resposta da API
    
    Example:
        >>> resultado = analisar_sentimento_groq(prompt, "Este produto é incrível!")
        >>> if resultado:
        ...     sentimento, tempo, tokens = resultado
        ...     print(f"Sentimento: {sentimento}")
    """
    # ... código ...
    return sentimento_texto, tempo_resposta_ms, tokens
```

**Explicação:**
- `Tuple[str, float, int]`: Tupla com 3 elementos (string, float, int)
- `Optional[...]`: Pode retornar None em caso de erro
- Docstring detalha cada elemento da tupla retornada

---

## 📝 Exemplo 3: Função com Lista (Dia 3)

### ❌ ANTES:
```python
def ler_reviews() -> list:
    # ... código ...
    return reviews
```

### ✅ DEPOIS:
```python
from typing import List, Optional

def ler_reviews() -> Optional[List[str]]:
    """
    Lê reviews de um arquivo de texto.
    
    Returns:
        Lista de strings com os reviews, ou None em caso de erro
    
    Raises:
        FileNotFoundError: Se o arquivo não existir
        PermissionError: Se não tiver permissão para ler o arquivo
    
    Example:
        >>> reviews = ler_reviews()
        >>> if reviews:
        ...     print(f"Total de reviews: {len(reviews)}")
    """
    # ... código ...
    return reviews
```

**Explicação:**
- `List[str]`: Lista de strings
- `Optional[List[str]]`: Pode retornar None
- Em Python 3.9+ pode usar `list[str]` ao invés de `List[str]`

---

## 📝 Exemplo 4: Função com Dicionário (Dia 3)

### ❌ ANTES:
```python
def comparar_reviews_llm(reviews: list) -> dict:
    # ... código ...
    return tabela
```

### ✅ DEPOIS:
```python
from typing import List, Optional, Dict, Any

def comparar_reviews_llm(reviews: List[str]) -> Optional[str]:
    """
    Compara análise de sentimentos entre múltiplos LLMs.
    
    Args:
        reviews: Lista de strings com os reviews a serem analisados
    
    Returns:
        String formatada em markdown com tabela comparativa, ou None em caso de erro
    
    Example:
        >>> reviews = ["Produto incrível!", "Péssima qualidade"]
        >>> resultado = comparar_reviews_llm(reviews)
        >>> if resultado:
        ...     print(resultado)
    """
    # ... código ...
    return tabela
```

**Explicação:**
- `List[str]`: Lista de strings
- `Optional[str]`: Retorna string ou None
- Se retornasse dicionário: `Dict[str, Any]` ou `dict[str, Any]`

---

## 📝 Exemplo 5: Função que Não Retorna Nada

### ❌ ANTES:
```python
def salvar_arquivo_tema_blog(tema: str, conteudo: str):
    # ... código ...
```

### ✅ DEPOIS:
```python
from typing import NoReturn  # Para funções que nunca retornam

def salvar_arquivo_tema_blog(tema: str, conteudo: str) -> None:
    """
    Salva conteúdo gerado em arquivo markdown.
    
    Args:
        tema: Tema do conteúdo (usado como nome do arquivo)
        conteudo: Conteúdo a ser salvo
    
    Raises:
        PermissionError: Se não tiver permissão para escrever
        OSError: Se houver erro ao criar diretório ou arquivo
    
    Example:
        >>> salvar_arquivo_tema_blog("Python", "# Python é incrível!")
    """
    # ... código ...
```

**Explicação:**
- `-> None`: Função não retorna valor (ou retorna None implicitamente)
- `NoReturn`: Apenas para funções que nunca retornam (ex: `sys.exit()`)

---

## 🎨 Formatos de Docstring

### Formato Google (Recomendado - Mais Simples)
```python
def minha_funcao(param1: str, param2: int = 10) -> bool:
    """
    Descrição curta do que a função faz.
    
    Descrição mais detalhada se necessário. Pode ter múltiplas
    linhas explicando o comportamento da função.
    
    Args:
        param1: Descrição do primeiro parâmetro
        param2: Descrição do segundo parâmetro (padrão: 10)
    
    Returns:
        Descrição do valor retornado
    
    Raises:
        ValueError: Quando param1 está vazio
        TypeError: Quando param2 não é int
    
    Example:
        >>> resultado = minha_funcao("teste", 20)
        >>> print(resultado)
        True
    """
    pass
```

### Formato NumPy (Alternativa)
```python
def minha_funcao(param1: str, param2: int = 10) -> bool:
    """
    Descrição curta do que a função faz.
    
    Descrição mais detalhada se necessário.
    
    Parameters
    ----------
    param1 : str
        Descrição do primeiro parâmetro
    param2 : int, optional
        Descrição do segundo parâmetro (padrão: 10)
    
    Returns
    -------
    bool
        Descrição do valor retornado
    
    Raises
    ------
    ValueError
        Quando param1 está vazio
    TypeError
        Quando param2 não é int
    
    Examples
    --------
    >>> resultado = minha_funcao("teste", 20)
    >>> print(resultado)
    True
    """
    pass
```

**Recomendação:** Use o formato **Google** (mais simples e legível)

---

## 📦 Imports Comuns para Type Hints

```python
from typing import (
    Optional,      # Para valores que podem ser None
    List,          # Para listas (Python < 3.9)
    Dict,          # Para dicionários (Python < 3.9)
    Tuple,         # Para tuplas
    Union,         # Para múltiplos tipos possíveis
    Any,           # Para qualquer tipo
    Callable,      # Para funções
)

# Python 3.9+ pode usar tipos built-in:
# list[str] ao invés de List[str]
# dict[str, int] ao invés de Dict[str, int]
# tuple[str, int] ao invés of Tuple[str, int]
```

---

## 🎯 Exemplo Completo: Refatorando seu código do Dia 2

### ❌ ANTES:
```python
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
    # ... resto do código
    return resposta + "\n" + "=" * 60

def salvar_arquivo_tema_blog(tema: str, conteudo: str):
    if not os.path.exists("resultado_blog"):
        os.makedirs("resultado_blog")
    # ... resto do código
```

### ✅ DEPOIS:
```python
import os
import time
from typing import Optional
from dotenv import load_dotenv
from groq import Groq
from datetime import datetime

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY não encontrada no arquivo .env")

client = Groq(api_key=groq_api_key)


def gerar_conteudo_tema(tema: str) -> Optional[str]:
    """
    Gera conteúdo de blog sobre um tema específico usando Groq API.
    
    O conteúdo é gerado com estilo RPG/D&D e salvo automaticamente
    em arquivo markdown.
    
    Args:
        tema: Tema do conteúdo a ser gerado (ex: "Python", "IA", "Web Development")
    
    Returns:
        String com o conteúdo gerado formatado, ou None em caso de erro
    
    Raises:
        ValueError: Se o tema estiver vazio ou None
        Exception: Se houver erro na API do Groq
    
    Example:
        >>> conteudo = gerar_conteudo_tema("Python")
        >>> if conteudo:
        ...     print(conteudo)
    """
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
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=0.45,
            max_tokens=200,
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


def salvar_arquivo_tema_blog(tema: str, conteudo: str) -> None:
    """
    Salva conteúdo gerado em arquivo markdown na pasta resultado_blog.
    
    O arquivo será nomeado com o tema e incluirá metadados como data de geração.
    
    Args:
        tema: Tema do conteúdo (usado como nome do arquivo)
        conteudo: Conteúdo a ser salvo no arquivo
    
    Raises:
        PermissionError: Se não tiver permissão para escrever na pasta
        OSError: Se houver erro ao criar diretório ou arquivo
    
    Example:
        >>> salvar_arquivo_tema_blog("Python", "# Python é incrível!")
    """
    if not os.path.exists("resultado_blog"):
        os.makedirs("resultado_blog")
    
    caminho_arquivo = f"resultado_blog/{tema}.md"
    
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(f"# {tema}\n\n")
        arquivo.write(f"**Data de geração:** {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n")
        arquivo.write("---\n\n")
        arquivo.write(conteudo)
    
    print(f"✅ Arquivo salvo: {caminho_arquivo}")


if __name__ == "__main__":
    print(gerar_conteudo_tema("Inteligência Artificial"))
    print(gerar_conteudo_tema("Python"))
    print(gerar_conteudo_tema("Web Development"))
```

---

## 🎯 Checklist Rápido

Para cada função, adicione:

1. **Type hints nos parâmetros:**
   ```python
   def funcao(param1: str, param2: int = 10):
   ```

2. **Type hint no retorno:**
   ```python
   def funcao(param1: str) -> str:
   # ou
   def funcao(param1: str) -> Optional[str]:
   # ou
   def funcao(param1: str) -> None:
   ```

3. **Docstring básica:**
   ```python
   def funcao(param1: str) -> str:
       """
       Descrição curta do que faz.
       
       Args:
           param1: Descrição do parâmetro
       
       Returns:
           Descrição do retorno
       """
   ```

---

## 💡 Dicas Finais

1. **Comece simples:** Adicione type hints básicos primeiro (`str`, `int`, `bool`)
2. **Use `Optional`** quando a função pode retornar `None`
3. **Docstrings curtas são melhores** que docstrings longas e confusas
4. **Exemplos ajudam muito** - inclua sempre que possível
5. **IDEs modernas** (VS Code, PyCharm) mostram type hints e docstrings no hover

---

## 📚 Recursos

- [Python Typing Documentation](https://docs.python.org/3/library/typing.html)
- [Google Style Guide - Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
- [Real Python - Type Hints](https://realpython.com/python-type-checking/)

---

**Próximo passo:** Aplique isso no seu código do Dia 4! 🚀

