# 🧭 GUIA_AGENTS.md — Agents e Tools com LangChain (Nível 1)

## 1. O que são Agents?
- **Chain:** fluxo fixo (passos pré-definidos). Ex.: loader → splitter → retriever → LLM.
- **Agent:** fluxo dinâmico. O LLM **decide** quais ferramentas usar e em que ordem.
- **ReAct (Reason + Act):** o Agent raciocina, escolhe uma tool, observa o resultado e repete até responder.

### Por que usar Agents?
- Delegar orquestração ao LLM (menos código manual).
- Permitir múltiplas ferramentas (RAG, cálculo, APIs, etc.).
- Adaptar a diferentes tipos de pergunta sem mudar código.

### Quando NÃO usar Agents?
- Fluxo determinístico simples (prefira Chain).
- Tarefas críticas onde o LLM não pode decidir passos.

---

## 2. Tools (Ferramentas)
- **O que são:** Funções Python que o Agent pode chamar.
- **Como escolhe:** Pela **descrição** da tool (seja explícito).
- **Boas descrições:** “Use para buscar conhecimento em documentos persistidos em `../Dia4/chroma_db`”.
- **Formato recomendado:** `Tool(name, description, func)`.

---

## 3. Passo a passo para este dia

### Passo 1 — Tool Calculator (20min)
1. Criar função `somar(numeros: str) -> str` que aceita string “2+2”.
2. Validar entrada simples (permitir dígitos, + - * / .).
3. Registrar como `Tool` com descrição clara.

### Passo 2 — RAG como Tool (35min)
1. Reutilizar embeddings e Chroma do Dia 4 (`../Dia4/chroma_db`).
2. Criar retriever com `search_kwargs={"k":3}`.
3. Definir função `buscar_conhecimento(query: str) -> str` que concatena conteúdos retornados.
4. Registrar `Tool(name="buscar_conhecimento", description="Use para buscar informações em documentos do Dia 4", func=...)`.

### Passo 3 — Agent ReAct (35min)
1. LLM padrão: `ChatGroq` (Llama 3) com `temperature=0`.
2. Prompt base ReAct: mensagens de sistema + `input` do usuário.
3. Criar agent: `create_react_agent(llm, tools, prompt)`.
4. Executor: `AgentExecutor(agent=agent, tools=tools, verbose=True)`.
5. Testar:
   - Query 1: “some 123 + 456” (deve usar calculator).
   - Query 2: “Qual é a diferença entre embeddings e BM25?” (deve usar RAG).
   - Query 3: “Qual a capital da França e 13*7?” (pode usar RAG + calculator).

### Passo 4 — Ajustes finos
- Se o Agent escolher tool errada, melhore descrições.
- Se RAG não retorna, verifique persistência em `../Dia4/chroma_db`.
- Log do pensamento: manter `verbose=True` para observar ReAct.

---

## 4. Debugging rápido
- **Agent não escolhe RAG:** descrição fraca → explicite “documentos do Dia 4, embeddings, Chroma”.
- **Chroma não encontrado:** garantir `../Dia4/chroma_db` existe; se não, reexecute scripts do Dia 4.
- **Erro de API:** ver `.env` (`GROQ_API_KEY`). Para fallback, configure Gemini/Claude.
- **Loops ou respostas vazias:** reduzir `max_iterations` ou revisar descrições das tools.

---

## 5. Boas práticas
- **Descrições objetivas:** digam “quando usar” e “o que retorna”.
- **Retornos curtos:** ferramentas devem devolver texto simples (ou JSON pequeno).
- **Raciocínio visível:** mantenha `verbose=True` durante os testes.
- **Custos:** priorize Groq (gratuito); limite tokens com `max_output_tokens`.

---

## 6. Referências
- `GUIA_DECISAO_SCAFFOLDING.md` — Nível 1 (conceito novo).
- ReAct paper: https://arxiv.org/abs/2210.03629
- LangChain Agents: https://python.langchain.com/docs/modules/agents/
- LangChain Tools: https://python.langchain.com/docs/modules/agents/tools/

---

**Última atualização:** 5 Dez 2025  
**Status:** 🟡 Em progresso

