"""
Modelos Pydantic compartilhados.

Define modelos de dados reutilizáveis entre os dias da Semana 3.
"""

from typing import Optional, Literal
from pydantic import BaseModel


class Message(BaseModel):
    """Modelo de mensagem de chat."""
    role: Literal["user", "assistant"]
    content: str
    timestamp: Optional[str] = None


class ConversationSummary(BaseModel):
    """Modelo de resumo de conversa."""
    id: str
    created_at: str
    last_message: Optional[str] = None
    message_count: int


class ChatRequest(BaseModel):
    """Modelo de requisição de chat."""
    message: str
    conversation_id: Optional[str] = None
    model: Optional[str] = None
    stream: bool = True


class Token(BaseModel):
    """Modelo de resposta com tokens JWT."""
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class LoginRequest(BaseModel):
    """Modelo de requisição de login."""
    username: str
    password: str


class RefreshRequest(BaseModel):
    """Modelo de requisição de refresh token."""
    refresh_token: str


class GenerateRequest(BaseModel):
    """Modelo de requisição de geração (sem histórico)."""
    prompt: str
    model: Optional[str] = None

