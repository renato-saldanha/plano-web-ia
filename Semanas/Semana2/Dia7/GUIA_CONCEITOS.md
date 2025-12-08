# GUIA_CONCEITOS - QA/Polish do Agent (Nível 3)

## 1) Docstrings e Prompt
- Deixe explícito “quando usar” e “quando NÃO usar” cada tool (calculator: apenas aritmética direta; RAG: perguntas sobre corpus; nada de extrapolar dados inexistentes).
- Inclua no prompt: “Use RAG antes de responder perguntas conceituais; só use calculator para operações numéricas simples; se faltar contexto, peça clarificação”.

## 2) Recursion e Observabilidade
- `recursion_limit`: 6-10 é suficiente na maioria dos fluxos; limites maiores aumentam risco de loop.
- Sempre inspecione `messages` após um teste que falhar para ver cadeia de raciocínio e escolha de tool.

## 3) Erros Amigáveis
- Falta de index (FAISS): “Recrie com scripts do Dia 4 em ../Dia4/; confirme caminho.”
- Falta de chave: “Configure .env (GROQ_API_KEY ou GOOGLE_API_KEY/ANTHROPIC_API_KEY) e recarregue.”
- Erros de rede: “Tente novamente; se persistir, teste com modelo alternativo.”

## 4) Smoke Tests Essenciais
- Cálculo simples → só calculator.
- Pergunta de contexto → RAG.
- Pergunta mista → RAG + calculator se necessário.
- Caso ambíguo → clarificação ou melhor palpite, sem alucinar.

## 5) Registro e Handoff
- Guarde entradas/saídas de testes no journal; aponte qual tool foi chamada.
- Documente passos mínimos de execução: ativar venv, exportar .env, onde está o index.
- Anote o comportamento esperado para cada caso de teste (serve de contrato para o backend no Dia 8).

