#!/usr/bin/env python3
"""
API FastAPI com Histórico de Chat - Template (Nível 2)

Preencha os TODOs seguindo GUIA_APRENDIZADO.md e o exemplo_referencia.py.
Objetivo: adicionar sistema de histórico de conversas ao /api/chat,
mantendo contexto entre mensagens.

Uso:
    uvicorn template:app --reload --port 8000

Regras:
- Não usar autocomplete/IA para gerar código.
- Manter tempo total em 160min (ver checklist.md).
"""

# Variáveis de Amb
import os
import uuid
from dotenv import load_dotenv

# LangChain
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage

# Rate Limiter
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

# FastAPI
from fastapi import FastAPI, Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from starlette.middleware.base import BaseHTTPMiddleware

# validação
from pydantic import BaseModel, Field

# JWT
from jose import JWTError, jwt
from datetime import date, datetime, timedelta, timezone
from typing import AsyncIterator, Dict, List, Literal, Optional

# Hashing
from passlib.context import CryptContext
from starlette.status import HTTP_404_NOT_FOUND

load_dotenv()


# Define Constântes
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
if not JWT_SECRET_KEY:
    raise Exception("Favor verificar a JWT_SECRET_KEY")

JWT_ALGORITHM = os.getenv("ALGORITHM")
if not JWT_ALGORITHM:
    raise Exception("Favor verificar o JWT_ALGORITHM")

ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
if not ACCESS_TOKEN_EXPIRE_MINUTES:
    raise Exception("Favor verificar o ACCESS_TOKEN_EXPIRE_MINUTES")

REFRESH_TOKEN_EXPIRE_DAYS = os.getenv("REFRESH_TOKEN_EXPIRE_DAYS")
if not REFRESH_TOKEN_EXPIRE_DAYS:
    raise Exception("Favor verificar o REFRESH_TOKEN_EXPIRE_DAYS")

DEFAULT_MODEL = "gpt-4o-mini"

# Define variável de mannipulação de encriptação
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Define a lista de
conversations: Dict[str, Dict[str, List[Dict]]] = {}

# =============================================================================
# Configurar FastAPI + CORS
# =============================================================================
app = FastAPI(
    title="API com Histórico de Chat",
    description="Dia 4 - Sistema de histórico de conversas",
    version="1.0.0",
)

ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost",
]

# Define classe do middleware de segurança


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame_options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        return response


# Instância da configuração do middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(SecurityHeadersMiddleware)

# Definição do Rate Limiter
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def verify_token(token: str, expected_type: str = "access") -> dict:
    """
    Verifica se o token fornecido é válido.
    Busca o usuário.
    Se o usuário for inválido, retorna uma excessão.

    Args: token:str-> Token de validação.
          expected_type:str-> Tipo esperado de token, se não for passado o parâmetro encara como "access" por padrão.

    Return: dict-> Objeto JSON contendo usuário e payload com a validação do token.
    """

    try:
        # Define o payload
        payload = jwt.decode(
            token,
            JWT_SECRET_KEY,
            algorithms=[JWT_ALGORITHM]
        )

        # Verifica o tipo de token
        token_type = payload.get("type")
        # Gera erro se diferente
        if token_type != expected_type:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Tipo de token inválido ({token_type})",
                headers={"WWW-Authenticate": "Bearer"}
            )
        return payload
    # Gera erro se token não é válido
    except JWTError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Token inválido ou expirado: {exc}",
            headers={"WWW-Authenticate": "Bearer"}
        ) from exc


async def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    """ 
    Verifica se o token fornecido é válido.
    Busca o usuário.
    Se o usuário for inválido, retorna uma excessão.

    Args: token-> Token de validação que depende do oauth2_scheme para aplicar a segurança.

    Return: dict-> Objeto JSON contendo usuário e payload com a validação do token.
    """

    payload = verify_token(token, expected_type="access")
    username = payload.get("sub")
    if not username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário não autorizado",
            headers={"WWW-Authenticate": "Bearer"}
        )

    return {"username": username, "payload": payload}


# =============================================================================
#  Modelos Pydantic para histórico
# =============================================================================
class Message(BaseModel):
    role: Literal["user", "assistant"]
    content: str
    timestamp: Optional[str] = None


class ConversationSummary(BaseModel):
    id: str
    created_at: str
    last_message: Optional[str] = None
    message_count: int


class ChatRequest(BaseModel):
    message: str = Field(..., description="Mensagem do usuário")
    conversation_id: Optional[str] = Field(
        None, description="ID da conversa (cria nova se não fornecido)")
    model: Optional[str] = Field(default=None, description="Modelo LLM")
    stream: bool = Field(default=True, description="Se true, responde via SSE")


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class LoginRequest(BaseModel):
    username: str
    password: str


class RefreshRequest(BaseModel):
    refresh_token: str


class GenerateRequest(BaseModel):
    prompt: str
    model: Optional[str] = None


# =============================================================================
# Funções auxiliares de histórico
# =============================================================================
def get_or_create_conversation(user_id: str, conversation_id: Optional[str] = None) -> str:
    """
    Retorna conversation_id existente ou cria novo.

    Args:
        user_id: ID do usuário
        conversation_id: ID da conversa (opcional)

    Returns:
        str: ID da conversa (existente ou novo)
    """

    if user_id not in conversations["user_id"]:
        conversations[user_id] = {}

    if conversation_id and conversation_id in conversations:
        return conversation_id

    new_id = str(uuid.uuid4())
    conversations[user_id][new_id] = []
    return new_id


def add_message(user_id: str, conversation_id: str, role: str, content: str) -> None:
    """
    Adiciona mensagem à conversa.

    Args:
        user_id: ID do usuário
        conversation_id: ID da conversa
        role: "user" ou "assistant"
        content: Conteúdo da mensagem
    """

    # Garante de user_id está em conversations
    if user_id not in conversations:
        conversations[user_id] = {}

    # Garante de conversation_id existe
    if conversation_id not in conversations[user_id]:
        conversations[user_id][conversation_id] = []

    # Define a mensaggem
    message = {
        "role": role,
        "content": content,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
    # Adiciona a mensagem na lista de conversa
    conversations[user_id][conversation_id].append(message)


def get_messages(user_id: str, conversation_id: str) -> List[Dict]:
    """
    Retorna lista de mensagens de uma conversa.

    Args:
        user_id: ID do usuário
        conversation_id: ID da conversa

    Returns:
        List[Dict]: Lista de mensagens
    """

    if user_id not in conversations:
        return []

    if conversation_id not in conversations[user_id]:
        return []

    return conversations[user_id][conversation_id].copy()


def list_conversations(user_id: str) -> List[Dict]:
    """
    Lista todas as conversas do usuário.

    Args:
        user_id: ID do usuário

    Returns:
        List[Dict]: Lista com {id, created_at, last_message, message_count}
    """

    if not user_id in conversations:
        return []

    # Busca conversas pelo user_id
    result = []
    for conversation_id, messages in conversations[user_id].items():
        created_at = messages[0].get("timestamp", datetime.now(timezone.utc).isoformat()) if not messages else None
        last_message = messages[-1].get("content") if messages else None
        message_count = len(messages)

        # Adiciona a conversa à lista
        result.append({
            "id": conversation_id,
            "created_at": created_at,
            "last_message": last_message,
            "message_count": message_count,
        })

    # Ordena por mais recente primeiro
    result.sort(key=lambda x: x["created_at"], reverse=True)
    return result


# =============================================================================
# Função de streaming (modificada para usar histórico)
# =============================================================================
async def stream_llm(messages: List, model: str, conversation_id) -> AsyncIterator[str]:
    """
    Gera tokens do LLM com contexto de histórico.

    Args:
        messages: Lista de HumanMessage/AIMessage (com histórico)
        model: Nome do modelo
    """

    # Defino o modelo
    model = ChatOpenAI(
        model=DEFAULT_MODEL,
        temperature=0.15,
        streaming=True,
    )

    # Itera o conteúdo das mensagens
    async for chunk in model.astream(messages):
        if chunk.content:
            yield f"data: {chunk.content}\\n\\n"

    yield "data: [DONE]\\n\\n"


# =============================================================================
# Auth endpoints (herdado do Dia 3)
# =============================================================================
FAKE_USER = {
    "username": "admin",
    "hashed_password": pwd_context.hash("admin123"),
}


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Cria token de acesso com opção de personalizar o tempo de expiração.

    Args: data-> Dados do usuário({"sub": username}).
          expires_delta-> Opcional, define um tempo de expiração personalizado.  

    Return: Um JWT encoded com um token de acesso.
    """

    to_encode = data.copy()

    # verifica se foi fornecida expriração personalizada
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + \
            timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))

    # Atualiza os dados do usuário
    to_encode.update({
        "exp": expire,
        "type": "access"
    })

    # Encripta o JWT
    encoded_jwt = jwt.encode(
        to_encode,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )
    return encoded_jwt


def create_refresh_token(data: dict) -> str:
    """
    Cria token de atualização.

    Args: data-> Dados do usuário({"sub": username}).          

    Return: Um JWT encoded com token de atualização.
    """

    to_encode = data.copy()

    time_utc = datetime.now(timezone.utc)
    time_delta = timedelta(days=int(REFRESH_TOKEN_EXPIRE_DAYS))
    expire = time_utc + time_delta

    # Atualiza os dados do usuário
    to_encode.update({
        "exp": expire,
        "type": "refresh",
    })

    # Encripta o JWT
    encoded_jwt = jwt.encode(
        to_encode,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM)

    return encoded_jwt


@app.post("/login", response_model=Token)
@limiter.limit("5/minute")
async def login(request: Request, login_data: LoginRequest):
    """ 
    Endpoint de Login com Rate Limiter de 5 acessos por minuto.
    """

    # Verificar usuário
    if login_data.username != FAKE_USER["username"]:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário inválido."
        )

    # Verificar senha
    if not pwd_context.verify(login_data.password, FAKE_USER["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Senha inválida."
        )

    # Gera tokens
    access_token = create_access_token(data={"sub": login_data.username})
    refresh_token = create_refresh_token(data={"sub": login_data.username})

    return Token(
        access_token=access_token,
        refresh_token=refresh_token
    )


@app.post("/refresh", response_model=Token)
async def refresh(request: RefreshRequest):
    """ 
    Endpoint de atualização de token de acesso.
    """

    # Verifica refresh token
    payload = verify_token(request.refresh_token, expected_type="refresh")
    username = payload.get("sub")

    # Gera novos tokens
    access_token = create_access_token(data={"sub": username})
    refresh_token = create_refresh_token(data={"sub": username})

    return Token(
        access_token=access_token,
        refresh_token=refresh_token)


@app.post("/chat")
async def chat(
    request: ChatRequest,
    current_user: dict = Depends(get_current_user),
):
    """
    Endpoint de chat com histórico.
    """

    model_name = request.model or DEFAULT_MODEL
    user_id = current_user["username"]
    conversation_id = get_or_create_conversation(
        user_id, request.conversation_id)

    messages = get_messages(user_id, conversation_id)

    langchain_messages = []

    for message in messages:
        if message["role"] == "user":
            human_message = HumanMessage(content=message["content"])
            langchain_messages.append(human_message)
        if message["role"] == "assistant":
            ai_message = AIMessage(content=message["content"])
            langchain_messages.append(ai_message)

    user_message = HumanMessage(content=request.message)
    langchain_messages.append(user_message)

    add_message(user_id, conversation_id, "user", request.message)

    streamable = bool(request.stream)
    match streamable:
        case True:
            async def generate():
                model = ChatOpenAI(
                    model=model_name,
                    temperature=0.2,
                    streaming=True,
                )
                response = ""

                async for chunk in model.astream(langchain_messages):
                    if chunk.content:
                        response += chunk.content
                        yield f"data: {chunk.content}\n\n"

                yield "data: [DONE]\n\n"

                add_message(user_id, conversation_id,
                            "assistant", response)

            return StreamingResponse(generate(), media_type="text/event-stream")
        case False:
            model = ChatOpenAI(
                model=model_name,
                temperature=0.2,
                streaming=False,
            )

            ai_response = await model.ainvoke(langchain_messages)
            response_content = ai_response.content

            add_message(user_id, conversation_id,
                        "assistant", response_content)

            return {
                "reply": response_content,
                "conversation_id": conversation_id,
                "user": user_id,
                "model": model,
            }


# =============================================================================
# TODO Endpoint - Listar conversas
# =============================================================================
@app.get("/conversations", response_model=List[ConversationSummary])
async def list_user_conversations(
    current_user: dict = Depends(get_current_user),
):
    """
    Lista todas as conversas do usuário autenticado.

    TODO:
    1. Obter user_id de current_user
    2. Chamar list_conversations(user_id)
    3. Retornar lista formatada como ConversationSummary
    """
    # TODO: Implementar

    user_id = current_user["username"]

    conversations = list_conversations(user_id)

    conversation_list = [ConversationSummary(
        id=conv["id"],
        created_at=conv["created_at"],
        last_message=conv["last_message"],
        message_count=conv["message_count"],
    ) for conv in conversations
    ]

    return conversation_list


# =============================================================================
# TODO 7: Endpoint - Obter mensagens de uma conversa
# =============================================================================
@app.get("/conversations/{conversation_id}/messages", response_model=List[Message])
async def get_conversation_messages(
    conversation_id: str,
    current_user: dict = Depends(get_current_user),
):
    """
    Retorna todas as mensagens de uma conversa específica.

    TODO:
    1. Obter user_id de current_user
    2. Verificar se conversa pertence ao usuário (segurança!)
    3. Buscar mensagens usando get_messages()
    4. Retornar lista formatada como Message
    5. Se conversa não encontrada, retornar 404
    """
    # TODO: Implementar

    user_id = current_user["username"]

    if user_id not in conversations:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail="Conversa não encontrada"
        )

    if conversation_id not in conversations[user_id]:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail="Conversa não encontrada"
        )

    messages = get_messages(user_id, conversation_id)

    formated_messages = [
        Message(
            role=message["role"],
            content=message["content"],
            timestamp=message["timestamp"],
        ) for message in messages
    ]

    return formated_messages


# =============================================================================
# Endpoint /api/generate (mantido do Dia 3, sem histórico)
# =============================================================================
async def stream_llm_simple(prompt: str, model: str) -> AsyncIterator[str]:
    """Versão simples sem histórico (para /api/generate)."""
    llm = ChatOpenAI(model=model, streaming=True, temperature=0.2)
    async for chunk in llm.astream([HumanMessage(content=prompt)]):
        if chunk.content:
            yield f"data: {chunk.content}\n\n"
    yield "data: [DONE]\n\n"


@app.post("/api/generate")
async def generate(
    request: GenerateRequest,
    current_user: dict = Depends(get_current_user),
):
    """Endpoint simples de streaming (sem histórico)."""
    model = request.model or DEFAULT_MODEL
    return StreamingResponse(
        stream_llm_simple(request.prompt, model=model),
        media_type="text/event-stream"
    )


@app.get("/health")
async def health():
    return {"status": "healthy", "feature": "chat_history"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
