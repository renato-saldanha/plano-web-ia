# 🧪 Exercícios - Agents e Tools (Dia 5)

## Instruções
- Use `exemplo_completo.py` como referência.
- Mantenha `verbose=True` para observar ReAct.
- Anote dúvidas e resultados no journal.

---

### Exercício 1 — Calculator Tool
- Implemente uma variação da tool que suporte potência (`**`) de forma segura.
- Teste com: `2**5 + 10`.

### Exercício 2 — RAG como Tool
- Altere `search_kwargs` para `{"k": 5}` e compare respostas.
- Pergunta: “Liste 3 vantagens de vector databases sobre BM25”.

### Exercício 3 — Agent com 2 Tools
- Execute o Agent com as perguntas:
  1. “Some 9999 + 321”
  2. “Explique embeddings em 2 frases curtas”
- Verifique se ele escolhe calculator no (1) e RAG no (2).

### Exercício 4 — Pergunta Mista
- Pergunta: “Qual a capital da França e quanto é 17*24?”.
- Objetivo: Agent deve usar RAG para capital e calculator para a conta.

### Desafio (opcional)
- Adicione uma terceira tool simples (ex.: contagem de tokens ou busca web simulada) e observe o impacto da descrição na escolha do Agent.

---

**Dica:** se o Agent escolher a tool errada, refine a descrição das tools deixando explícito **quando** usar e **o que** retorna.

