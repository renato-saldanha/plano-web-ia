"""
Módulo de gerenciamento de conversas.

Fornece funções para gerenciar histórico de conversas em memória.
"""

import uuid
from datetime import datetime, timezone
from typing import Dict, List, Optional

# Armazenamento em memória
# Estrutura: {user_id: {conversation_id: [messages]}}
conversations: Dict[str, Dict[str, List[Dict]]] = {}


def get_or_create_conversation(user_id: str, conversation_id: Optional[str] = None) -> str:
    """
    Retorna conversation_id existente ou cria novo.
    
    Args:
        user_id: ID do usuário
        conversation_id: ID da conversa (opcional, cria nova se não fornecido)
        
    Returns:
        str: ID da conversa (existente ou novo)
    """
    if user_id not in conversations:
        conversations[user_id] = {}
    
    if conversation_id and conversation_id in conversations[user_id]:
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
        role: Role da mensagem ("user" ou "assistant")
        content: Conteúdo da mensagem
    """
    if user_id not in conversations:
        conversations[user_id] = {}
    if conversation_id not in conversations[user_id]:
        conversations[user_id][conversation_id] = []
    
    message = {
        "role": role,
        "content": content,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
    conversations[user_id][conversation_id].append(message)


def get_messages(user_id: str, conversation_id: str) -> List[Dict]:
    """
    Retorna lista de mensagens de uma conversa.
    
    Args:
        user_id: ID do usuário
        conversation_id: ID da conversa
        
    Returns:
        List[Dict]: Lista de mensagens (cópia para evitar mutação)
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
        List[Dict]: Lista de conversas com id, created_at, last_message, message_count
    """
    if user_id not in conversations:
        return []
    
    result = []
    for conv_id, messages in conversations[user_id].items():
        if not messages:
            continue
        
        created_at = messages[0].get("timestamp", datetime.now(timezone.utc).isoformat())
        last_msg = messages[-1].get("content", "") if messages else None
        
        result.append({
            "id": conv_id,
            "created_at": created_at,
            "last_message": last_msg,
            "message_count": len(messages)
        })
    
    result.sort(key=lambda x: x["created_at"], reverse=True)
    return result

