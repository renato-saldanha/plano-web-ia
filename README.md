# 📚 Plano de Desenvolvimento Web + IA Generativa

> **Plano de desenvolvimento de 2 meses focado em Desenvolvimento Web + IA Generativa, criando scripts práticos de automação e aplicações profissionais.**

![Python](https://img.shields.io/badge/python-3.12+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![GitHub followers](https://img.shields.io/github/followers/renato-saldanha?style=social&label=Followers)
![GitHub stars](https://img.shields.io/github/stars/renato-saldanha/plano-web-ia?style=social&label=Stars)
![GitHub forks](https://img.shields.io/github/forks/renato-saldanha/plano-web-ia?style=social&label=Forks)

## 📊 Estatísticas do GitHub

<div align="center">
  <img height="180em" src="https://github-readme-stats.vercel.app/api?username=renato-saldanha&show_icons=true&theme=dark&include_all_commits=true&count_private=true&hide_border=true&bg_color=0D1117"/>
  <img height="180em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=renato-saldanha&layout=compact&langs_count=6&theme=dark&hide_border=true&bg_color=0D1117"/>
</div>

<div align="center">
  <img src="https://github-readme-streak-stats.demolab.com/?user=renato-saldanha&theme=dark&hide_border=true&background=0D1117" alt="GitHub Streak"/>
</div>

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
- [Criando Novos Dias](#️-criando-novos-dias)
- [Licença](#-licença)

---

## 🎯 Descrição

Este projeto é um plano de desenvolvimento de 2 meses focado em Desenvolvimento Web + IA Generativa. Durante a primeira semana, foram criados scripts de automação utilizando diferentes LLMs (Large Language Models) para tarefas práticas.

**Objetivos:**
- Aprender fundamentos de IA Generativa
- Criar scripts práticos de automação
- Comparar diferentes LLMs (Groq, Gemini, Claude)
- Desenvolver habilidades em Python e APIs
- Construir aplicações profissionais com frameworks modernos

**Metodologia:**
O projeto segue uma metodologia de ensino baseada em Scaffolding e Progressive Disclosure, garantindo aprendizado efetivo através de prática guiada e progressiva.

---

## ✨ Funcionalidades

### Semana 1 - Fundamentos de IA Generativa ✅

#### 1. Gerador de Conteúdo para Blog
- **Script:** `Semanas/Semana1/Dia2/gerador_conteudo_blog.py`
- **Descrição:** Gera conteúdo completo para blog sobre qualquer tema usando Groq API
- **Features:**
  - Geração de conteúdo estruturado
  - Salvamento automático em Markdown
  - Métricas de performance (tempo, tokens)
- **Uso:**
  ```bash
  python Semanas/Semana1/Dia2/gerador_conteudo_blog.py
  ```

#### 2. Analisador de Sentimentos
- **Script:** `Semanas/Semana1/Dia3/analisador_sentimentos.py`
- **Descrição:** Analisa sentimentos de reviews comparando 3 LLMs diferentes (Groq, Gemini, Claude)
- **Features:**
  - Análise comparativa de múltiplos LLMs
  - Métricas de concordância entre modelos
  - Geração de relatórios em Markdown
- **Uso:**
  ```bash
  python Semanas/Semana1/Dia3/analisador_sentimentos.py
  ```

#### 3. Resumidor de PDFs
- **Script:** `Semanas/Semana1/Dia4/resumidor_pdf.py`
- **Descrição:** Extrai texto de PDFs e gera resumos usando diferentes LLMs
- **Features:**
  - Extração de texto com pdfplumber
  - Resumos comparativos de múltiplos LLMs
  - Métricas de compressão e qualidade
- **Uso:**
  ```bash
  python Semanas/Semana1/Dia4/resumidor_pdf.py
  ```

#### 4. CLI Integrado
- **Script:** `Semanas/Semana1/Dia6/cli_automatizacoes.py`
- **Descrição:** Interface de linha de comando unificando todos os scripts anteriores
- **Features:**
  - Menu interativo
  - Comandos individuais para cada funcionalidade
  - Tratamento de erros robusto
- **Uso:**
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

## 🚀 Instalação

### Pré-requisitos

- Python 3.12 ou superior
- Contas nas APIs:
  - [Groq](https://console.groq.com/) (gratuita)
  - [Google Gemini](https://makersuite.google.com/app/apikey) (gratuita)
  - [Anthropic Claude](https://console.anthropic.com/) (pode ter custo)

### Passo 1: Clonar Repositório

```bash
git clone https://github.com/renato-saldanha/plano-web-ia.git
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
# API Keys
GROQ_API_KEY=sua_chave_groq_aqui
GEMINI_API_KEY=sua_chave_gemini_aqui
ANTHROPIC_API_KEY=sua_chave_anthropic_aqui
OPENAI_API_KEY=sua_chave_openai_aqui

# Banco de Dados (para Semana 2+)
DATABASE_NAME=postgresql://usuario:senha@localhost:5432/nome_banco
```

**⚠️ IMPORTANTE:** Nunca commite o arquivo `.env`! Ele está no `.gitignore`.

### Passo 5: Configurar PostgreSQL (Semana 2+)

Para usar funcionalidades da Semana 2 (RAG com PGVector):

1. **Instalar PostgreSQL:**
   - [Download PostgreSQL](https://www.postgresql.org/download/)

2. **Instalar extensão pgvector:**
   ```sql
   CREATE EXTENSION IF NOT EXISTS vector;
   ```

3. **Criar tabela produtos (para exemplo do Dia 7):**
   ```sql
   CREATE TABLE produtos (
       id SERIAL PRIMARY KEY,
       nome TEXT NOT NULL,
       descricao TEXT,
       preco NUMERIC(10, 2),
       estoque INTEGER,
       categoria TEXT,
       sku TEXT,
       ativo BOOLEAN DEFAULT true,
       criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
       atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
   ```

### Passo 6: Verificar Instalação

**Teste Semana 1:**
```bash
python Semanas/Semana1/Dia1/hello_ai_groq.py
```

**Teste Semana 2 (requer PostgreSQL):**
```bash
python Semanas/Semana2/Dia7/exercicios/1-rag_completo.py
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
    ├── Semana1/                 # Fundamentos de IA Generativa
    │   ├── README.md
    │   ├── Dia1/                # Setup APIs
    │   │   ├── hello_ai_groq.py
    │   │   └── ...
    │   ├── Dia2/                # Gerador de conteúdo
    │   │   ├── gerador_conteudo_blog.py
    │   │   └── ...
    │   ├── Dia3/                # Analisador de sentimentos
    │   │   ├── analisador_sentimentos.py
    │   │   └── ...
    │   ├── Dia4/                # Resumidor de PDFs
    │   │   ├── resumidor_pdf.py
    │   │   └── ...
    │   ├── Dia5/                # Refatoração
    │   ├── Dia6/                # CLI integrado
    │   │   ├── cli_automatizacoes.py
    │   │   └── ...
    │   └── Dia7/                # Deploy + Review
    │
    └── Semana2/                 # LangChain + RAG
        ├── README.md
        ├── Dia1-3/              # Fundamentos LangChain
        ├── Dia4/                # RAG Avançado (FAISS/Chroma)
        ├── Dia5/                # Agents
        ├── Dia6/                # LangGraph
        └── Dia7/                # Knowledge Assistant Completo
            ├── exercicios/
            │   └── 1-rag_completo.py  # Sistema RAG com PGVector
            └── ...
```

---

## 🛠️ Tecnologias Utilizadas

### Linguagens
- **Python 3.12+** - Linguagem principal

### Bibliotecas Python
- **groq** - API do Groq para LLMs
- **google-generativeai** - API do Google Gemini
- **anthropic** - API do Anthropic Claude
- **langchain** - Framework para aplicações com LLMs
- **langchain-groq** - Integração LangChain com Groq
- **langchain-openai** - Integração LangChain com OpenAI
- **langchain-postgres** - Vector store PGVector para PostgreSQL
- **langchain-huggingface** - Embeddings com HuggingFace
- **python-dotenv** - Gerenciamento de variáveis de ambiente
- **pdfplumber** - Extração de texto de PDFs
- **psycopg2** - Driver PostgreSQL para Python
- **argparse** - Criação de CLI (built-in)

### APIs Externas
- [Groq API](https://console.groq.com/) - LLM rápido e gratuito
- [Google Gemini API](https://makersuite.google.com/app/apikey) - LLM do Google
- [Anthropic Claude API](https://console.anthropic.com/) - LLM da Anthropic
- [OpenAI API](https://platform.openai.com/) - GPT models

### Banco de Dados
- **PostgreSQL** - Banco de dados relacional
- **pgvector** - Extensão PostgreSQL para vector similarity search

### Ferramentas
- **Git** - Controle de versão
- **GitHub** - Hospedagem de código
- **Markdown** - Documentação

---

## 📅 Semana 1

### O que foi feito:

**Dia 1 - Setup APIs** ✅
- Configuração de ambiente Python
- Setup de APIs (Groq, Gemini, Claude)
- Primeiro script "Hello AI"

**Dia 2 - Gerador de Conteúdo** ✅
- Script para gerar conteúdo de blog
- Integração com Groq API
- Salvamento automático de resultados

**Dia 3 - Analisador de Sentimentos** ✅
- Comparação de 3 LLMs diferentes
- Análise de sentimentos de reviews
- Métricas de performance (tempo, tokens)

**Dia 4 - Resumidor de PDFs** ✅
- Extração de texto de PDFs
- Geração de resumos com múltiplos LLMs
- Comparação de resultados

**Dia 5 - Refatoração** ✅
- Melhoria de código
- Tratamento de erros
- Documentação

**Dia 6 - CLI Integrado** ✅
- Interface de linha de comando unificada
- Menu interativo
- Integração de todos os scripts anteriores

**Dia 7 - Deploy + Review** ✅
- Documentação completa
- Deploy no GitHub
- Review da semana

### Estatísticas da Semana:
- **Scripts criados:** 5
- **LLMs testados:** 3 (Groq, Gemini, Claude)
- **Linhas de código:** ~2000+
- **Tempo estimado:** ~30-40 horas
- **Status:** ✅ Completa

---

## 📅 Semana 2 - LangChain + RAG ✅

### O que foi feito:

**Dia 1-3 - Fundamentos LangChain** ✅
- Introdução ao LangChain e LCEL (LangChain Expression Language)
- Criação de chains básicas
- Integração com múltiplos LLMs (Groq, OpenAI)

**Dia 4 - RAG Avançado** ✅
- Vector databases (FAISS, Chroma)
- Embeddings com HuggingFace
- Busca semântica e retrieval

**Dia 5 - Agents** ✅
- Criação de tools com `@tool`
- Agents ReAct com LangChain
- Integração de múltiplas ferramentas

**Dia 6 - LangGraph** ✅
- Orquestração de workflows complexos
- Integração de agents com RAG

**Dia 7 - Knowledge Assistant Completo** ✅
- Sistema RAG completo com PGVector
- Indexação automática de produtos do PostgreSQL
- Comparação STUFF vs MapReduce
- Agent ReAct com múltiplas tools

### Funcionalidades Principais da Semana 2:

#### 1. Sistema RAG com PGVector
- **Script:** `Semanas/Semana2/Dia7/exercicios/1-rag_completo.py`
- **Descrição:** Sistema completo de RAG usando PostgreSQL com extensão pgvector
- **Features:**
  - Indexação automática de produtos da tabela SQL
  - Busca semântica com embeddings
  - Comparação de métodos STUFF vs MapReduce
  - Agent ReAct com tools integradas
- **Uso:**
  ```bash
  python Semanas/Semana2/Dia7/exercicios/1-rag_completo.py
  ```

#### 2. Tools e Agents
- **Tools disponíveis:**
  - `search_knowledges`: Busca semântica na base de conhecimento
  - `calculator`: Resolução de expressões aritméticas
- **Agent ReAct:** Escolha automática de tools baseada na pergunta

### Estatísticas da Semana 2:
- **Scripts criados:** 10+
- **Vector stores testados:** FAISS, Chroma, PGVector
- **Agents criados:** 3+
- **Status:** ✅ Completa

---

## 🎯 Próximos Passos

### Semana 3: FastAPI + Backend 🟡
- Criação de APIs REST
- Endpoints para automações
- Autenticação e segurança
- Integração com sistemas de IA

### Semana 4-8: [Continuar conforme plano]
- Bun + Hono
- NextJS Frontend
- Projeto Final

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

## 🛠️ Criando Novos Dias

Se você fez fork deste projeto e deseja criar novos dias seguindo a metodologia do plano, este guia explica como fazer isso.

### 📋 Visão Geral

O projeto utiliza uma metodologia de ensino baseada em **Scaffolding** e **Progressive Disclosure**, onde cada dia segue uma estrutura padronizada de 160 minutos (2h40) dividida em fases específicas.

### 📚 Documentos Essenciais

Antes de criar um novo dia, leia os seguintes documentos na raiz do projeto:

1. **`CONTEXTO_CRIACAO_DIA.md`** ⭐ - **LEIA PRIMEIRO**
   - Instruções completas para agentes IA criarem novos dias
   - Define a metodologia e estrutura obrigatória
   - Especifica os arquivos necessários e níveis de scaffolding

2. **`METODOLOGIA_ENSINO.md`**
   - Explica a metodologia de ensino aplicada
   - Detalha os níveis de scaffolding (1, 2, 3)
   - Define a estrutura padrão de um dia

3. **`TEMPLATE_ESTRUTURA_DIA.md`**
   - Template completo com exemplos de cada arquivo
   - Estrutura de pastas e nomenclatura
   - Exemplos de código para cada nível de scaffolding

4. **`GUIAS/GUIA_DECISAO_SCAFFOLDING.md`**
   - Matriz de decisão para escolher o nível de scaffolding
   - Exemplos práticos de quando usar cada nível
   - Checklist de decisão

5. **`1-Plano_Desenvolvimento.md`**
   - Plano macro completo do projeto
   - Contexto de cada semana e dia
   - Sequência lógica de aprendizado

### 🎯 Processo de Criação

#### Passo 1: Entender o Contexto

1. Leia o **`CONTEXTO_PROXIMO_DIA.md`** do dia anterior
   - Este arquivo contém o briefing obrigatório para criar o próximo dia
   - Explica o que foi aprendido e o que será feito no próximo dia

2. Revise o **`journal.md`** do dia anterior (opcional)
   - Identifica dificuldades enfrentadas
   - Ajuda a ajustar o nível de scaffolding se necessário

#### Passo 2: Definir Estrutura do Dia

Cada dia deve ter os seguintes arquivos **obrigatórios** (na ordem especificada):

```
DiaX/
├── README.md                    # Contexto e objetivos do dia
├── CONTEXTO_AGENTE.md           # Informações técnicas detalhadas
├── checklist.md                 # Tarefas práticas divididas em fases
├── journal.md                   # Template para reflexão
├── requirements.txt             # Dependências Python (obrigatório, mesmo que vazio)
└── CONTEXTO_PROXIMO_DIA.md      # Guia para construir próximo dia (obrigatório)
```

**Arquivos adicionais** conforme o nível de scaffolding:

- **Nível 1 (Iniciante):** `exemplo_completo.py`, `GUIA_PASSO_A_PASSO.md`
- **Nível 2 (Intermediário):** `template.py`, `GUIA_APRENDIZADO.md`, `exemplo_referencia.py`, `exercicios.md`
- **Nível 3 (Avançado):** `especificacoes.md`, `GUIA_CONCEITOS.md`, `exercicios.md`

#### Passo 3: Seguir a Estrutura de Tempo

Cada dia deve ter exatamente **160 minutos** (2h40) divididos em:

| Fase | Duração | Descrição |
|------|---------|-----------|
| **Preparação** | 5min | Abrir checklist, revisar README.md, validar ambiente |
| **Leitura guiada** | 20min | Ler guias/documentos do dia, destacar pontos-chave |
| **Construção guiada** | 90min | Trabalhar no template.py, exercícios ou código principal |
| **Consolidação** | 25min | Testes rápidos, refino e checklist parcial |
| **Registro/handoff** | 20min | Checklist final, journal, CONTEXTO_PROXIMO_DIA.md |
| **Buffer** | 10min | Resolver imprevistos ou mover item para próximo dia |

**⚠️ IMPORTANTE:** Se alguma atividade exceder 160 minutos, divida em um novo dia.

#### Passo 4: Usar Agentes IA (Recomendado)

O arquivo **`CONTEXTO_CRIACAO_DIA.md`** foi criado especificamente para ser usado com agentes IA (como Cursor, Claude, ChatGPT). 

**Como usar:**

1. Abra o arquivo `CONTEXTO_CRIACAO_DIA.md` no seu agente IA
2. Forneça o contexto do dia anterior (leia `CONTEXTO_PROXIMO_DIA.md`)
3. O agente seguirá as instruções e criará todos os arquivos necessários
4. Revise e ajuste conforme necessário

**Exemplo de prompt para agente IA:**

```
Usando o CONTEXTO_CRIACAO_DIA.md como guia, crie o Dia 5 da Semana 3.
Leia primeiro o Semanas/Semana3/Dia4/CONTEXTO_PROXIMO_DIA.md para entender o contexto.
```

### 📝 Checklist de Criação

Antes de considerar um dia completo, verifique:

- [ ] Todos os arquivos obrigatórios foram criados
- [ ] `README.md` tem objetivo claro e duração de 160min
- [ ] `checklist.md` está dividido nas 6 fases (totalizando 160min)
- [ ] `CONTEXTO_PROXIMO_DIA.md` foi criado (obrigatório para todos os dias)
- [ ] Nível de scaffolding foi definido e justificado
- [ ] Arquivos do scaffolding correspondem ao nível escolhido
- [ ] Referências aos guias estão explícitas no checklist
- [ ] `requirements.txt` foi criado (mesmo que vazio)
- [ ] Código segue padrões do projeto (PEP 8 para Python)

### 🎓 Níveis de Scaffolding

**⚠️ IMPORTANTE:** Os níveis são determinados pelo **CONCEITO**, não pela posição temporal.

- **Nível 1:** Conceito completamente novo, primeira exposição
- **Nível 2:** Conceito parcialmente conhecido, aplicação em novo contexto
- **Nível 3:** Conceitos conhecidos, aplicação independente

**Exemplo:**
- Semana 1, Dia 1: Nível 1 (conceito novo: usar APIs diretamente)
- Semana 2, Dia 1: Nível 1 (conceito novo: LangChain)
- Semana 2, Dia 2: Nível 2 (conceito parcialmente conhecido: já sabe LangChain básico)

### 🔗 Recursos Adicionais

- **Estrutura de exemplo:** Veja `Semanas/Semana3/Dia4/` como referência completa
- **Templates:** Use `TEMPLATE_ESTRUTURA_DIA.md` como base
- **Metodologia:** Consulte `METODOLOGIA_ENSINO.md` para entender a filosofia

### 💡 Dicas

1. **Sempre leia o `CONTEXTO_PROXIMO_DIA.md` do dia anterior** antes de criar um novo dia
2. **Use agentes IA** para acelerar a criação seguindo `CONTEXTO_CRIACAO_DIA.md`
3. **Mantenha consistência** com a estrutura dos dias anteriores
4. **Teste o checklist** para garantir que cabe em 160 minutos
5. **Crie o `CONTEXTO_PROXIMO_DIA.md`** no final de cada dia (obrigatório)

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

## 👤 Autor

**Renato Saldanha**
- GitHub: [@renato-saldanha](https://github.com/renato-saldanha)
- Repositório: [plano-web-ia](https://github.com/renato-saldanha/plano-web-ia)

---

## 🙏 Agradecimentos

- [Groq](https://groq.com/) por API gratuita e rápida
- [Google](https://ai.google.dev/) por Gemini API
- [Anthropic](https://www.anthropic.com/) por Claude API
- Comunidade Python por excelentes bibliotecas

---

**Última atualização:** 7 Dez 2025

