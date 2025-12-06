# 🧭 GUIA_AGENTS.md — Agents e Tools com LangChain v1.0 (Nível 1)

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
- **Boas descrições:** "Use para buscar conhecimento em documentos persistidos em `../Dia4/faiss_index`".
- **Formato v1.0:** Usar decorator `@tool` com type hints e docstring.

### Exemplo de Tool com LangChain v1.0:
```python
from langchain_core.tools import tool
from typing import Annotated

@tool
def calculadora(expressao: Annotated[str, "Expressão matemática, ex: '2+2'"]) -> str:
    """Calcula uma expressão aritmética simples."""
    return str(eval(expressao))  # Simplificado; adicione validação em produção
```

---

## 3. Passo a passo para este dia

### Passo 1 — Tool Calculator (20min)
1. Criar função com decorator `@tool` que aceita string "2+2".
2. Validar entrada simples (permitir dígitos, + - * / .).
3. Docstring clara (Agent usa para decidir quando chamar).

### Passo 2 — RAG como Tool (35min)
1. Reutilizar embeddings e FAISS do Dia 4 (`../Dia4/faiss_index`).
2. Criar retriever com `search_kwargs={"k":3}`.
3. Definir função `@tool buscar_conhecimento(pergunta: str) -> str` que concatena conteúdos retornados.
4. Docstring: "Busca informações em documentos usando RAG avançado do Dia 4".

### Passo 3 — Agent com create_agent v1.0 (35min)
1. LLM padrão: `ChatGroq` (Llama 3) com `temperature=0`.
2. Importar: `from langchain.agents import create_agent`
3. Criar agent: `agent = create_agent(llm, tools=[calculadora, buscar_conhecimento])`
4. Invocar: `agent.invoke({"messages": [HumanMessage(content="sua pergunta")]})`
5. Testar:
   - Query 1: "some 123 + 456" (deve usar calculator).
   - Query 2: "Qual é a diferença entre embeddings e BM25?" (deve usar RAG).
   - Query 3: "Qual a capital da França e 13*7?" (pode usar RAG + calculator).

### Passo 4 — Ajustes finos
- Se o Agent escolher tool errada, melhore descrições (docstrings).
- Se RAG não retorna, verifique persistência em `../Dia4/faiss_index`.
- Log do pensamento: iterar sobre `resultado["messages"]` para ver raciocínio.

---

## 4. create_agent: A API oficial do LangChain v1.0

### Evolução das APIs

| API | Status | Quando usar |
|-----|--------|-------------|
| `AgentExecutor` (clássico) | Descontinuado | Legado; migre para v1.0 |
| `langgraph.prebuilt.create_react_agent` | Substituído | Era intermediário; use `create_agent` |
| **`langchain.agents.create_agent`** | **✅ Oficial v1.0** | **Use este** |

### Invocação
```python
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

agent = create_agent(model="claude-sonnet-4", tools=[tool1, tool2])
result = agent.invoke({"messages": [HumanMessage(content="pergunta")]})
```

### Recursos v1.0 (Opcionais para este dia)

#### Middleware
Adicione contexto dinâmico, PII redaction, human-in-the-loop:
```python
from langchain.agents.middleware import PIIMiddleware, SummarizationMiddleware

agent = create_agent(
    model="gpt-4o",
    tools=[...],
    middleware=[
        PIIMiddleware("email", strategy="redact"),
        SummarizationMiddleware(trigger={"tokens": 500})
    ]
)
```

#### Structured Output
Respostas tipadas com Pydantic:
```python
from langchain.agents.structured_output import ToolStrategy
from pydantic import BaseModel

class Weather(BaseModel):
    temperature: float
    condition: str

agent = create_agent(
    "gpt-4o-mini",
    tools=[weather_tool],
    response_format=ToolStrategy(Weather)
)
```

**Referência:** [LangChain v1.0 Docs](https://docs.langchain.com/oss/python/releases/langchain-v1)

---

## 5. Debugging rápido
- **Agent não escolhe RAG:** docstring fraca → explicite "documentos do Dia 4, embeddings, FAISS".
- **FAISS não encontrado:** garantir `../Dia4/faiss_index` existe; se não, reexecute scripts do Dia 4.
- **Erro de API:** ver `.env` (`GROQ_API_KEY`). Para fallback, configure Gemini/Claude.
- **Loops ou respostas vazias:** adicionar `config={"recursion_limit": 10}` no invoke.

---

## 6. Boas práticas
- **Docstrings objetivas:** digam "quando usar" e "o que retorna".
- **Retornos curtos:** ferramentas devem devolver texto simples (ou JSON pequeno).
- **Raciocínio visível:** iterar sobre `messages` para ver thought process.
- **Custos:** priorize Groq (gratuito); limite tokens com `max_tokens`.

---

## 7. Referências
- **LangChain v1.0 Release:** https://docs.langchain.com/oss/python/releases/langchain-v1
- **create_agent Docs:** https://reference.langchain.com/python/langchain/agents/
- **Middleware Guide:** https://docs.langchain.com/oss/python/releases/langchain-v1#middleware
- **ReAct Paper:** https://arxiv.org/abs/2210.03629
- **Scaffolding:** `GUIAS/GUIA_DECISAO_SCAFFOLDING.md` (Nível 1)

---

**Última atualização:** 5 Dez 2025  
**Status:** 🟢 Atualizado para LangChain v1.0

