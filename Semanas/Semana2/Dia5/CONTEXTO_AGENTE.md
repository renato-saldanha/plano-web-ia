# 🤖 Contexto para Agentes IA

Este arquivo fornece contexto essencial para agentes IA que precisam entender o estado atual do projeto e próximos passos.

---

## 📍 Localização Atual

**Projeto:** Plano de Desenvolvimento - 2 Meses em Web + IA  
**Semana:** 2 de 8  
**Dia:** 5 de 7 (Sexta-feira, 5 Dez 2025)  
**Diretório:** `Semanas/Semana2/Dia5/`  
**Dia absoluto:** 12 de 56 dias totais

---

## 🎯 Estado Atual do Projeto

### O que foi feito:
- ✅ Dia 1-4 (Semana 2): LangChain básico → Chains/LCEL → RAG básico → RAG avançado (Chroma + embeddings)

### O que está em progresso:
- 🟡 Dia 5: Agents e Tools — Agent ReAct usando RAG como tool

### O que falta fazer (hoje):
- [ ] Ler `GUIA_AGENTS.md` (ReAct, tools, thought process)
- [ ] Transformar RAG avançado (Dia 4) em tool reutilizável
- [ ] Criar Agent ReAct com múltiplas tools (RAG + calculator)
- [ ] Testar queries que exigem ferramentas diferentes
- [ ] Preencher journal e `CONTEXTO_PROXIMO_DIA.md`

---

## 📋 Estrutura de Arquivos

### Arquivos Obrigatórios (ordem padrão):
- `README.md` - Contexto e objetivos do dia
- `CONTEXTO_AGENTE.md` - Este arquivo (contexto técnico)
- `checklist.md` - Checklist detalhado com fases
- `journal.md` - Template para reflexão
- `requirements.txt` - Dependências Python (obrigatório sempre)
- `CONTEXTO_PROXIMO_DIA.md` - Guia para construir Dia 6 (obrigatório)

### Arquivos de Aprendizado (Nível 1 - conceito novo):
- `GUIA_AGENTS.md` - Conceitos teóricos + passo-a-passo
- `exemplo_completo.py` - Código completo comentado (Agent + tools)
- `exercicios.md` - Exercícios guiados progressivos

---

## 🔑 Informações Importantes

### Stack Tecnológica:
- **Linguagem:** Python 3.12+
- **Framework:** LangChain
- **LLMs:** Groq (Llama 3) preferencial; Gemini/Claude como alternativas
- **Vector DB:** Chroma persistido em `../Dia4/chroma_db` (reutilizar)
- **Embeddings:** HuggingFace (`all-MiniLM-L6-v2`) já usados no Dia 4

### Configuração Necessária:
- Ambiente virtual ativo (mesmo da semana).
- Variáveis `.env`: `GROQ_API_KEY` (prioridade), `GOOGLE_API_KEY`, `ANTHROPIC_API_KEY`.
- Persistência do RAG: diretório `../Dia4/chroma_db` existente (se não existir, reexecute scripts do Dia 4).

### Objetivo do Dia:
Criar um Agent ReAct capaz de escolher ferramentas (calculator e RAG avançado) para responder perguntas, exibindo o raciocínio e reutilizando o vector store do Dia 4 como tool.

### Nível de Scaffolding:
- **Nível 1 (Iniciante)** — conceito totalmente novo (Agents/Tools/ReAct).
- Referência: `GUIAS/GUIA_DECISAO_SCAFFOLDING.md`.
- Entregáveis guiados: `exemplo_completo.py` comentado + `exercicios.md`.

---

## 🗺️ Próximos Passos

### Imediato (hoje - 160min):
1. Revisar `README.md` e `GUIA_AGENTS.md` (conceitos + ReAct).
2. Criar tools (calculator simples + RAG como tool).
3. Montar Agent ReAct com `create_react_agent` e executar queries de teste.
4. Registrar aprendizados no journal e preparar `CONTEXTO_PROXIMO_DIA.md`.

### Próximo Dia (Dia 6):
- **Foco:** Projeto integrado com LangChain (consolidar chains + RAG + agents).
- **Conexão:** Usar o Agent e tools como base para o projeto integrado.

---

## 📚 Referências Rápidas

- Metodologia: `../../METODOLOGIA_ENSINO.md`
- Scaffolding: `../../GUIAS/GUIA_DECISAO_SCAFFOLDING.md`
- Dia 4: `../Dia4/GUIA_RAG_AVANCADO.md` (rever RAG usado como tool)
- LangChain Agents: https://python.langchain.com/docs/modules/agents/
- ReAct: https://arxiv.org/abs/2210.03629

---

**Última atualização:** 5 Dez 2025  
**Status:** 🟡 Em progresso

