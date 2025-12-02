# 📚 [Nome do Projeto]

> **Descrição breve e impactante do projeto em uma linha**

[Badges opcionais - adicione se quiser]
![Python](https://img.shields.io/badge/python-3.12+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## 📋 Índice

- [Descrição](#-descrição)
- [Funcionalidades](#-funcionalidades)
- [Instalação](#-instalação)
- [Uso](#-uso)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Semana 1](#-semana-1)
- [Próximos Passos](#-próximos-passos)
- [Contribuindo](#-contribuindo)
- [Licença](#-licença)

---

## 🎯 Descrição

**TODO: Preencher com descrição completa do projeto**

Este projeto é um plano de desenvolvimento de 2 meses focado em Desenvolvimento Web + IA Generativa. Durante a primeira semana, foram criados scripts de automação utilizando diferentes LLMs (Large Language Models) para tarefas práticas.

**Objetivos:**
- Aprender fundamentos de IA Generativa
- Criar scripts práticos de automação
- Comparar diferentes LLMs (Groq, Gemini, Claude)
- Desenvolver habilidades em Python e APIs

---

## ✨ Funcionalidades

### Semana 1 - Fundamentos de IA Generativa

**TODO: Listar todas as funcionalidades criadas**

#### 1. Gerador de Conteúdo para Blog
- **Script:** `Semanas/Semana1/Dia2/gerador_conteudo_blog.py`
- **Descrição:** Gera conteúdo completo para blog sobre qualquer tema usando Groq API
- **Uso:**
  ```python
  python Semanas/Semana1/Dia2/gerador_conteudo_blog.py
  ```

#### 2. Analisador de Sentimentos
- **Script:** `Semanas/Semana1/Dia3/analisador_sentimentos.py`
- **Descrição:** Analisa sentimentos de reviews comparando 3 LLMs diferentes (Groq, Gemini, Claude)
- **Uso:**
  ```python
  python Semanas/Semana1/Dia3/analisador_sentimentos.py
  ```

#### 3. Resumidor de PDFs
- **Script:** `Semanas/Semana1/Dia4/resumidor_pdf.py`
- **Descrição:** Extrai texto de PDFs e gera resumos usando diferentes LLMs
- **Uso:**
  ```python
  python Semanas/Semana1/Dia4/resumidor_pdf.py
  ```

#### 4. CLI Integrado
- **Script:** `Semanas/Semana1/Dia6/cli_automatizacoes.py`
- **Descrição:** Interface de linha de comando unificando todos os scripts anteriores
- **Uso:**
  ```bash
  python Semanas/Semana1/Dia6/cli_automatizacoes.py blog --tema "Python"
  python Semanas/Semana1/Dia6/cli_automatizacoes.py sentimentos --arquivo reviews.txt
  python Semanas/Semana1/Dia6/cli_automatizacoes.py resumir --pdf arquivo.pdf --llm groq
  python Semanas/Semana1/Dia6/cli_automatizacoes.py  # Menu interativo
  ```

---

## 🚀 Instalação

### Pré-requisitos

- Python 3.12 ou superior
- Contas nas APIs:
  - [Groq](https://console.groq.com/) (gratuita)
  - [Google Gemini](https://makersuite.google.com/app/apikey) (gratuita)
  - [Anthropic Claude](https://console.anthropic.com/) (pode ter custo)

### Passo 1: Clonar Repositório

```bash
git clone https://github.com/seu-usuario/plano-web-ia.git
cd plano-web-ia
```

### Passo 2: Criar Ambiente Virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### Passo 3: Instalar Dependências

```bash
pip install -r requirements.txt
```

**Ou instalar manualmente:**

```bash
pip install groq google-generativeai anthropic python-dotenv pdfplumber
```

### Passo 4: Configurar Variáveis de Ambiente

Crie arquivo `.env` na raiz do projeto:

```env
GROQ_API_KEY=sua_chave_groq_aqui
GEMINI_API_KEY=sua_chave_gemini_aqui
ANTHROPIC_API_KEY=sua_chave_anthropic_aqui
```

**⚠️ IMPORTANTE:** Nunca commite o arquivo `.env`! Ele está no `.gitignore`.

### Passo 5: Verificar Instalação

```bash
python Semanas/Semana1/Dia1/hello_ai_groq.py
```

Se funcionar, instalação está completa! ✅

---

## 💻 Uso

### Exemplo 1: Gerar Conteúdo para Blog

```python
# Edite Semanas/Semana1/Dia2/gerador_conteudo_blog.py
# Na função main(), altere o tema:

if __name__ == "__main__":
    tema = "Inteligência Artificial"
    resultado = gerar_conteudo_tema(tema)
    print(resultado)
```

Execute:
```bash
python Semanas/Semana1/Dia2/gerador_conteudo_blog.py
```

### Exemplo 2: Analisar Sentimentos

1. Adicione reviews em `Semanas/Semana1/Dia3/reviews/reviews.txt`:
   ```
   ## Review 1 - Produto excelente, recomendo!
   ## Review 2 - Não gostei, qualidade ruim.
   ```

2. Execute:
```bash
python Semanas/Semana1/Dia3/analisador_sentimentos.py
```

### Exemplo 3: Resumir PDF

1. Adicione PDF em `Semanas/Semana1/Dia4/pdfs/`

2. Execute:
```bash
python Semanas/Semana1/Dia4/resumidor_pdf.py
```

### Exemplo 4: Usar CLI Integrado

```bash
# Gerar conteúdo
python Semanas/Semana1/Dia6/cli_automatizacoes.py blog --tema "Python"

# Analisar sentimentos
python Semanas/Semana1/Dia6/cli_automatizacoes.py sentimentos --arquivo reviews/reviews.txt

# Resumir PDF
python Semanas/Semana1/Dia6/cli_automatizacoes.py resumir --pdf pdfs/arquivo.pdf --llm groq

# Menu interativo
python Semanas/Semana1/Dia6/cli_automatizacoes.py
```

---

## 📁 Estrutura do Projeto

```
plano-web-ia/
├── README.md                    # Este arquivo
├── .gitignore                   # Arquivos ignorados pelo Git
├── .env                         # Variáveis de ambiente (não versionado)
├── requirements.txt             # Dependências Python
│
├── METODOLOGIA_ENSINO.md        # Metodologia do projeto
├── README_ESTRUTURA_PROJETO.md  # Estrutura e navegação
├── TEMPLATE_ESTRUTURA_DIA.md    # Template para criar novos dias
│
├── GUIAS/                       # Guias de aprendizado
│   ├── GUIA_CLI.md
│   ├── GUIA_DEPLOY.md
│   └── ...
│
└── Semanas/
    └── Semana1/
        ├── README.md            # Visão geral da semana
        ├── Dia1/                # Setup APIs
        │   ├── hello_ai_groq.py
        │   └── ...
        ├── Dia2/                # Gerador de conteúdo
        │   ├── gerador_conteudo_blog.py
        │   └── ...
        ├── Dia3/                # Analisador de sentimentos
        │   ├── analisador_sentimentos.py
        │   └── ...
        ├── Dia4/                # Resumidor de PDFs
        │   ├── resumidor_pdf.py
        │   └── ...
        ├── Dia5/                # Refatoração
        ├── Dia6/                # CLI integrado
        │   ├── cli_automatizacoes.py
        │   └── ...
        └── Dia7/                # Deploy + Review
```

---

## 🛠️ Tecnologias Utilizadas

### Linguagens
- **Python 3.12+** - Linguagem principal

### Bibliotecas Python
- **groq** - API do Groq para LLMs
- **google-generativeai** - API do Google Gemini
- **anthropic** - API do Anthropic Claude
- **python-dotenv** - Gerenciamento de variáveis de ambiente
- **pdfplumber** - Extração de texto de PDFs
- **argparse** - Criação de CLI (built-in)

### APIs Externas
- [Groq API](https://console.groq.com/) - LLM rápido e gratuito
- [Google Gemini API](https://makersuite.google.com/app/apikey) - LLM do Google
- [Anthropic Claude API](https://console.anthropic.com/) - LLM da Anthropic

### Ferramentas
- **Git** - Controle de versão
- **GitHub** - Hospedagem de código
- **Markdown** - Documentação

---

## 📅 Semana 1

### O que foi feito:

**Dia 1 - Setup APIs**
- Configuração de ambiente Python
- Setup de APIs (Groq, Gemini, Claude)
- Primeiro script "Hello AI"

**Dia 2 - Gerador de Conteúdo**
- Script para gerar conteúdo de blog
- Integração com Groq API
- Salvamento automático de resultados

**Dia 3 - Analisador de Sentimentos**
- Comparação de 3 LLMs diferentes
- Análise de sentimentos de reviews
- Métricas de performance (tempo, tokens)

**Dia 4 - Resumidor de PDFs**
- Extração de texto de PDFs
- Geração de resumos com múltiplos LLMs
- Comparação de resultados

**Dia 5 - Refatoração**
- Melhoria de código
- Tratamento de erros
- Documentação

**Dia 6 - CLI Integrado**
- Interface de linha de comando unificada
- Menu interativo
- Integração de todos os scripts anteriores

**Dia 7 - Deploy + Review**
- Documentação completa
- Deploy no GitHub
- Review da semana

### Estatísticas da Semana:
- **Scripts criados:** 5
- **LLMs testados:** 3 (Groq, Gemini, Claude)
- **Linhas de código:** ~2000+
- **Tempo estimado:** ~30-40 horas

---

## 🎯 Próximos Passos

### Semana 2: LangChain + RAG
- Introdução ao LangChain
- Criação de chains
- Retrieval-Augmented Generation (RAG)
- Integração com vector databases

### Semana 3: FastAPI + Backend
- Criação de APIs REST
- Endpoints para automações
- Autenticação e segurança

### Semana 4-8: [Continuar conforme plano]

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'feat: adiciona AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

**Padrões:**
- Siga PEP 8 para código Python
- Use mensagens de commit descritivas
- Adicione documentação para novas features
- Teste antes de fazer commit

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

## 👤 Autor

**Seu Nome**
- GitHub: [@seu-usuario](https://github.com/seu-usuario)
- Email: seu@email.com

---

## 🙏 Agradecimentos

- [Groq](https://groq.com/) por API gratuita e rápida
- [Google](https://ai.google.dev/) por Gemini API
- [Anthropic](https://www.anthropic.com/) por Claude API
- Comunidade Python por excelentes bibliotecas

---

**Última atualização:** 30 Nov 2025

---

## 📝 Notas

**TODO: Adicionar notas adicionais se necessário**

Este README é um template. Preencha todas as seções marcadas com **TODO** antes de fazer commit.

