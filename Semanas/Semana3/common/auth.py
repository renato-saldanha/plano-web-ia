"""
Módulo de autenticação JWT.

Fornece funções para criação, verificação e uso de tokens JWT.
"""

import os
from datetime import datetime, timedelta, timezone
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configurações JWT
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY") or os.getenv("JWT_SECRET")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM") or os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", "7"))

# Configurar OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def verify_token(token: str, expected_type: str = "access") -> dict:
    """
    Verifica e decodifica um token JWT.
    
    Args:
        token: Token JWT a verificar
        expected_type: Tipo esperado do token ("access" ou "refresh")
        
    Returns:
        dict: Payload decodificado do token
        
    Raises:
        HTTPException: Se token inválido, expirado ou tipo incorreto
    """
    if not JWT_SECRET_KEY:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="JWT_SECRET_KEY não configurada"
        )
    
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        if payload.get("type") != expected_type:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Tipo de token inválido. Esperado: {expected_type}"
            )
        return payload
    except JWTError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Token inválido: {exc}"
        ) from exc


async def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    """
    Dependency que extrai e valida o usuário atual do token.
    
    Esta função é usada com Depends() em rotas protegidas.
    
    Args:
        token: Token JWT extraído automaticamente pelo oauth2_scheme
        
    Returns:
        dict: Informações do usuário autenticado {"username": str, "payload": dict}
        
    Raises:
        HTTPException: Se token inválido ou usuário não encontrado
    """
    payload = verify_token(token, expected_type="access")
    username = payload.get("sub")
    if not username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário não autorizado"
        )
    return {"username": username, "payload": payload}


def create_access_token(data: dict) -> str:
    """
    Cria um access token JWT.
    
    Args:
        data: Dados a incluir no payload do token
        
    Returns:
        str: Token JWT codificado
    """
    if not JWT_SECRET_KEY:
        raise ValueError("JWT_SECRET_KEY não configurada")
    
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({
        "exp": int(expire.timestamp()),
        "type": "access"
    })
    return jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)


def create_refresh_token(data: dict) -> str:
    """
    Cria um refresh token JWT com expiração mais longa.
    
    Args:
        data: Dados a incluir no payload do token
        
    Returns:
        str: Token JWT codificado
    """
    if not JWT_SECRET_KEY:
        raise ValueError("JWT_SECRET_KEY não configurada")
    
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({
        "exp": int(expire.timestamp()),
        "type": "refresh"
    })
    return jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)

