#!/usr/bin/env python3
"""
Script para testar o servidor MCP localmente
Útil para debug antes de containerizar

NOTA: Este script testa as ferramentas diretamente.
Para testar o protocolo MCP completo, execute: python server.py
"""

import asyncio
import json
import sys
from typing import Any, Sequence
from mcp.types import Tool, TextContent

# Simular as funções do servidor para teste
async def calcular(expressao: str) -> str:
    """Calcula uma expressão matemática."""
    try:
        resultado = eval(expressao)  # ⚠️ Apenas para teste
        return f"✅ Resultado: {resultado}"
    except Exception as e:
        return f"❌ Erro ao calcular '{expressao}': {e}"

async def contar_palavras(texto: str) -> str:
    """Conta palavras em um texto."""
    palavras = len(texto.split())
    caracteres = len(texto)
    caracteres_sem_espaco = len(texto.replace(" ", ""))
    
    return f"""
📊 Estatísticas do texto:
- Palavras: {palavras}
- Caracteres (total): {caracteres}
- Caracteres (sem espaços): {caracteres_sem_espaco}
""".strip()

async def formatar_json(json_string: str) -> str:
    """Formata e valida um JSON."""
    try:
        obj = json.loads(json_string)
        json_formatado = json.dumps(obj, indent=2, ensure_ascii=False)
        return f"✅ JSON válido e formatado:\n\n```json\n{json_formatado}\n```"
    except json.JSONDecodeError as e:
        return f"❌ JSON inválido: {e}"
    except Exception as e:
        return f"❌ Erro: {e}"

async def testar_ferramentas():
    """Testa as ferramentas do servidor MCP."""
    print("🧪 Testando Servidor MCP\n")
    print("=" * 60)
    
    # Listar ferramentas
    print("\n📋 Ferramentas disponíveis:")
    print("  - calcular: Calcula uma expressão matemática simples")
    print("  - contar_palavras: Conta palavras em um texto")
    print("  - formatar_json: Formata e valida um JSON")
    
    print("\n" + "=" * 60)
    
    # Testar calcular
    print("\n🧮 Testando 'calcular':")
    resultado = await calcular("15 * 23")
    print(f"  {resultado}")
    
    # Testar contar_palavras
    print("\n📊 Testando 'contar_palavras':")
    resultado = await contar_palavras("Este é um texto de exemplo para contar palavras")
    print(f"  {resultado}")
    
    # Testar formatar_json
    print("\n📝 Testando 'formatar_json':")
    json_test = '{"nome":"João","idade":30,"cidade":"São Paulo"}'
    resultado = await formatar_json(json_test)
    print(f"  {resultado}")
    
    print("\n" + "=" * 60)
    print("✅ Todos os testes concluídos!")
    print("\n💡 Para testar o protocolo MCP completo, execute: python server.py")

if __name__ == "__main__":
    try:
        asyncio.run(testar_ferramentas())
    except KeyboardInterrupt:
        print("\n\n⚠️ Teste cancelado pelo usuário.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Erro durante teste: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

