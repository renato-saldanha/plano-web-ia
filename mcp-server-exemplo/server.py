#!/usr/bin/env python3
"""
Servidor MCP de Exemplo
Expõe ferramentas úteis para o Cursor

Este servidor implementa o protocolo MCP e oferece ferramentas que podem
ser usadas pelo Cursor através do chat.
"""

import asyncio
import json
import sys
from typing import Any, Sequence
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

# Criar servidor MCP
server = Server("meu-servidor-mcp")

@server.list_tools()
async def list_tools() -> list[Tool]:
    """Lista todas as ferramentas disponíveis."""
    return [
        Tool(
            name="calcular",
            description="Calcula uma expressão matemática simples",
            inputSchema={
                "type": "object",
                "properties": {
                    "expressao": {
                        "type": "string",
                        "description": "Expressão matemática a calcular (ex: '2+2', '10*5', '100/4')"
                    }
                },
                "required": ["expressao"]
            }
        ),
        Tool(
            name="contar_palavras",
            description="Conta palavras em um texto",
            inputSchema={
                "type": "object",
                "properties": {
                    "texto": {
                        "type": "string",
                        "description": "Texto para contar palavras"
                    }
                },
                "required": ["texto"]
            }
        ),
        Tool(
            name="formatar_json",
            description="Formata e valida um JSON",
            inputSchema={
                "type": "object",
                "properties": {
                    "json_string": {
                        "type": "string",
                        "description": "String JSON para formatar"
                    }
                },
                "required": ["json_string"]
            }
        ),
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> Sequence[TextContent]:
    """Executa uma ferramenta."""
    if name == "calcular":
        expressao = arguments.get("expressao", "")
        try:
            # ⚠️ AVISO: eval() é perigoso em produção!
            # Em produção, use uma biblioteca como 'simpleeval' ou 'ast.literal_eval'
            resultado = eval(expressao)
            return [TextContent(
                type="text",
                text=f"✅ Resultado: {resultado}"
            )]
        except Exception as e:
            return [TextContent(
                type="text",
                text=f"❌ Erro ao calcular '{expressao}': {e}"
            )]
    
    elif name == "contar_palavras":
        texto = arguments.get("texto", "")
        palavras = len(texto.split())
        caracteres = len(texto)
        caracteres_sem_espaco = len(texto.replace(" ", ""))
        
        resultado = f"""
📊 Estatísticas do texto:
- Palavras: {palavras}
- Caracteres (total): {caracteres}
- Caracteres (sem espaços): {caracteres_sem_espaco}
"""
        return [TextContent(
            type="text",
            text=resultado.strip()
        )]
    
    elif name == "formatar_json":
        json_string = arguments.get("json_string", "")
        try:
            # Parse e formatar JSON
            obj = json.loads(json_string)
            json_formatado = json.dumps(obj, indent=2, ensure_ascii=False)
            return [TextContent(
                type="text",
                text=f"✅ JSON válido e formatado:\n\n```json\n{json_formatado}\n```"
            )]
        except json.JSONDecodeError as e:
            return [TextContent(
                type="text",
                text=f"❌ JSON inválido: {e}"
            )]
        except Exception as e:
            return [TextContent(
                type="text",
                text=f"❌ Erro: {e}"
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

