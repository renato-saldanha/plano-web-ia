# 📅 Dia 7 - Domingo (7 Dez 2025)

## 🎯 Contexto para Agentes IA

Este é o **décimo quarto dia** do plano de 2 meses em Desenvolvimento Web + IA Generativa.

### 📋 O que foi proposto
- **Objetivo do Dia:** Polir o “Knowledge Assistant” criado no Dia 6 com foco em QA rápido, descrições de tools, mensagens de erro mais amigáveis e documentação curta/handoff.
- **Duração estimada:** 2h30-2h40 (160min exatos).
- **Foco:** Testes adicionais (cálculo, RAG, cenários ambíguos), revisão de docstrings das tools e registro de evidências para o handoff.

### 🗺️ Estrutura do Plano
- **Semana 2:** LangChain + RAG (1 Dez - 7 Dez)
- **Dia 6 (concluído):** Projeto integrado em LangGraph com tools + RAG ✅
- **Dia 7 (hoje):** QA, polish e documentação curta do Knowledge Assistant 🟡
- **Dia 8 (próximo):** Início da Semana 3 (FastAPI + IA) — preparar handoff e pré-requisitos

### 📁 Arquivos neste diretório
- `README.md` — Este arquivo (contexto do dia)
- `CONTEXTO_AGENTE.md` — Estado, stack e passos de QA
- `checklist.md` — Checklist 160min
- `journal.md` — Registro do dia (preencher)
- `requirements.txt` — Dependências (mesmas do Dia 6, sem novas)
- `CONTEXTO_PROXIMO_DIA.md` — Handoff para o Dia 8
- `especificacoes.md` — Requisitos de QA/polish (Nível 3)
- `GUIA_CONCEITOS.md` — Conceitos-chave de QA e UX de agent (Nível 3)
- `exercicios.md` — Desafios independentes de QA/polish (Nível 3)

### 🎯 O que você vai aprender/praticar
1. QA rápido de agents com LangChain (`langchain.agents.create_agent`) e ferramentas descritas com clareza.
2. Ajuste de docstrings das tools para reduzir escolhas erradas.
3. Registro de evidências (inputs/outputs) para handoff e reprodutibilidade.

### 💡 Notas Importantes
- **Baseado em:** Dia 4 (RAG com Vector Databases) + Dia 5 (tools/agents) + Dia 6 (LangGraph).
- **Nível de Scaffolding:** **Nível 3 (Avançado)** — conceitos conhecidos, foco em autonomia/QA. Justificativa: aplicação independente sobre agent já funcional (ver `../../GUIAS/GUIA_DECISAO_SCAFFOLDING.md`).
- **Pré-requisitos:** 
  - `.env` com chave do LLM (Groq/OpenAI) e `DATABASE_NAME` configurado
  - PostgreSQL com extensão `pgvector` instalada
  - Tabela `produtos` no banco de dados (veja seção de configuração abaixo)
- **Stack:** Python 3.12 recomendado; LangChain agents (`langchain.agents.create_agent`, `@tool`); PGVector para vector store.

---

## 🔧 Configuração Necessária

### Banco de Dados PostgreSQL

**Requisitos:**
- PostgreSQL com extensão `pgvector` instalada
- Tabela `produtos` com a seguinte estrutura:

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

**Configuração `.env`:**
```env
# API Keys
GROQ_API_KEY=sua_chave_groq
OPENAI_API_KEY=sua_chave_openai

# Banco de Dados PostgreSQL
DATABASE_NAME=postgresql://usuario:senha@localhost:5432/nome_banco
```

**Exemplo:**
```env
DATABASE_NAME=postgresql://postgres:senha@localhost:5432/marketplace
```

### Vector Store

- **Implementação:** PGVector (PostgreSQL com extensão pgvector)
- **Coleção:** "produtos"
- **Indexação:** Automática na primeira execução
  - O sistema verifica se a coleção está vazia
  - Se vazia, lê automaticamente os dados da tabela SQL `produtos`
  - Converte em documentos LangChain e indexa no PGVector
  - Não é necessário executar scripts separados de indexação

---

## 🚀 Funcionalidades Implementadas

### 1. Indexação Automática

O sistema implementa indexação automática de produtos:
- **Função:** `_indexar_produtos_automaticamente()`
- **Comportamento:** Verifica se a coleção PGVector está vazia na primeira execução
- **Processo:**
  1. Conecta ao PostgreSQL
  2. Busca produtos ativos da tabela `produtos`
  3. Converte cada produto em documento LangChain com metadata
  4. Cria embeddings e indexa no PGVector automaticamente
- **Vantagem:** Não requer scripts separados de indexação

### 2. Comparação STUFF vs MapReduce

Implementação completa de comparação entre métodos de processamento:
- **Função:** `comparar_chain_types()`
- **Métodos comparados:**
  - **STUFF:** Processamento direto (mais rápido para poucos chunks)
  - **MapReduce:** Processamento paralelo (melhor para muitos chunks)
- **Métricas:** Tempo de execução e qualidade das respostas
- **Análise:** Quando usar cada abordagem baseado no volume de dados

### 3. Tools Disponíveis

#### `search_knowledges`
- **Propósito:** Busca semântica na coleção de produtos usando PGVector
- **Quando usar:** Perguntas sobre produtos, categorias, preços, estoque
- **Quando NÃO usar:** Cálculos matemáticos, perguntas fora do contexto de produtos
- **Retorno:** Respostas baseadas apenas nos documentos indexados

#### `calculator`
- **Propósito:** Resolve expressões aritméticas simples e intermediárias
- **Quando usar:** Cálculos diretos (ex: "Quanto é 15*2?")
- **Quando NÃO usar:** Perguntas conceituais, consultas sobre produtos
- **Limitação:** Apenas expressões aritméticas simples

### 4. Agent ReAct

- **Função:** `build_agent()` cria agent usando `create_agent`
- **Função:** `execute_agent()` executa com logging completo do raciocínio
- **Recursos:**
  - Escolha automática de tools baseada na pergunta
  - Logging detalhado de todas as decisões (`messages`)
  - Limite de recursão configurável (`recursion_limit: 10`)

### 5. Sistema de LLMs

- **Suporte:** Groq (Llama 3.1 8B) e OpenAI (GPT-4o-mini)
- **Função:** `model_changed()` permite alternar entre modelos
- **Configuração:** Via variáveis de ambiente no `.env`

---

## 📝 Estrutura do Código Implementado

### Arquivo Principal: `exercicios/1-rag_completo.py`

#### Funções Principais

**Configuração:**
- `load_retriever()`: Carrega retriever PGVector com verificação e indexação automática
- `_indexar_produtos_automaticamente()`: Indexa produtos da tabela SQL no PGVector

**Tools:**
- `search_knowledges()`: Tool para busca RAG com PGVector
- `calculator()`: Tool para cálculos aritméticos

**Agent:**
- `build_agent()`: Cria agent ReAct com tools configuradas
- `execute_agent()`: Executa agent com logging completo

**Processamento:**
- `map_reduce_parallel()`: Implementa MapReduce para processamento paralelo de chunks
- `comparar_chain_types()`: Compara STUFF vs MapReduce com métricas

**Utilitários:**
- `model_changed()`: Alterna entre modelos LLM (Groq/OpenAI)

### Fluxo de Execução

1. **Inicialização:**
   - Carrega variáveis de ambiente (`.env`)
   - Conecta ao PostgreSQL via PGVector
   - Verifica se coleção está vazia → indexa automaticamente se necessário

2. **Processamento de Pergunta:**
   - Agent analisa a pergunta
   - Escolhe tool apropriada (`search_knowledges` ou `calculator`)
   - Executa tool e retorna resposta
   - Logging completo do raciocínio

3. **Comparação (opcional):**
   - Executa mesma pergunta com STUFF e MapReduce
   - Compara tempo e qualidade
   - Gera relatório de análise

---

## 🧪 Como Usar

### Execução Básica

```python
python exercicios/1-rag_completo.py
```

Isso executará `comparar_chain_types()` que:
- Testa múltiplas perguntas
- Compara STUFF vs MapReduce
- Gera relatório de performance

### Uso Programático

```python
from exercicios.1_rag_completo import execute_agent, load_retriever

# Executar agent com pergunta
resposta = execute_agent("Me liste os produtos disponíveis.")
print(resposta)

# Usar retriever diretamente
retriever = load_retriever()
docs = retriever.invoke("notebook")
```

### Verificação de Indexação

Na primeira execução, você verá mensagens como:
```
DEBUG: Conectando ao banco: localhost:5432/marketplace
DEBUG: Coleção: produtos
Coleção vazia detectada. Indexando produtos automaticamente...
📦 Encontrados 26 produtos na tabela SQL
🔄 Criando embeddings e indexando... (isso pode demorar alguns minutos)
✅ Indexação concluída! 26 produtos indexados.
```

---

## 🔗 Referências
- Plano completo: `../../1-Plano_Desenvolvimento.md`
- Metodologia: `../../METODOLOGIA_ENSINO.md`
- Scaffolding: `../../GUIAS/GUIA_DECISAO_SCAFFOLDING.md`
- Dia 4: `../Dia4/GUIA_RAG_AVANCADO.md` (conceitos de RAG e vector stores)
- Dia 5: `../Dia5/GUIA_AGENTS.md` (tools e agents)
- Dia 6: `GUIA_APRENDIZADO.md`, `template.py`, `exemplo_referencia.py`, `exercicios.md`
- LangGraph Docs: https://python.langchain.com/docs/langgraph
- LangChain Overview: https://docs.langchain.com/oss/python/langchain/overview
- PGVector Docs: https://python.langchain.com/docs/integrations/vectorstores/pgvector

---

## ⚠️ Diferenças em Relação ao Planejado

**Mudança Principal:** Migração de FAISS para PGVector
- **Planejado:** Usar FAISS indexado em `../Dia4/faiss_index`
- **Implementado:** PGVector com PostgreSQL para persistência em banco de dados
- **Motivo:** Melhor integração com dados SQL existentes e indexação automática
- **Impacto:** Requer configuração de PostgreSQL, mas oferece mais flexibilidade

**Adição:** Comparação STUFF vs MapReduce
- **Não planejado originalmente**
- **Implementado:** Sistema completo de comparação com métricas
- **Benefício:** Entendimento prático de quando usar cada método

---

**Status:** ✅ Implementado  
**Última atualização:** 7 Dez 2025

