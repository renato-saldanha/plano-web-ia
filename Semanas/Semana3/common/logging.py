"""
Módulo de logging estruturado.

Fornece JSONFormatter e funções helper para logging estruturado em formato JSON.
"""

import json
import logging
from datetime import datetime, timezone


class JSONFormatter(logging.Formatter):
    """Formatter que serializa logs em formato JSON."""
    
    def format(self, record):
        """
        Formata um log record em JSON.
        
        Args:
            record: LogRecord do Python logging
            
        Returns:
            str: JSON string do log
        """
        log_data = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }
        
        # Adicionar campos extras se existirem
        if hasattr(record, "user_id"):
            log_data["user_id"] = record.user_id
        if hasattr(record, "conversation_id"):
            log_data["conversation_id"] = record.conversation_id
        if hasattr(record, "method"):
            log_data["method"] = record.method
        if hasattr(record, "path"):
            log_data["path"] = record.path
        if hasattr(record, "status_code"):
            log_data["status_code"] = record.status_code
        if hasattr(record, "duration_ms"):
            log_data["duration_ms"] = record.duration_ms
        
        return json.dumps(log_data)


def log_structured(level: str, message: str, **kwargs):
    """
    Função helper para logging estruturado.
    
    Args:
        level: Nível do log (INFO, WARNING, ERROR, etc.)
        message: Mensagem do log
        **kwargs: Campos extras para incluir no log
    """
    log_data = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "level": level,
        "message": message,
        **kwargs
    }
    
    log_json = json.dumps(log_data)
    
    logger = logging.getLogger(__name__)
    if level == "ERROR":
        logger.error(log_json)
    elif level == "WARNING":
        logger.warning(log_json)
    else:
        logger.info(log_json)


def setup_logger(name: str = __name__, level: int = logging.INFO) -> logging.Logger:
    """
    Configura um logger com JSONFormatter.
    
    Args:
        name: Nome do logger
        level: Nível de logging (default: INFO)
        
    Returns:
        logging.Logger: Logger configurado
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Remover handlers existentes para evitar duplicação
    logger.handlers.clear()
    
    handler = logging.StreamHandler()
    handler.setFormatter(JSONFormatter())
    logger.addHandler(handler)
    
    return logger

