# 🐳 Guia Completo: Criar Servidor MCP Local com Docker para Cursor

Este guia mostra como criar um servidor MCP (Model Context Protocol) local, containerizá-lo com Docker e configurá-lo no Cursor.

---

## 📋 O que é MCP?

**MCP (Model Context Protocol)** é um protocolo desenvolvido pela Anthropic que permite que o Cursor se conecte a ferramentas e fontes de dados externas, ampliando suas funcionalidades.

**Benefícios:**
- ✅ Conectar o Cursor a APIs personalizadas
- ✅ Acessar bancos de dados locais
- ✅ Criar ferramentas customizadas para IA
- ✅ Integrar com serviços internos da empresa

---

## 🎯 Estrutura do Projeto

Vamos criar um servidor MCP simples que oferece ferramentas úteis:

```
mcp-server/
├── server.py          # Servidor MCP principal
├── Dockerfile         # Configuração Docker
├── docker-compose.yml # Orquestração (opcional)
├── requirements.txt   # Dependências Python
├── .env.example       # Exemplo de variáveis de ambiente
└── README.md          # Documentação
```

---

## 📝 Passo 1: Criar Servidor MCP em Python

### 1.1 Instalar SDK do MCP

```bash
pip install mcp
```

### 1.2 Criar Servidor Básico

O servidor MCP precisa:
- Escutar em `stdio` (entrada/saída padrão)
- Implementar o protocolo MCP
- Expor ferramentas (tools) e recursos (resources)

**Exemplo de servidor MCP simples:**

```python
#!/usr/bin/env python3
"""
Servidor MCP de Exemplo
Expõe ferramentas úteis para o Cursor
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
            description="Calcula uma expressão matemática",
            inputSchema={
                "type": "object",
                "properties": {
                    "expressao": {
                        "type": "string",
                        "description": "Expressão matemática a calcular (ex: '2+2', '10*5')"
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
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> Sequence[TextContent]:
    """Executa uma ferramenta."""
    if name == "calcular":
        expressao = arguments.get("expressao", "")
        try:
            resultado = eval(expressao)  # ⚠️ Usar com cuidado em produção!
            return [TextContent(
                type="text",
                text=f"Resultado: {resultado}"
            )]
        except Exception as e:
            return [TextContent(
                type="text",
                text=f"Erro ao calcular: {e}"
            )]
    
    elif name == "contar_palavras":
        texto = arguments.get("texto", "")
        palavras = len(texto.split())
        return [TextContent(
            type="text",
            text=f"Total de palavras: {palavras}"
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
    asyncio.run(main())
```

---

## 🐳 Passo 2: Criar Dockerfile

```dockerfile
# Dockerfile para Servidor MCP
FROM python:3.12-slim

# Definir diretório de trabalho
WORKDIR /app

# Copiar requirements primeiro (cache de layers)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código do servidor
COPY server.py .

# Definir comando padrão
CMD ["python", "server.py"]
```

---

## 📦 Passo 3: Criar requirements.txt

```txt
mcp>=0.1.0
```

---

## 🐙 Passo 4: Criar docker-compose.yml (Opcional)

```yaml
version: '3.8'

services:
  mcp-server:
    build: .
    container_name: meu-servidor-mcp
    stdin_open: true
    tty: true
    environment:
      - PYTHONUNBUFFERED=1
    # Se precisar de variáveis de ambiente:
    # env_file:
    #   - .env
```

---

## 🔧 Passo 5: Construir e Testar Docker

### 5.1 Construir Imagem

```bash
docker build -t meu-servidor-mcp .
```

### 5.2 Testar Localmente

```bash
# Testar execução do container
docker run -it --rm meu-servidor-mcp

# Ou com docker-compose
docker-compose up
```

---

## ⚙️ Passo 6: Configurar no Cursor

### 6.1 Localizar Arquivo de Configuração

O Cursor usa um arquivo de configuração MCP. Localização típica:

**Windows:**
```
%APPDATA%\Cursor\User\globalStorage\saoudrizwan.claude-dev\settings\cline_mcp_settings.json
```

**macOS:**
```
~/Library/Application Support/Cursor/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json
```

**Linux:**
```
~/.config/Cursor/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json
```

### 6.2 Adicionar Configuração

Adicione seu servidor MCP ao arquivo de configuração:

```json
{
  "mcpServers": {
    "meu-servidor-mcp": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "meu-servidor-mcp"
      ]
    }
  }
}
```

**Ou usando docker-compose:**

```json
{
  "mcpServers": {
    "meu-servidor-mcp": {
      "command": "docker-compose",
      "args": [
        "run",
        "--rm",
        "mcp-server"
      ],
      "cwd": "/caminho/para/seu/projeto/mcp-server"
    }
  }
}
```

### 6.3 Reiniciar Cursor

Após adicionar a configuração, **reinicie o Cursor** para que ele reconheça o novo servidor MCP.

---

## 🧪 Passo 7: Testar no Cursor

Após reiniciar o Cursor:

1. Abra o chat do Cursor
2. Digite algo como: "Use a ferramenta calcular para calcular 15 * 23"
3. O Cursor deve usar seu servidor MCP automaticamente

---

## 📚 Exemplo Avançado: Servidor MCP com API Externa

Aqui está um exemplo mais completo que integra com APIs externas:

```python
#!/usr/bin/env python3
"""
Servidor MCP Avançado
Integra com APIs externas e oferece mais funcionalidades
"""

import asyncio
import os
import httpx
from typing import Any, Sequence
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent
from dotenv import load_dotenv

load_dotenv()

server = Server("servidor-mcp-avancado")

@server.list_tools()
async def list_tools() -> list[Tool]:
    """Lista todas as ferramentas disponíveis."""
    return [
        Tool(
            name="buscar_cep",
            description="Busca informações de um CEP brasileiro",
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
            name="converter_moeda",
            description="Converte valores entre moedas usando API pública",
            inputSchema={
                "type": "object",
                "properties": {
                    "valor": {"type": "number", "description": "Valor a converter"},
                    "de": {"type": "string", "description": "Moeda origem (ex: USD)"},
                    "para": {"type": "string", "description": "Moeda destino (ex: BRL)"}
                },
                "required": ["valor", "de", "para"]
            }
        ),
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> Sequence[TextContent]:
    """Executa uma ferramenta."""
    if name == "buscar_cep":
        cep = arguments.get("cep", "").replace("-", "")
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"https://viacep.com.br/ws/{cep}/json/")
                if response.status_code == 200:
                    data = response.json()
                    if "erro" not in data:
                        resultado = f"""
CEP: {data.get('cep', 'N/A')}
Logradouro: {data.get('logradouro', 'N/A')}
Bairro: {data.get('bairro', 'N/A')}
Cidade: {data.get('localidade', 'N/A')}
Estado: {data.get('uf', 'N/A')}
"""
                        return [TextContent(type="text", text=resultado)]
                    else:
                        return [TextContent(type="text", text="CEP não encontrado")]
                else:
                    return [TextContent(type="text", text=f"Erro na API: {response.status_code}")]
        except Exception as e:
            return [TextContent(type="text", text=f"Erro: {e}")]
    
    elif name == "converter_moeda":
        valor = arguments.get("valor", 0)
        de = arguments.get("de", "USD")
        para = arguments.get("para", "BRL")
        # Implementar conversão usando API pública
        return [TextContent(type="text", text=f"Conversão de {valor} {de} para {para}")]
    
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
    asyncio.run(main())
```

**requirements.txt atualizado:**

```txt
mcp>=0.1.0
httpx>=0.25.0
python-dotenv>=1.0.0
```

---

## 🚨 Troubleshooting

### Problema: Cursor não reconhece o servidor MCP

**Solução:**
1. Verifique se o arquivo de configuração está no local correto
2. Verifique a sintaxe JSON (use um validador JSON)
3. Reinicie o Cursor completamente
4. Verifique os logs do Cursor para erros

### Problema: Docker cria múltiplos containers

**Solução:**
Use `--rm` no comando Docker para remover automaticamente:

```json
{
  "mcpServers": {
    "meu-servidor-mcp": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "--name", "meu-servidor-mcp-unico",
        "meu-servidor-mcp"
      ]
    }
  }
}
```

Ou pare containers antigos antes:

```bash
docker stop meu-servidor-mcp-unico 2>/dev/null || true
```

### Problema: Servidor não responde

**Solução:**
1. Teste o servidor localmente primeiro: `python server.py`
2. Teste o container: `docker run -it meu-servidor-mcp`
3. Verifique se o servidor está usando `stdio` corretamente
4. Verifique logs do Docker: `docker logs meu-servidor-mcp-unico`

---

## 📖 Recursos Adicionais

- **Documentação MCP:** https://modelcontextprotocol.io
- **Documentação Cursor MCP:** https://docs.cursor.com/context/mcp
- **SDK Python MCP:** https://github.com/modelcontextprotocol/python-sdk

---

## ✅ Checklist de Implementação

- [ ] Criar servidor MCP em Python
- [ ] Criar Dockerfile
- [ ] Criar requirements.txt
- [ ] Construir imagem Docker
- [ ] Testar container localmente
- [ ] Configurar no Cursor (mcp.json)
- [ ] Reiniciar Cursor
- [ ] Testar ferramentas no chat do Cursor
- [ ] Adicionar mais ferramentas conforme necessário

---

**Última atualização:** Dezembro 2025

