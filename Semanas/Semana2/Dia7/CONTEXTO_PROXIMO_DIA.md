# 🎯 Contexto para Construir o Dia 8

## 📚 O que aprendemos hoje (Dia 7)
- Reforço de docstrings/prompt das tools do Knowledge Assistant (calculator + RAG FAISS).
- Smoke tests adicionais (cálculo, RAG conceitual, pergunta mista, entrada ambígua).
- Melhoria de mensagens de erro e registro de evidências para handoff.

### Habilidades desenvolvidas
- QA rápido em agents LangChain (`langchain.agents.create_agent`, `@tool`), interpretando `messages`.
- Polimento de UX/erros e documentação breve de uso.

### Código/Artefatos usados
- `../Dia6/template.py` e `exemplo_referencia.py` (ajustes de docstrings/prompt).
- `../Dia4/faiss_index` (retriever).
- `exercicios.md` (smoke tests) e `especificacoes.md` (critérios de QA).

---

## 🔗 Por que o Dia 8 é importante
- Marca início da Semana 3: Backend FastAPI + IA (conceito novo → provável Nível 1).
- Precisamos de ambiente web para servir o assistant e preparar autenticação/segurança.
- Prepara transição do protótipo CLI/agent para uma API utilizável.

---

## 🎯 O que será feito no Dia 8
### Objetivo principal
Criar esqueleto FastAPI com endpoint simples integrado ao LLM escolhido, configurando base de segurança e variáveis de ambiente.

### Conceitos que serão aprendidos
- FastAPI + Pydantic v2 (setup, roteamento, validação).
- Streaming/respostas assíncronas com LLM (prévia).
- Boas práticas de segurança básica (CORS, secrets, logs).

### Como se relaciona com Dia 7
- Reusa o Knowledge Assistant como lógica de domínio; cria uma camada HTTP para expor o fluxo.
- Documentação e evidências de QA servem como contrato de comportamento esperado.

---

## 📋 Como Construir o Dia 8
### 1. Estrutura básica
```
Semana3/Dia1/ (ou equivalente)
├── README.md
├── CONTEXTO_AGENTE.md
├── checklist.md
├── journal.md
├── requirements.txt
└── (arquivos de scaffolding conforme Nível 1)
```

### 2. Definir Nível de Scaffolding
- Conceito novo (FastAPI) → **Nível 1** recomendado (ver `../../GUIAS/GUIA_DECISAO_SCAFFOLDING.md`).
- Arquivos: `exemplo_completo.py` + `GUIA_PASSO_A_PASSO.md` + `exercicios.md` focados em endpoints básicos e segurança mínima.

### 3. Criar arquivos de aprendizado
- `exemplo_completo.py`: endpoint `/health` e `/chat` com echo do LLM (stream opcional).
- `GUIA_PASSO_A_PASSO.md`: setup venv, instalar FastAPI + uvicorn, estrutura de pastas, primeira rota.
- `exercicios.md`: desafios incrementais (CORS, validação Pydantic, logging estruturado).

### 4. Seguir checklist
- Preparação → Leitura → Construção → Consolidação → Registro (160min).

---

## 📚 Recursos de Preparação
- `../../METODOLOGIA_ENSINO.md` e `../../GUIAS/GUIA_DECISAO_SCAFFOLDING.md`.
- Documentação FastAPI (atual): https://fastapi.tiangolo.com/
- Pydantic v2 overview: https://docs.pydantic.dev/latest/
- LangChain/LangGraph overview: https://docs.langchain.com/oss/python/langchain/overview

### Conceitos pré-requisitos
- Python 3.12 + virtualenv.
- Noções de HTTP/JSON.
- Princípios de segurança básica (segredos, CORS).

---

## 💡 Dicas Importantes
1. Fixar Nível 1 para FastAPI: fornecer exemplo completo e passo-a-passo claro.
2. Reusar outputs de QA de hoje como contratos de comportamento para endpoints.
3. Começar com endpoints mínimos (`/health`, `/chat`) antes de adicionar autenticação.
4. Manter limite de 160min; dividir se houver excedente.

---

**Última atualização:** 7 Dez 2025  
**Status:** 🟡 Pronto como briefing para o Dia 8

