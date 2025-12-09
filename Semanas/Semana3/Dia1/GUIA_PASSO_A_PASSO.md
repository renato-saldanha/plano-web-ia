# 🧭 GUIA_PASSO_A_PASSO - FastAPI Dia 1 (Nível 1)

Objetivo: subir um FastAPI com `/health` e `/chat` (eco), CORS mínimo e logs.

---

## 1) Preparar ambiente (10min)
- Ativar venv:
  - PowerShell: `./venv/Scripts/Activate.ps1`
  - Bash: `source venv/bin/activate`
- Instalar dependências: `pip install -r requirements.txt`
- Opcional: criar `.env` com chaves (`GROQ_API_KEY`, `GOOGLE_API_KEY`, `ANTHROPIC_API_KEY`) se quiser trocar placeholder do LLM.

## 2) Rodar o servidor (5min)
- Com recarregamento: `uvicorn exemplo_completo:app --reload --port 8000`
- Docs automáticas: http://localhost:8000/docs  
- Redoc: http://localhost:8000/redoc

## 3) Testar `/health` (5min)
- Curl: `curl http://localhost:8000/health`
- Esperado:
  ```json
  {"status":"ok","version":"0.1.0","docs":"http://localhost:8000/docs"}
  ```

## 4) Testar `/chat` (10min)
- httpie: `http POST http://localhost:8000/chat message="Olá FastAPI" source="web"`
- Curl:
  ```bash
  curl -X POST http://localhost:8000/chat ^
    -H "Content-Type: application/json" ^
    -d "{\"message\":\"Olá FastAPI\",\"source\":\"web\"}"
  ```
- Esperado:
  ```json
  {"reply":"[eco] Olá FastAPI","model":"placeholder-echo","metadata":{"source":"web","user_id":null}}
  ```

## 5) Ajustar CORS se necessário (5min)
- Em `exemplo_completo.py`, edite `ALLOWED_ORIGINS` para incluir a origem local (ex.: frontend em 3000/5173).

## 6) Próximos passos (para Dia 2)
- Integrar JWT e middlewares.
- Trocar `call_llm` por chamada real (Groq/Gemini/Claude) e considerar streaming.
- Adicionar testes rápidos (httpx/pytest) e rate limiting básico.

---

### Referências
- FastAPI: https://fastapi.tiangolo.com/
- Pydantic v2: https://docs.pydantic.dev/latest/
- Metodologia: `../../METODOLOGIA_ENSINO.md`
- Scaffolding: `../../GUIAS/GUIA_DECISAO_SCAFFOLDING.md`

