# 🧪 Exercícios - Dia 6 (LangGraph + Tools + RAG)

## Como usar
- Execute os casos em `exemplo_referencia.py` ou no fluxo que você montar a partir de `template.py`.
- Para cada exercício, anote no `journal.md`: pergunta, ferramenta(s) usadas, se a escolha foi correta e ajustes nas descrições.

---

## Exercício 1 — Calculator-only (Smoke)
- Pergunta: `Some 789 + 432`
- Esperado: usar **calculadora** apenas.
- Se escolher RAG, fortaleça a docstring da calculadora deixando explícito “Use para contas aritméticas simples”.

## Exercício 2 — RAG-only (Conceitual)
- Pergunta: `Explique em 2 frases a diferença entre embeddings e BM25.`
- Esperado: usar **buscar_conhecimento** apenas.
- Se escolher calculadora, reforce docstring do RAG: “Use para perguntas conceituais baseadas no corpus do Dia 4 (FAISS)”.

## Exercício 3 — Misto (RAG + cálculo)
- Pergunta: `Qual é a capital da França e quanto é 13*7?`
- Esperado: consultar RAG para capital e usar calculadora para a conta.
- Observação: verifique se a ordem faz sentido; se inverter, melhore descrições.

## Exercício 4 — Fallback e mensagens
- Pergunta: `Quais são os passos de chunking usados no Dia 4?`
- Esperado: buscar no RAG. Se não achar, resposta honesta “não encontrado”.
- Ajuste docstring do RAG para citar “documentos do Dia 4”.

## Exercício 5 — Robustez
- Pergunta: `Some 2 + dois`
- Esperado: validação da calculadora respondendo erro amigável.
- Melhore regex/validação conforme necessário.

---

## Critérios de sucesso
- Agent escolhe a tool correta em 4/5 cenários ou você ajustou descrições para isso.
- Não há exceções não tratadas durante os smoke tests.
- Journal possui registro das queries e observações.

