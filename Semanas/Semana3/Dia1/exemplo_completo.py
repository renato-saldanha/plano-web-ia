#!/usr/bin/env python3
"""
Esqueleto FastAPI (Nível 1) com rotas básicas e placeholder LLM.

Como usar:
1) Ative o venv e instale dependências:
   pip install -r requirements.txt
2) Rode o servidor:
   uvicorn exemplo_completo:app --reload --port 8000
3) Teste:
   curl http://localhost:8000/health
   http POST http://localhost:8000/chat message="Olá FastAPI"

Notas:
- CORS está restrito a localhost para dev; ajuste em produção.
- LLM é placeholder; substitua `call_llm` para integrar Groq/Gemini/Claude.
"""

import asyncio
from contextlib import asynccontextmanager
from typing import Any, Dict, Optional

import logging
import os

from dotenv import load_dotenv
from fastapi import Body, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field, HttpUrl
from langchain_openai import ChatOpenAI
import uuid

# ============================================================================ #
# Configuração
# ============================================================================ #

load_dotenv()  # Carrega .env na raiz se existir

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
logger = logging.getLogger("fastapi-dia1")

ALLOWED_ORIGINS = [
    "http://192.168.1.15:3000",
]

APP_NAME = "FastAPI + IA (Semana 3 - Dia 1)"
APP_VERSION = "0.1.0"


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Gerencia eventos de startup e shutdown da aplicação."""
    # Startup
    logger.info("%s iniciado (versão %s)", APP_NAME, APP_VERSION)
    llm_key_present = any(
        os.getenv(key) for key in ("GROQ_API_KEY", "GOOGLE_API_KEY", "OPENAI_API_KEY")
    )
    if not llm_key_present:
        logger.info("Rodando em modo eco (nenhuma chave LLM encontrada).")

    yield  # Aplicação roda aqui

    # Shutdown (se precisar limpar recursos no futuro)
    logger.info("%s encerrado.", APP_NAME)


app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="Esqueleto básico para evoluir com JWT e LLM nos próximos dias.",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================================ #
# Modelos Pydantic
# ============================================================================ #


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, description="Mensagem do usuário")
    source: Optional[str] = Field(
        default="web",
        description="Origem da requisição (web, cli, teste)",
    )
    user_id: Optional[str] = Field(
        default=None,
        description="Identificador do usuário (para rastrear sessões futuras)",
    )
    temperature: float | None = Field(
        default=None,
        ge=0,
        le=1,
        description="Temperatura do Modelo"
    )


class ChatResponse(BaseModel):
    reply: str = Field(..., description="Resposta gerada ou ecoada")
    model: str = Field(default="placeholder-echo",
                       description="Modelo utilizado")
    metadata: Dict[str, Any] = Field(
        default_factory=dict,
        description="Metadados de debug/trace"
    )


class HealthResponse(BaseModel):
    status: str = Field(..., description="Estado do serviço")
    version: str = Field(..., description="Versão da aplicação")
    docs: Optional[HttpUrl] = Field(
        default=None, description="URL dos docs locais se disponível"
    )


# ============================================================================ #
# Funções auxiliares
# ============================================================================ #


def call_llm(message: str, temperature: float | None) -> str:
    """
    Placeholder para futura chamada de LLM.

    Substitua por integração real (Groq/Gemini/Claude) nos próximos dias.
    """
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=temperature if temperature else 0
    )

    response = llm.invoke(message)

    return response.content


# ============================================================================ #
# Rotas
# ============================================================================ #


@app.get("/health", response_model=HealthResponse, tags=["health"])
async def health() -> HealthResponse:
    return HealthResponse(
        status="ok",
        version=APP_VERSION,
        docs="http://localhost:8000/docs",
    )


@app.post("/chat", response_model=ChatResponse, tags=["chat"])
async def chat(payload: ChatRequest = Body(...)) -> ChatResponse:
    request_id = str(uuid.uuid4())
    logging.info("request_id:%s", request_id)
    logger.info("payload=%s", payload.model_dump())

    reply_text = call_llm(payload.message, payload.temperature)

    return ChatResponse(
        reply=reply_text,
        model="placeholder-echo",
        metadata={
            "request_id": request_id,
            "source": payload.source,
            "user_id": payload.user_id,
            "temperature": payload.temperature,
        },
    )


async def generate_chunks():
    chunks = ["Olá, ", "como posso ", "ajudar?"]
    for chunk in chunks:
        yield chunk
        await asyncio.sleep(.5)


@app.get("/stream", tags=["chat"])
async def stream_reply():
    return StreamingResponse(generate_chunks(), media_type="text/plain")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("exemplo_completo:app", host="0.0.0.0", port=8000, reload=True)
