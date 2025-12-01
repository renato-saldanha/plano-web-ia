#!/usr/bin/env python3
"""
Servidor MCP Avançado
Integra com APIs externas e oferece mais funcionalidades

Este exemplo mostra como criar um servidor MCP mais completo que:
- Integra com APIs externas
- Usa variáveis de ambiente
- Oferece múltiplas ferramentas úteis
"""

import asyncio
import json
import os
import sys
from typing import Any, Sequence
import httpx
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Criar servidor MCP
server = Server("servidor-mcp-avancado")

@server.list_tools()
async def list_tools() -> list[Tool]:
    """Lista todas as ferramentas disponíveis."""
    return [
        Tool(
            name="buscar_cep",
            description="Busca informações de um CEP brasileiro usando a API ViaCEP",
            inputSchema={
                "type": "object",
                "properties": {
                    "cep": {
                        "type": "string",
                        "description": "CEP a buscar (formato: 12345678 ou 12345-678)"
                    }
                },
                "required": ["cep"]
            }
        ),
        Tool(
            name="buscar_clima",
            description="Busca informações do clima de uma cidade (exemplo com OpenWeatherMap)",
            inputSchema={
                "type": "object",
                "properties": {
                    "cidade": {
                        "type": "string",
                        "description": "Nome da cidade"
                    },
                    "pais": {
                        "type": "string",
                        "description": "Código do país (ex: 'br', 'us')",
                        "default": "br"
                    }
                },
                "required": ["cidade"]
            }
        ),
        Tool(
            name="gerar_hash",
            description="Gera hash MD5 ou SHA256 de uma string",
            inputSchema={
                "type": "object",
                "properties": {
                    "texto": {
                        "type": "string",
                        "description": "Texto para gerar hash"
                    },
                    "algoritmo": {
                        "type": "string",
                        "enum": ["md5", "sha256"],
                        "description": "Algoritmo de hash a usar",
                        "default": "sha256"
                    }
                },
                "required": ["texto"]
            }
        ),
        Tool(
            name="validar_email",
            description="Valida formato de email usando regex",
            inputSchema={
                "type": "object",
                "properties": {
                    "email": {
                        "type": "string",
                        "description": "Email a validar"
                    }
                },
                "required": ["email"]
            }
        ),
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> Sequence[TextContent]:
    """Executa uma ferramenta."""
    if name == "buscar_cep":
        cep = arguments.get("cep", "").replace("-", "").replace(" ", "")
        if len(cep) != 8 or not cep.isdigit():
            return [TextContent(
                type="text",
                text="❌ CEP inválido. Use formato: 12345678 ou 12345-678"
            )]
        
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(f"https://viacep.com.br/ws/{cep}/json/")
                if response.status_code == 200:
                    data = response.json()
                    if "erro" not in data:
                        resultado = f"""
📍 Informações do CEP {data.get('cep', 'N/A')}:

🏠 Logradouro: {data.get('logradouro', 'N/A')}
🏘️ Bairro: {data.get('bairro', 'N/A')}
🏙️ Cidade: {data.get('localidade', 'N/A')}
🗺️ Estado: {data.get('uf', 'N/A')}
📮 CEP: {data.get('cep', 'N/A')}
"""
                        return [TextContent(type="text", text=resultado.strip())]
                    else:
                        return [TextContent(type="text", text="❌ CEP não encontrado")]
                else:
                    return [TextContent(
                        type="text",
                        text=f"❌ Erro na API: Status {response.status_code}"
                    )]
        except httpx.TimeoutException:
            return [TextContent(type="text", text="❌ Timeout ao buscar CEP")]
        except Exception as e:
            return [TextContent(type="text", text=f"❌ Erro: {e}")]
    
    elif name == "buscar_clima":
        cidade = arguments.get("cidade", "")
        pais = arguments.get("pais", "br")
        
        # Nota: Para usar OpenWeatherMap, você precisa de uma API key
        # Este é um exemplo que mostra a estrutura
        api_key = os.getenv("OPENWEATHER_API_KEY")
        
        if not api_key:
            return [TextContent(
                type="text",
                text="⚠️ API key do OpenWeatherMap não configurada. Configure OPENWEATHER_API_KEY no .env"
            )]
        
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                url = f"http://api.openweathermap.org/data/2.5/weather"
                params = {
                    "q": f"{cidade},{pais}",
                    "appid": api_key,
                    "units": "metric",
                    "lang": "pt_br"
                }
                response = await client.get(url, params=params)
                
                if response.status_code == 200:
                    data = response.json()
                    resultado = f"""
🌤️ Clima em {data.get('name', cidade)}:

🌡️ Temperatura: {data['main']['temp']}°C
🌡️ Sensação: {data['main']['feels_like']}°C
📊 Umidade: {data['main']['humidity']}%
💨 Vento: {data['wind']['speed']} m/s
☁️ Condição: {data['weather'][0]['description'].title()}
"""
                    return [TextContent(type="text", text=resultado.strip())]
                else:
                    return [TextContent(
                        type="text",
                        text=f"❌ Erro ao buscar clima: {response.status_code}"
                    )]
        except Exception as e:
            return [TextContent(type="text", text=f"❌ Erro: {e}")]
    
    elif name == "gerar_hash":
        texto = arguments.get("texto", "")
        algoritmo = arguments.get("algoritmo", "sha256").lower()
        
        import hashlib
        
        try:
            if algoritmo == "md5":
                hash_obj = hashlib.md5(texto.encode())
            elif algoritmo == "sha256":
                hash_obj = hashlib.sha256(texto.encode())
            else:
                return [TextContent(
                    type="text",
                    text=f"❌ Algoritmo inválido: {algoritmo}. Use 'md5' ou 'sha256'"
                )]
            
            hash_hex = hash_obj.hexdigest()
            return [TextContent(
                type="text",
                text=f"✅ Hash {algoritmo.upper()} de '{texto}':\n\n{hash_hex}"
            )]
        except Exception as e:
            return [TextContent(type="text", text=f"❌ Erro: {e}")]
    
    elif name == "validar_email":
        email = arguments.get("email", "")
        
        import re
        
        # Regex simples para validação de email
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if re.match(pattern, email):
            return [TextContent(
                type="text",
                text=f"✅ Email válido: {email}"
            )]
        else:
            return [TextContent(
                type="text",
                text=f"❌ Email inválido: {email}"
            )]
    
    else:
        raise ValueError(f"Ferramenta desconhecida: {name}")

async def main():
    """Função principal do servidor."""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Servidor MCP encerrado pelo usuário", file=sys.stderr)
        sys.exit(0)
    except Exception as e:
        print(f"Erro no servidor MCP: {e}", file=sys.stderr)
        sys.exit(1)

