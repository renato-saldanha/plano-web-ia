"""
Módulos compartilhados para Semana 3.

Este pacote contém funções e classes reutilizáveis entre os dias da Semana 3,
reduzindo duplicação de código e complexidade acumulada.
"""

from .logging import JSONFormatter, log_structured, setup_logger
from .auth import verify_token, get_current_user, create_access_token, create_refresh_token
from .models import (
    Message,
    ConversationSummary,
    ChatRequest,
    Token,
    LoginRequest,
    RefreshRequest,
    GenerateRequest,
)
from .conversations import (
    get_or_create_conversation,
    add_message,
    get_messages,
    list_conversations,
    conversations,
)

__all__ = [
    # Logging
    "JSONFormatter",
    "log_structured",
    "setup_logger",
    # Auth
    "verify_token",
    "get_current_user",
    "create_access_token",
    "create_refresh_token",
    # Models
    "Message",
    "ConversationSummary",
    "ChatRequest",
    "Token",
    "LoginRequest",
    "RefreshRequest",
    "GenerateRequest",
    # Conversations
    "get_or_create_conversation",
    "add_message",
    "get_messages",
    "list_conversations",
    "conversations",
]

