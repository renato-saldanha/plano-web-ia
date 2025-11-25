# 🔧 Troubleshooting: Autocomplete não funciona no Python

Guia para resolver problemas de autocomplete/IntelliSense no Python.

---

## 🔍 Principais Causas

### 1. **Ambiente Virtual não Ativado/Reconhecido**

**Problema:** O editor não reconhece o ambiente virtual onde as bibliotecas estão instaladas.

**Solução:**
```bash
# 1. Ativar o venv
# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate

# 2. No VS Code/Cursor:
# - Pressione Ctrl+Shift+P (ou Cmd+Shift+P no Mac)
# - Digite: "Python: Select Interpreter"
# - Escolha o interpretador do venv (venv\Scripts\python.exe)
```

---

### 2. **Biblioteca não Instalada no Ambiente Atual**

**Problema:** Você instalou a biblioteca em outro ambiente ou globalmente.

**Solução:**
```bash
# Verificar se está no venv correto
which python  # Mac/Linux
where python  # Windows

# Instalar biblioteca no venv ativo
pip install groq python-dotenv

# Verificar se foi instalado
pip list | grep groq
```

---

### 3. **Linter/Type Checker não Configurado**

**Problema:** O editor não tem um linter configurado para Python.

**Solução:**
```bash
# Instalar Pylance (recomendado) ou Jedi
# No VS Code/Cursor, instale a extensão:
# - Python (Microsoft)
# - Pylance (Microsoft)
```

**Configurar no VS Code/Cursor:**
```json
// .vscode/settings.json
{
    "python.languageServer": "Pylance",
    "python.analysis.typeCheckingMode": "basic"
}
```

---

### 4. **Tipos não Definidos (Type Hints)**

**Problema:** Objetos sem type hints não são reconhecidos pelo autocomplete.

**Solução:**
```python
# ❌ Sem type hints - autocomplete pode não funcionar
def processar_dados(dados):
    return dados.upper()  # Não sabe que 'dados' é string

# ✅ Com type hints - autocomplete funciona
def processar_dados(dados: str) -> str:
    return dados.upper()  # Sabe que 'dados' é string
```

**Para bibliotecas externas:**
```python
from groq import Groq
from typing import Optional

# Type hint ajuda o autocomplete
client: Groq = Groq(api_key="sua_chave")

# Agora o autocomplete funciona melhor
client.chat.completions.create(...)  # ✅ Autocomplete funciona
```

---

### 5. **Biblioteca sem Stubs de Tipo**

**Problema:** Algumas bibliotecas não têm arquivos `.pyi` (type stubs).

**Solução:**
```bash
# Instalar stubs se disponíveis
pip install types-requests  # Exemplo para requests

# Ou usar type: ignore
from groq import Groq  # type: ignore
```

---

### 6. **Cache do Editor Corrompido**

**Problema:** Cache do editor pode estar desatualizado.

**Solução:**
```bash
# VS Code/Cursor:
# 1. Fechar editor
# 2. Deletar pasta .vscode/.cache (se existir)
# 3. Reabrir editor

# Ou via comando:
# Ctrl+Shift+P → "Python: Clear Cache and Reload Window"
```

---

### 7. **Importação Dinâmica**

**Problema:** Imports dinâmicos não são reconhecidos.

**Solução:**
```python
# ❌ Importação dinâmica - autocomplete não funciona
modulo = __import__('groq')
client = modulo.Groq()

# ✅ Importação normal - autocomplete funciona
from groq import Groq
client = Groq()
```

---

## 🎯 Soluções Específicas para Groq/Gemini

### Groq API

```python
# ✅ Forma correta (autocomplete funciona)
from groq import Groq

client = Groq(api_key="sua_chave")
# Agora client.chat.completions.create() tem autocomplete
```

**Se não funcionar:**
```python
# Adicionar type hint explícito
from groq import Groq
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from groq.types.chat import ChatCompletion

client = Groq(api_key="sua_chave")
completion: ChatCompletion = client.chat.completions.create(...)
```

### Gemini API

```python
# ✅ Forma correta
import google.generativeai as genai

genai.configure(api_key="sua_chave")
model = genai.GenerativeModel('gemini-pro')
# Agora model.generate_content() tem autocomplete
```

---

## 🔧 Checklist de Verificação

- [ ] Ambiente virtual está ativado
- [ ] Interpretador Python correto selecionado no editor
- [ ] Bibliotecas instaladas no venv ativo (`pip list`)
- [ ] Extensão Python/Pylance instalada
- [ ] Type hints adicionados nas funções
- [ ] Cache do editor limpo
- [ ] Imports são estáticos (não dinâmicos)

---

## 💡 Dicas Rápidas

### 1. Verificar Interpretador
```python
import sys
print(sys.executable)  # Deve apontar para venv\Scripts\python.exe
```

### 2. Forçar Recarregar
- **VS Code/Cursor:** `Ctrl+Shift+P` → "Developer: Reload Window"

### 3. Verificar Instalação
```bash
# No terminal do venv
python -c "import groq; print(groq.__file__)"
# Deve mostrar caminho dentro do venv
```

### 4. Usar Type Hints
```python
# Sempre que possível, adicione type hints
def minha_funcao(parametro: str) -> dict:
    return {"resultado": parametro}
```

---

## 🐛 Erro Específico: "Cannot find reference"

**Causa:** Editor não encontra o módulo.

**Solução:**
```python
# Adicionar ao início do arquivo
# type: ignore
# ou
# pylint: disable=import-error

from groq import Groq  # type: ignore
```

---

## 📚 Recursos

- **Pylance Docs:** https://github.com/microsoft/pylance-release
- **Python Type Hints:** https://docs.python.org/3/library/typing.html
- **VS Code Python:** https://code.visualstudio.com/docs/languages/python

---

**Se nada funcionar:** Reinicie o editor e verifique se o venv está ativado! 🔄

