# 📅 Semana 1: Fundamentos de IA Generativa

**Período:** 24 Nov - 30 Nov 2024  
**Objetivo:** Entender conceitos básicos de IA e criar primeiros scripts de automação

---

## 🎯 Objetivos da Semana

- ✅ Entender conceitos 2025: tokens, embeddings, prompts, context window, streaming
- ✅ Configurar ambiente Python 3.12 + APIs de IA (Groq, Gemini, Claude)
- ✅ Comparar 3 LLMs diferentes (nova habilidade crítica 2025)
- ✅ Criar primeiros 3 scripts de automação

---

## 📋 Cronograma Diário

| Dia | Data | Dia da Semana | Foco | Entrega |
|-----|------|---------------|------|---------|
| **Dia 1** | 24/11 | Segunda-feira | Setup APIs + Tutorial básico prompting | Hello AI funcionando |
| **Dia 2** | 25/11 | Terça-feira | Script 1 - Gerador de conteúdo para blog | Script funcionando |
| **Dia 3** | 26/11 | Quarta-feira | Script 2 - Analisador de sentimentos (3 LLMs) | Comparação documentada |
| **Dia 4** | 27/11 | Quinta-feira | Script 3 - Resumidor de documentos PDF | Script funcionando |
| **Dia 5** | 28/11 | Sexta-feira | Refatorar scripts + Documentação | Código limpo + README |
| **Dia 6** | 29/11 | Sábado | Projeto integrado: CLI para múltiplas automações | CLI funcional |
| **Dia 7** | 30/11 | Domingo | Deploy no GitHub + README épico + Review | Projeto completo |

---

## 📁 Estrutura de Pastas

```
Semana1/
├── README.md (este arquivo)
├── Dia1/
│   ├── README.md
│   ├── checklist.md
│   ├── hello_ai_groq.py
│   ├── setup_apis.md
│   ├── journal.md
│   └── requirements.txt
├── Dia2/
|   ├── resultado_blog/
│   ├── README.md
│   ├── journal.md
│   ├── checklist.md
|   ├── gerador_conteudo_blog.py
├── Dia3/
|   ├── resultado_comparacao/
|   ├── reviews/
│   ├── README.md
│   ├── journal.md
│   ├── checklist.md
|   ├── analisador_sentimentos.py
├── Dia4/
|   ├── pdfs/
|   ├── resultado_comparacao/
│   ├── README.md
│   ├── journal.md
│   ├── checklist.md
|   ├── resumidor_pdf.py
├── Dia5/
│   ├── README.md
├── Dia6/
└── Dia7/
```

---

## 🎯 Entrega Final da Semana

**Projeto:** CLI de Automações com IA

**Features:**
- [ X] Gerador de conteúdo para blog
- [ X] Analisador de sentimentos (comparando 3 LLMs)
- [ X] Resumidor de documentos PDF
- [ ] Interface CLI unificada
- [ ] Documentação completa (README)
- [ ] Comparação documentada de LLMs

---

## 📚 Recursos da Semana

- OpenAI Cookbook: Text Generation, Embeddings
- Groq Docs: Llama 3.2, Mixtral
- YouTube: "Groq vs OpenAI Speed Comparison 2025"
- DIO: Curso de APIs em Python

---

## ✅ Checklist Semanal

- [x] Dia 1 completo (Setup) ✅
- [x] Dia 2 completo (Gerador de conteúdo) ✅
- [x] Dia 3 completo (Analisador de sentimentos) ✅
- [x] Dia 4 criado (Resumidor de PDF) 📁
- [x] Dia 5 criado (Refatoração) 📁
- [ ] Dia 6 completo (CLI integrado)
- [ ] Dia 7 completo (Deploy + Review)

---

## Visão Geral da semana

- Utilizei o pdflumber para manipular arquivos PDFs..
- Aprendi a melhorar os prompts em alguns casos.
- Melhorei os scripts com tratamento de erros mais específicos e implementação do logging.
- Aprendi a fazer chamada de um agente, recuperar iformações como modelo, token usado e também calcular métricas.
- Fiz comparações de textos por expressões.

---

## Scripts Criados

- Dia 1: D:\plano web+ia\Semanas\Semana1\Dia1\hello_ai_groq.py
- Dia 2: D:\plano web+ia\Semanas\Semana1\Dia2\gerador_conteudo_blog.py
- Dia 3: D:\plano web+ia\Semanas\Semana1\Dia3\analisardor_sentimentos.py
- Dia 4: D:\plano web+ia\Semanas\Semana1\Dia4\resumidor_pdf.py

## Instalação 
- No terminal digite: 
```python
    cd Semanas/Semana1/
    python -m venv venv
    /venv/Scripts/Activate
    pip install pdflumber groq google.generativeai anthropic dotenv os autopep8
```

## Comando para uso
- Listar pacotes instalados: 
```python
    pip list
```
- Executar script: 
```python
    python [Diretorio]
        Ex: python /Semanas/Semana1/Dia1/script.py
```
- Verificar style guide: 
```python
    python -m autopep8 --dif /Semanas/Semana1/Dia1/script.py
```
- Corrigir style guide automaticamente: 
```python
    python -m autopep8 --in-place /Semanas/Semana1/Dia1/script.py
```

## Links Github:
[Dia 1](https://github.com/renato-saldanha/plano-web-ia/tree/main/Semanas/Semana1/Dia1) <br>
[Dia 2](https://github.com/renato-saldanha/plano-web-ia/tree/main/Semanas/Semana1/Dia2) <br>
[Dia 3](https://github.com/renato-saldanha/plano-web-ia/tree/main/Semanas/Semana1/Dia3) <br>
[Dia 4](https://github.com/renato-saldanha/plano-web-ia/tree/main/Semanas/Semana1/Dia4) <br>
[Dia 5](https://github.com/renato-saldanha/plano-web-ia/tree/main/Semanas/Semana1/Dia5) <br>

## Tecnologias utilizadas:
- Python 3.13
- Cursor 2.0

## Guia de uso:
- Gerador de conteúdo (Dia 2): Basta alterar ou adicionar uma nova linha dentro do metodo "__main__" com um assunto diferente.
> Ex: logging.info(gerar_conteudo_tema("Engenharia de Sofware com IA"))
- Analisador de sentimentos (Dia 3): No arquivo Semanas\Semana1\Dia3\reviews\reviews.txt adicione ou altere os reviews conforme desejado(siga um padrão sempre).
> Seguindo o exemplo no arquivo: ## Review 5 - Cheguei  na loja ao abrir, já não tinha tênis na numeração que uso. Me desanimou.
- Resumidor de PDFs (Dia 4): Adicione arquivos PDF no diretório Semanas\Semana1\Dia4\pdfs\.

# Troubleshooting Comum em Python

## Erros Mais Comuns e Soluções

---

## 1. ModuleNotFoundError / ImportError

### Problema:
```python
ModuleNotFoundError: No module named 'groq'
```

### Soluções:

**Solução 1: Instalar o módulo**
```bash
pip install groq
```

**Solução 2: Verificar ambiente virtual**
```bash
# Ativar venv primeiro
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Depois instalar
pip install groq
```

**Solução 3: Verificar se está no venv correto**
```bash
# Ver onde o Python está instalado
python -c "import sys; print(sys.executable)"

# Verificar se está no venv
which python  # Mac/Linux
where python  # Windows
```

---

## 2. FileNotFoundError

### Problema:
```python
FileNotFoundError: [Errno 2] No such file or directory: 'arquivo.txt'
```

### Soluções:

**Solução 1: Usar caminho absoluto**
```python
import os

# Caminho relativo ao script
diretorio_script = os.path.dirname(os.path.abspath(__file__))
caminho_completo = os.path.join(diretorio_script, "arquivo.txt")

with open(caminho_completo, "r") as f:
    conteudo = f.read()
```

**Solução 2: Verificar se arquivo existe**
```python
import os

if os.path.exists("arquivo.txt"):
    with open("arquivo.txt", "r") as f:
        conteudo = f.read()
else:
    print("Arquivo não encontrado!")
```

**Solução 3: Criar diretório se não existir**
```python
import os

diretorio = "resultados"
if not os.path.exists(diretorio):
    os.makedirs(diretorio, exist_ok=True)
```

---

## 3. PermissionError

### Problema:
```python
PermissionError: [Errno 13] Permission denied: 'arquivo.txt'
```

### Soluções:

**Solução 1: Verificar se arquivo está aberto**
- Feche o arquivo no editor (VS Code, Notepad, etc.)
- Tente novamente

**Solução 2: Verificar permissões**
```python
import os

# Verificar se tem permissão de escrita
if os.access("arquivo.txt", os.W_OK):
    with open("arquivo.txt", "w") as f:
        f.write("conteudo")
else:
    print("Sem permissão de escrita!")
```

**Solução 3: Tratamento de erro**
```python
try:
    with open("arquivo.txt", "w") as f:
        f.write("conteudo")
except PermissionError:
    print("Arquivo está aberto ou bloqueado!")
    print("Feche o arquivo e tente novamente.")
```

---

## 4. KeyError

### Problema:
```python
KeyError: 'chave_inexistente'
```

### Soluções:

**Solução 1: Verificar se chave existe**
```python
dicionario = {"chave": "valor"}

if "chave" in dicionario:
    valor = dicionario["chave"]
else:
    print("Chave não encontrada!")
```

**Solução 2: Usar .get() com valor padrão**
```python
dicionario = {"chave": "valor"}

valor = dicionario.get("chave", "padrão")  # Retorna "padrão" se não existir
```

**Solução 3: Usar try/except**
```python
try:
    valor = dicionario["chave"]
except KeyError:
    valor = "padrão"
```

---

## 5. AttributeError

### Problema:
```python
AttributeError: 'NoneType' object has no attribute 'text'
```

### Soluções:

**Solução 1: Verificar se objeto não é None**
```python
response = fazer_requisicao()

if response is not None:
    texto = response.text
else:
    print("Resposta é None!")
```

**Solução 2: Usar verificação condicional**
```python
response = fazer_requisicao()

if response and hasattr(response, 'text'):
    texto = response.text
else:
    print("Resposta inválida!")
```

---

## 6. TypeError

### Problema:
```python
TypeError: can only concatenate str (not "int") to str
```

### Soluções:

**Solução 1: Converter para string**
```python
idade = 25
mensagem = "Idade: " + str(idade)
```

**Solução 2: Usar f-string**
```python
idade = 25
mensagem = f"Idade: {idade}"
```

**Solução 3: Verificar tipo antes**
```python
def somar(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        raise TypeError("Apenas números são permitidos")
```

---

## 7. ValueError

### Problema:
```python
ValueError: invalid literal for int() with base 10: 'abc'
```

### Soluções:

**Solução 1: Validar entrada**
```python
entrada = input("Digite um número: ")

if entrada.isdigit():
    numero = int(entrada)
else:
    print("Entrada inválida!")
```

**Solução 2: Usar try/except**
```python
try:
    numero = int(input("Digite um número: "))
except ValueError:
    print("Entrada inválida! Digite um número.")
```

---

## 8. IndentationError

### Problema:
```python
IndentationError: expected an indented block
```

### Soluções:

**Solução 1: Usar 4 espaços (não tabs)**
```python
# ✅ CORRETO
def funcao():
    if condicao:
        return True

# ❌ ERRADO (tabs ou espaços errados)
def funcao():
	if condicao:  # Tab
		return True
```

**Solução 2: Configurar editor**
- VS Code/Cursor: Configurar para usar espaços
- Verificar se está usando 4 espaços consistentemente

---

## 9. ❌ SyntaxError

### Problema:
```python
SyntaxError: invalid syntax
```

### Soluções Comuns:

**Problema 1: Parênteses não fechados**
```python
# ❌ ERRADO
if condicao:

# ✅ CORRETO
if condicao:
    pass
```

**Problema 2: Aspas não fechadas**
```python
# ❌ ERRADO
texto = "Olá mundo

# ✅ CORRETO
texto = "Olá mundo"
```

**Problema 3: Dois pontos esquecidos**
```python
# ❌ ERRADO
if condicao
    pass

# ✅ CORRETO
if condicao:
    pass
```

---

## 10. ❌ Problemas com .env (Variáveis de Ambiente)

### Problema:
```python
KeyError: 'GROQ_API_KEY'
```

### Soluções:

**Solução 1: Verificar se arquivo .env existe**
```python
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY não encontrada no .env")
```

**Solução 2: Verificar formato do .env**
```bash
# ✅ CORRETO (.env)
GROQ_API_KEY=sua_chave_aqui
GEMINI_API_KEY=outra_chave

# ❌ ERRADO
GROQ_API_KEY = sua_chave_aqui  # Espaços podem causar problemas
```

**Solução 3: Verificar se .env está no lugar certo**
```
projeto/
├── .env          ← Aqui!
├── script.py
└── ...
```

---

## 11. ❌ Problemas com APIs

### Problema: API não responde ou retorna erro

### Soluções:

**Solução 1: Verificar API key**
```python
import os

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("API key não configurada!")

print(f"API key configurada: {api_key[:10]}...")  # Mostra só primeiros caracteres
```

**Solução 2: Tratamento de erros**
```python
try:
    response = client.chat.completions.create(...)
except Exception as e:
    logging.error(f"Erro na API: {e}")
    logging.error("Verifique:")
    logging.error("1. API key está correta?")
    logging.error("2. Tem créditos/quota?")
    logging.error("3. Internet está funcionando?")
```

**Solução 3: Verificar resposta**
```python
response = client.chat.completions.create(...)

if not response:
    raise Exception("Resposta vazia da API")

if not response.choices:
    raise Exception("Nenhuma escolha na resposta")
```

---

## 12. ❌ Problemas com Encoding (Caracteres Especiais)

### Problema:
```python
UnicodeDecodeError: 'utf-8' codec can't decode byte...
```

### Soluções:

**Solução 1: Especificar encoding**
```python
# ✅ CORRETO
with open("arquivo.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()

# ✅ Para escrita também
with open("arquivo.txt", "w", encoding="utf-8") as f:
    f.write("conteúdo com acentos: ção")
```

**Solução 2: Tratamento de erro**
```python
try:
    with open("arquivo.txt", "r", encoding="utf-8") as f:
        conteudo = f.read()
except UnicodeDecodeError:
    # Tentar outro encoding
    with open("arquivo.txt", "r", encoding="latin-1") as f:
        conteudo = f.read()
```

---

## 13. ❌ Problemas com PDFs

### Problema: Erro ao extrair texto de PDF

### Soluções:

**Solução 1: Verificar se PDF existe**
```python
import os

if not os.path.exists("arquivo.pdf"):
    raise FileNotFoundError("PDF não encontrado!")
```

**Solução 2: Tratamento de erros específicos**
```python
import pdfplumber
from pdfminer.pdfparser import PDFSyntaxError

try:
    with pdfplumber.open("arquivo.pdf") as pdf:
        texto = ""
        for page in pdf.pages:
            texto += page.extract_text()
except PDFSyntaxError:
    logging.error("PDF corrompido ou inválido!")
except PermissionError:
    logging.error("Sem permissão para ler o PDF!")
except Exception as e:
    logging.error(f"Erro ao extrair texto: {e}")
```

---

## 14. ❌ Problemas com Logging

### Problema: Logs não aparecem

### Soluções:

**Solução 1: Configurar logging**
```python
import logging

logging.basicConfig(
    level=logging.INFO,  # Mude para DEBUG para ver tudo
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)

logging.info("Agora deve aparecer!")
```

**Solução 2: Verificar nível**
```python
# Se level=WARNING, INFO não aparece
logging.basicConfig(level=logging.WARNING)  # Só mostra WARNING e acima

# Para ver tudo:
logging.basicConfig(level=logging.DEBUG)  # Mostra tudo
```

---

## 15. ❌ Problemas com PEP 8

### Problema: Muitos erros de formatação

### Soluções:

**Solução 1: Usar autopep8**
```bash
python -m autopep8 --in-place arquivo.py
```

**Solução 2: Verificar com flake8**
```bash
flake8 arquivo.py
```

**Solução 3: Corrigir manualmente**
- Use 4 espaços (não tabs)
- Espaços ao redor de operadores
- Linhas não muito longas (máx 79 caracteres)

---

## 🔍 Como Debugar Problemas

### 1. **Ler a Mensagem de Erro Completa**

```python
# A mensagem de erro mostra:
# 1. Tipo do erro (TypeError, ValueError, etc.)
# 2. Mensagem descritiva
# 3. Linha onde ocorreu
# 4. Stack trace (caminho até o erro)
```

### 2. **Usar print() ou logging para Debug**

```python
# Ver valores de variáveis
print(f"Valor de x: {x}")
print(f"Tipo de x: {type(x)}")

# Ou com logging
logging.debug(f"Valor de x: {x}")
logging.debug(f"Tipo de x: {type(x)}")
```

### 3. **Verificar Tipos**

```python
# Verificar tipo de variável
print(type(variavel))

# Verificar se é None
if variavel is None:
    print("Variável é None!")

# Verificar se tem atributo
if hasattr(objeto, 'atributo'):
    print(objeto.atributo)
```

### 4. **Usar try/except para Capturar Erros**

```python
try:
    # Código que pode dar erro
    resultado = processar_dados()
except Exception as e:
    # Ver detalhes do erro
    logging.error(f"Tipo do erro: {type(e)}")
    logging.error(f"Mensagem: {e}")
    logging.error(f"Detalhes: {e.__class__.__name__}")
```

---

## 📋 Checklist de Troubleshooting

Quando algo não funciona, verifique:

- [ ] Ambiente virtual está ativado?
- [ ] Dependências estão instaladas? (`pip install -r requirements.txt`)
- [ ] Arquivo `.env` existe e tem as variáveis corretas?
- [ ] Caminhos de arquivos estão corretos?
- [ ] Arquivos não estão abertos em outro programa?
- [ ] API keys estão corretas e têm créditos?
- [ ] Python está na versão correta? (`python --version`)
- [ ] Encoding está correto? (utf-8)
- [ ] Logging está configurado?
- [ ] Erros estão sendo tratados com try/except?

---

## 🎯 Resumo dos Erros Mais Comuns

| Erro | Causa Comum | Solução Rápida |
|------|-------------|----------------|
| `ModuleNotFoundError` | Módulo não instalado | `pip install modulo` |
| `FileNotFoundError` | Arquivo não existe | Verificar caminho |
| `PermissionError` | Arquivo aberto/bloqueado | Fechar arquivo |
| `KeyError` | Chave não existe no dict | Usar `.get()` |
| `AttributeError` | Objeto é None | Verificar se não é None |
| `TypeError` | Tipo errado | Converter tipo |
| `ValueError` | Valor inválido | Validar entrada |
| `IndentationError` | Espaços/tabs errados | Usar 4 espaços |
| `SyntaxError` | Sintaxe incorreta | Verificar código |

---

## 💡 Dicas Finais

1. **Sempre leia a mensagem de erro completa** - ela diz exatamente o problema
2. **Use logging** para rastrear o que está acontecendo
3. **Valide entradas** antes de usar
4. **Trate erros** com try/except
5. **Teste incrementalmente** - não escreva tudo de uma vez
6. **Use type hints** para evitar erros de tipo
7. **Verifique documentação** quando não souber como usar algo

---

## 🔍 Troubleshooting Específico dos Scripts (Dia 2, 3 e 4)

### 📝 Dia 2: Gerador de Conteúdo para Blog (`gerador_conteudo_blog.py`)

#### Problema 1: `AttributeError: 'NoneType' object has no attribute 'content'`

**Causa:** A resposta da API pode ser None ou não ter `choices[0].message.content`

**Solução:**
```python
# Linha 71 - Adicionar verificação
resposta = llm_response.choices[0].message.content

# ✅ CORRETO:
if llm_response and llm_response.choices and len(llm_response.choices) > 0:
    resposta = llm_response.choices[0].message.content
else:
    logging.error("Resposta da API inválida ou vazia")
    return None
```

#### Problema 2: `ZeroDivisionError` ao calcular velocidade

**Causa:** `tempo_resposta_ms` pode ser 0 (linha 74)

**Solução:**
```python
# Linha 74 - Adicionar verificação
velocidade = llm_response.usage.total_tokens / (tempo_resposta_ms/1000)

# ✅ CORRETO:
if tempo_resposta_ms > 0:
    velocidade = llm_response.usage.total_tokens / (tempo_resposta_ms/1000)
else:
    velocidade = 0
    logging.warning("Tempo de resposta muito rápido, velocidade não calculada")
```

#### Problema 3: Arquivo não salva (sem erro visível)

**Causa:** Função `salvar_arquivo_tema_blog` retorna `None` mas não propaga erro

**Solução:**
```python
# Linha 84 - Verificar retorno
salvar_arquivo_tema_blog(tema, resposta)

# ✅ CORRETO:
resultado_salvamento = salvar_arquivo_tema_blog(tema, resposta)
if resultado_salvamento is None:
    logging.warning("Arquivo não foi salvo, mas continuando...")
```

#### Problema 4: Nome de arquivo inválido (caracteres especiais no tema)

**Causa:** Tema pode ter caracteres inválidos para nome de arquivo (ex: `/`, `\`, `:`)

**Solução:**
```python
# Linha 115 - Sanitizar nome do arquivo
import re

nome_arquivo = re.sub(r'[<>:"/\\|?*]', '_', tema)  # Substitui caracteres inválidos
caminho_arquivo = f"resultado_blog/{nome_arquivo}.md"
```

---

### 📊 Dia 3: Analisador de Sentimentos (`analisardor_sentimentos.py`)

#### Problema 1: `TypeError: 'NoneType' object is not subscriptable`

**Causa:** `analisar_sentimento_groq` ou `analisar_sentimento_gemini` retornam `None` (linhas 141-142)

**Solução:**
```python
# Linha 141 - Verificar se resultado não é None
resultado_groq, tempo_resposta_ms_groq, tokens_groq = analisar_sentimento_groq(...)

# ✅ CORRETO:
resultado_groq = analisar_sentimento_groq(prompt_analise_sentimento, review)
if resultado_groq is None:
    logging.warning(f"Falha ao analisar review com Groq: {review[:50]}...")
    continue  # Pula para próxima review

resultado_groq, tempo_resposta_ms_groq, tokens_groq = resultado_groq
```

#### Problema 2: `KeyError` ao acessar `resultados_groq[i]['sentimento']`

**Causa:** Se alguma análise falhar, a lista pode ter tamanhos diferentes

**Solução:**
```python
# Linha 262 - Verificar tamanhos antes de iterar
for i in range(len(resultados_groq)):
    # ✅ CORRETO:
    if i >= len(resultados_gemini):
        logging.warning(f"Índice {i} não existe em resultados_gemini")
        break
    
    if 'sentimento' not in resultados_groq[i]:
        logging.warning(f"Review {i} não tem sentimento do Groq")
        continue
```

#### Problema 3: Arquivo `reviews.txt` não encontrado

**Causa:** Arquivo não existe ou caminho incorreto (linha 172)

**Solução:**
```python
# Linha 172 - Verificar se arquivo existe antes de abrir
arquivo = "reviews/reviews.txt"
caminho_completo = os.path.join(diretorio_script, arquivo)

if not os.path.exists(caminho_completo):
    logging.error(f"Arquivo não encontrado: {caminho_completo}")
    logging.error("Crie o arquivo reviews/reviews.txt com uma review por linha")
    return None
```

#### Problema 4: Reviews vazias ou apenas espaços em branco

**Causa:** Arquivo pode ter linhas vazias

**Solução:**
```python
# Linha 179 - Filtrar linhas vazias
reviews = arquivo.readlines()

# ✅ CORRETO:
reviews = [r.strip() for r in arquivo.readlines() if r.strip()]
if not reviews:
    logging.error("Nenhuma review válida encontrada no arquivo!")
    return None
```

#### Problema 5: `AttributeError` ao acessar `response.text` (Gemini)

**Causa:** Resposta do Gemini pode não ter atributo `text` ou ser None

**Solução:**
```python
# Linha 105 - Verificar antes de acessar
sentimento_texto = response.text.strip().lower()

# ✅ CORRETO:
if not response or not hasattr(response, 'text') or not response.text:
    logging.error("Resposta do Gemini inválida ou vazia")
    return None

sentimento_texto = response.text.strip().lower()
```

---

### 📄 Dia 4: Resumidor de PDFs (`resumidor_pdf.py`)

#### Problema 1: `TypeError: 'NoneType' object has no attribute 'split'`

**Causa:** `resumo_groq` ou `resumo_gemini` podem ser `None` (linhas 173-174)

**Solução:**
```python
# Linha 161-162 - Verificar se resumos não são None
resumo_groq = resumir_pdf(texto, caminho_arquivo, "groq")
resumo_gemini = resumir_pdf(texto, caminho_arquivo, "gemini")

# ✅ CORRETO:
resumo_groq = resumir_pdf(texto, caminho_arquivo, "groq")
resumo_gemini = resumir_pdf(texto, caminho_arquivo, "gemini")

if not resumo_groq or not resumo_gemini:
    logging.error("Não foi possível gerar resumos. Verifique as APIs.")
    return None

# Agora pode usar com segurança
comparacao = {
    "groq": {
        "resumo": resumo_groq,
        "comprimento": len(resumo_groq),  # Não vai dar erro
        ...
    }
}
```

#### Problema 2: PDF muito grande (limite de tokens)

**Causa:** PDF pode ter mais texto do que o limite de tokens da API

**Solução:**
```python
# Linha 38 - Limitar tamanho do texto extraído
texto_completo = "\n".join(chunks)

# ✅ CORRETO:
texto_completo = "\n".join(chunks)
# Limitar a ~4000 caracteres (aproximadamente 1000 tokens)
if len(texto_completo) > 4000:
    logging.warning(f"PDF muito grande ({len(texto_completo)} chars). Limitando a 4000 chars.")
    texto_completo = texto_completo[:4000] + "... [texto truncado]"

return texto_completo
```

#### Problema 3: `FileNotFoundError` ao listar PDFs

**Causa:** Pasta `pdfs/` não existe (linha 298)

**Solução:**
```python
# Linha 298 - Verificar se pasta existe
caminho_pasta_pdf = os.path.join(diretorio_script, "pdfs/")

# ✅ CORRETO:
caminho_pasta_pdf = os.path.join(diretorio_script, "pdfs/")
if not os.path.exists(caminho_pasta_pdf):
    logging.error(f"Pasta não encontrada: {caminho_pasta_pdf}")
    logging.error("Crie a pasta 'pdfs/' e adicione arquivos PDF nela")
    return

if not os.listdir(caminho_pasta_pdf):
    logging.warning("Pasta 'pdfs/' está vazia. Adicione arquivos PDF.")
    return
```

#### Problema 4: `AttributeError` ao acessar `response.choices[0]` (Groq)

**Causa:** Resposta pode não ter `choices` ou estar vazia

**Solução:**
```python
# Linha 72 - Verificar estrutura da resposta
resumo = response.choices[0].message.content.strip()

# ✅ CORRETO:
if not response or not hasattr(response, 'choices'):
    logging.error("Resposta do Groq inválida")
    return None

if not response.choices or len(response.choices) == 0:
    logging.error("Resposta do Groq não tem choices")
    return None

if not hasattr(response.choices[0], 'message'):
    logging.error("Resposta do Groq não tem message")
    return None

resumo = response.choices[0].message.content.strip()
```

#### Problema 5: `ImportError` ao importar módulos utilitários

**Causa:** Módulos `util.config` e `util.util` podem não existir (linhas 8-9)

**Solução:**
```python
# Verificar se arquivos existem:
# Semanas/Semana1/Dia4/util/config.py
# Semanas/Semana1/Dia4/util/util.py

# Se não existirem, criar ou usar código inline:
# Em vez de:
# from Semanas.Semana1.Dia4.util.config import criar_llm_response

# Usar diretamente no código ou criar os módulos utilitários
```

#### Problema 6: Divisão por zero ao calcular taxa de compressão

**Causa:** `tamanho_original` pode ser 0 (linha 267)

**Solução:**
```python
# Linha 267 - Já tem verificação, mas pode melhorar
taxa_compressao = (1 - tamanho_resumo / tamanho_original) * 100 if tamanho_original > 0 else 0

# ✅ JÁ ESTÁ CORRETO, mas pode adicionar log:
if tamanho_original == 0:
    logging.warning("Texto original está vazio, taxa de compressão não calculada")
```

---

## 📋 Checklist Específico por Script

### ✅ Dia 2 - Gerador de Conteúdo

- [ ] API key do Groq configurada no `.env`?
- [ ] Pasta `resultado_blog/` será criada automaticamente?
- [ ] Tema não tem caracteres inválidos para nome de arquivo?
- [ ] Resposta da API não é None?
- [ ] Tempo de resposta > 0 antes de calcular velocidade?

### ✅ Dia 3 - Analisador de Sentimentos

- [ ] Arquivo `reviews/reviews.txt` existe?
- [ ] Arquivo tem pelo menos uma review válida (não vazia)?
- [ ] API keys de Groq e Gemini configuradas?
- [ ] Resultados não são None antes de usar?
- [ ] Listas `resultados_groq` e `resultados_gemini` têm mesmo tamanho?

### ✅ Dia 4 - Resumidor de PDFs

- [ ] Pasta `pdfs/` existe e tem arquivos?
- [ ] PDFs não estão corrompidos?
- [ ] PDFs não são muito grandes (limite de tokens)?
- [ ] Módulos `util.config` e `util.util` existem?
- [ ] Resumos não são None antes de calcular métricas?
- [ ] Texto extraído não está vazio?

---

## 🎯 Erros Comuns Específicos por Script

| Script | Erro Comum | Linha | Solução |
|--------|-----------|-------|---------|
| Dia 2 | `AttributeError: 'NoneType'` | 71 | Verificar se `llm_response.choices` existe |
| Dia 2 | `ZeroDivisionError` | 74 | Verificar se `tempo_resposta_ms > 0` |
| Dia 3 | `TypeError: cannot unpack None` | 141 | Verificar se função retorna valor válido |
| Dia 3 | `KeyError: 'sentimento'` | 263 | Verificar se chave existe no dict |
| Dia 3 | `FileNotFoundError` | 172 | Criar arquivo `reviews/reviews.txt` |
| Dia 4 | `TypeError: 'NoneType' split` | 174 | Verificar se resumo não é None |
| Dia 4 | `FileNotFoundError` | 298 | Criar pasta `pdfs/` |
| Dia 4 | `ImportError` | 8-9 | Criar módulos `util.config` e `util.util` |

---

**Última atualização:** 30 Nov 2025


**Status:** 🟡 Em progresso  
**Progresso:** 5/7 dias completos | 5/7 dias criados 

