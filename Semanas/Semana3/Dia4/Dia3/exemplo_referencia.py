#!/usr/bin/env python3
"""
API FastAPI com Streaming (SSE) + LLM (Exemplo de Referência)

- /api/generate: retorna tokens via SSE
- /chat: streaming opcional (SSE) ou resposta única JSON
- Protegido por JWT (usa fluxo simples compatível com Dia 2)

Uso:
    uvicorn exemplo_referencia:app --reload --port 8000
"""

import os
from typing import AsyncIterator, Optional

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import StreamingResponse
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from jose import JWTError, jwt
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# -----------------------------------------------------------------------------
# Config / env
# -----------------------------------------------------------------------------
load_dotenv()

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY") or ""
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
DEFAULT_MODEL = os.getenv("DEFAULT_LLM_MODEL", "gpt-4o-mini")

if not JWT_SECRET_KEY:
    raise RuntimeError("Defina JWT_SECRET_KEY no .env")

# -----------------------------------------------------------------------------
# FastAPI + CORS
# -----------------------------------------------------------------------------
app = FastAPI(
    title="API Streaming SSE + LLM (Ref)",
    description="Dia 3 - Exemplo completo",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------------------------------------------------------
# Auth (compatível com Dia 2)
# -----------------------------------------------------------------------------
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def verify_token(token: str, expected_type: str = "access") -> dict:
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        if payload.get("type") != expected_type:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Tipo de token inválido ({payload.get('type')})",
            )
        return payload
    except JWTError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Token inválido ou expirado: {exc}",
        ) from exc


async def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    payload = verify_token(token, expected_type="access")
    username = payload.get("sub")
    if not username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário não autorizado",
        )
    return {"username": username, "payload": payload}


# -----------------------------------------------------------------------------
# Modelos
# -----------------------------------------------------------------------------
class GenerateRequest(BaseModel):
    prompt: str = Field(..., description="Texto de entrada")
    model: Optional[str] = Field(default=None, description="Modelo LLM")


class ChatRequest(BaseModel):
    message: str
    model: Optional[str] = Field(default=None)
    stream: bool = Field(default=True)


# -----------------------------------------------------------------------------
# LLM streaming helper
# -----------------------------------------------------------------------------
async def stream_llm(prompt: str, model: str) -> AsyncIterator[str]:
    llm = ChatOpenAI(
        model=model,
        streaming=True,
    )

    async for chunk in llm.astream([HumanMessage(content=prompt)]):
        text = chunk.content
        if not text:
            continue
        # Formato SSE
        yield f"data: {text}\n\n"

    yield "data: [DONE]\n\n"


# -----------------------------------------------------------------------------
# Endpoints
# -----------------------------------------------------------------------------
@app.post("/api/generate")
async def generate(
    request: GenerateRequest,
    current_user: dict = Depends(get_current_user),
):
    model = request.model or DEFAULT_MODEL
    return StreamingResponse(
        stream_llm(request.prompt, model=model),
        media_type="text/event-stream",
    )


@app.post("/chat")
async def chat(
    request: ChatRequest,
    current_user: dict = Depends(get_current_user),
):
    model = request.model or DEFAULT_MODEL

    if request.stream:
        return StreamingResponse(
            stream_llm(request.message, model=model),
            media_type="text/event-stream",
        )

    llm = ChatOpenAI(model=model, streaming=False)
    ai_msg = await llm.ainvoke([HumanMessage(content=request.message)])
    return {
        "reply": ai_msg.content,
        "user": current_user["username"],
        "model": model,
    }


@app.get("/health")
async def health():
    return {"status": "healthy", "feature": "streaming", "model_default": DEFAULT_MODEL}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

