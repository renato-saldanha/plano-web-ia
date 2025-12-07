# 📘 GUIA_APRENDIZADO.md — Dia 6 (Projeto Integrado com LangGraph) — Nível 2

## 1) Visão Geral
- **Objetivo:** Integrar tools (calculator + RAG do Dia 4) em um fluxo único com **LangGraph** (`langgraph.prebuilt.create_react_agent`), formando um “Knowledge Assistant”.
- **Por que Nível 2:** Conceitos já vistos (RAG, tools, agents). Agora o desafio é integrar e ajustar descrições, com apoio de exemplo e template. Decisão baseada em `GUIAS/GUIA_DECISAO_SCAFFOLDING.md`.
- **Stack:** Python 3.12, LangChain + LangGraph, Groq (Llama 3) como LLM padrão, FAISS do Dia 4.

## 2) Passo a passo (resumo)
1. **Setup rápido**
   - Carregue `.env` (`GROQ_API_KEY` ou fallback).
   - Verifique `../Dia4/faiss_index` (recrie se necessário).
2. **Tools**
   - `@tool calculadora`: valida expressão simples e retorna string.
   - `@tool buscar_conhecimento`: usa retriever FAISS com `k=3`, concatena trechos.
3. **Agent (LangGraph)**
   - `from langgraph.prebuilt import create_react_agent`
   - `agent = create_react_agent(llm, tools=[calculadora, buscar_conhecimento])`
   - `agent.invoke({"messages": [HumanMessage(content="...")]}, config={"recursion_limit": 8})`
4. **Testes rápidos**
   - Query 1: só cálculo.
   - Query 2: só RAG conceitual.
   - Query 3: mista (RAG + cálculo).
   - Ajuste descrições se o agent escolher errado.

## 3) Detalhes úteis
### 3.1 Ferramentas com `@tool`
```python
from typing import Annotated
from langchain_core.tools import tool

@tool
def calculadora(expressao: Annotated[str, "Expressão aritmética simples ex: '2+2'"]) -> str:
    """Use para contas aritméticas simples ( + - * / ). Evite texto longo."""
    # validação leve aqui
    ...
```

### 3.2 Carregar retriever FAISS
```python
from pathlib import Path
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def load_retriever() -> FAISS:
    base = Path(__file__).parent.parent / "Dia4" / "faiss_index"
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.load_local(
        base,
        embeddings,
        allow_dangerous_deserialization=True
    ).as_retriever(search_kwargs={"k": 3})
```

### 3.3 Agent com LangGraph (prebuilt ReAct)
```python
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq

llm = ChatGroq(model="llama-3.1-70b-versatile", temperature=0)
agent = create_react_agent(llm, tools=[calculadora, buscar_conhecimento])

result = agent.invoke(
    {"messages": [HumanMessage(content="Qual a capital da França?")]} ,
    config={"recursion_limit": 8, "run_name": "dia6-demo"}
)
print(result["messages"][-1].content)
```

### 3.4 Debugging rápido
- Agent não escolhe RAG → docstring fraca; explicite “documentos do Dia 4 via FAISS”.
- FAISS ausente → recrie no Dia 4; cheque path `../Dia4/faiss_index`.
- Loop grande → ajuste `recursion_limit` (6-10) no config do invoke.
- Custos → Groq (gratuito) é padrão; limite `max_tokens` no LLM se necessário.

## 4) Como usar os arquivos
- `exemplo_referencia.py`: versão completa para consulta/testes rápidos.
- `template.py`: ponto de partida com TODOs (preencha docstrings, validações, prompt base).
- `exercicios.md`: smoke tests e ajustes guiados.

## 5) Critérios de sucesso do dia
- Agent LangGraph responde usando calculator quando a pergunta exige conta.
- Agent usa RAG (FAISS Dia 4) quando a pergunta exige contexto.
- Três queries de teste registradas (cálculo, RAG, mista) sem erros críticos.
- Journal e `CONTEXTO_PROXIMO_DIA.md` atualizados.

## 6) Referências
- `../Dia4/GUIA_RAG_AVANCADO.md`
- `../Dia5/GUIA_AGENTS.md`
- LangGraph Docs: https://python.langchain.com/docs/langgraph
- LangChain Overview: https://docs.langchain.com/oss/python/langchain/overview

