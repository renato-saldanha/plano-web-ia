# Exercícios - Dia 7 (Nível 3)

Foco: QA e polish do Knowledge Assistant (LangGraph).

## Exercício 1 — Docstrings e Prompt (15-20min)
- Reescreva as docstrings das tools para incluir: propósito, quando usar, quando NÃO usar, exemplos curtos.
- Ajuste o prompt para instruir: “Use RAG antes de responder perguntas conceituais; só use calculator para aritmética simples; se estiver ambíguo, peça clarificação.”

## Exercício 2 — Smoke Tests Extras (30-35min)
Rode os 4 casos e registre no journal: entrada, tool(s) chamadas, resposta final, observações.
- Só cálculo: `(18 / 3) + 5`
- Só RAG: pergunta conceitual do corpus (ex.: sobre FAISS ou recursion_limit)
- Misto: “Segundo o corpus, qual recursion_limit sugerido e depois faça 15*2?”
- Ambíguo: “Preciso de ajuda com números e contexto, o que faço?”

Critério: nenhuma escolha de tool errada; se ocorrer, ajuste docstrings/prompt e repita.

## Exercício 3 — Erros e UX (20-25min)
- Simule falta de index ou de chave e produza mensagens amigáveis sugerindo correção.
- Documente no journal qual mensagem aparece e o passo de correção.

## Exercício 4 — Handoff (15-20min)
- Escreva no README ou journal um passo-a-passo mínimo: ativar venv, carregar .env, localizar `../Dia4/faiss_index`, rodar o script, casos de teste principais.
- Liste expectativas de comportamento (serve de contrato para o backend do Dia 8).

## Stretch (opcional, se houver tempo)
- Adicionar contador simples de tentativas ou fallback de modelo (ex.: trocar Groq → Gemini).

---

**Dica:** Use `messages` para inspecionar a cadeia de decisão do agent. Se o agent tentar calculator em pergunta conceitual, reforce a docstring do RAG indicando que perguntas textuais devem usar o retriever.

