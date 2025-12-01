# 🐳 Servidor MCP de Exemplo com Docker

Este é um exemplo completo de servidor MCP (Model Context Protocol) containerizado com Docker para uso no Cursor.

## 📋 Estrutura

```
mcp-server-exemplo/
├── server.py              # Servidor MCP básico
├── server_avancado.py     # Servidor MCP avançado (com APIs externas)
├── Dockerfile             # Configuração Docker
├── docker-compose.yml     # Orquestração (opcional)
├── requirements.txt       # Dependências Python (básico)
├── requirements_avancado.txt  # Dependências (avançado)
├── testar_local.py        # Script para testar localmente
├── .dockerignore          # Arquivos ignorados no build
└── README.md              # Este arquivo
```

## 🚀 Como Usar

### Opção 1: Servidor Básico

#### 1. Instalar Dependências

```bash
pip install -r requirements.txt
```

#### 2. Testar Localmente (Opcional)

```bash
python testar_local.py
```

#### 3. Construir Imagem Docker

```bash
docker build -t meu-servidor-mcp .
```

#### 4. Testar Container

```bash
docker run -it --rm meu-servidor-mcp
```

### Opção 2: Servidor Avançado

#### 1. Instalar Dependências

```bash
pip install -r requirements_avancado.txt
```

#### 2. Configurar Variáveis de Ambiente (Opcional)

Crie um arquivo `.env`:

```env
OPENWEATHER_API_KEY=sua_chave_aqui
```

#### 3. Construir Imagem Docker

```bash
# Edite o Dockerfile para usar server_avancado.py ou crie um Dockerfile separado
docker build -t meu-servidor-mcp-avancado .
```

### 5. Configurar no Cursor

Adicione ao arquivo de configuração MCP do Cursor:

**Windows:** `%APPDATA%\Cursor\User\globalStorage\saoudrizwan.claude-dev\settings\cline_mcp_settings.json`

**macOS:** `~/Library/Application Support/Cursor/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`

**Linux:** `~/.config/Cursor/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`

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
      "cwd": "D:/plano web+ia/mcp-server-exemplo"
    }
  }
}
```

### 6. Reiniciar Cursor

Após adicionar a configuração, **reinicie o Cursor completamente**.

## 🛠️ Ferramentas Disponíveis

### Servidor Básico (`server.py`)

1. **calcular** - Calcula expressões matemáticas simples
2. **contar_palavras** - Conta palavras e caracteres em um texto
3. **formatar_json** - Formata e valida JSON

### Servidor Avançado (`server_avancado.py`)

1. **buscar_cep** - Busca informações de CEP brasileiro (API ViaCEP)
2. **buscar_clima** - Busca informações do clima (requer OpenWeatherMap API key)
3. **gerar_hash** - Gera hash MD5 ou SHA256 de uma string
4. **validar_email** - Valida formato de email usando regex

## 🧪 Testando

### Testar Localmente (sem Docker)

```bash
python testar_local.py
```

### Testar Protocolo MCP Completo

```bash
python server.py
```

### Testar Container Docker

```bash
docker run -it --rm meu-servidor-mcp
```

## 📖 Documentação Completa

Consulte `../GUIAS/GUIA_MCP_DOCKER.md` para:
- Documentação completa do MCP
- Exemplos avançados
- Troubleshooting
- Melhores práticas

## ⚠️ Notas de Segurança

- ⚠️ O uso de `eval()` na ferramenta `calcular` é apenas para exemplo
- ✅ Em produção, use bibliotecas seguras como `simpleeval` ou `ast.literal_eval`
- 🔒 Não exponha este servidor publicamente sem autenticação adequada
- 🔑 Mantenha API keys seguras (use `.env` e não commite no git)

## 🐛 Troubleshooting

### Cursor não reconhece o servidor

1. Verifique se o arquivo de configuração está no local correto
2. Verifique a sintaxe JSON
3. Reinicie o Cursor completamente
4. Verifique logs do Docker: `docker logs meu-servidor-mcp`

### Docker cria múltiplos containers

Use `--rm` no comando Docker ou pare containers antigos:

```bash
docker stop meu-servidor-mcp 2>/dev/null || true
```

## 📚 Recursos

- [Documentação MCP](https://modelcontextprotocol.io)
- [Documentação Cursor MCP](https://docs.cursor.com/context/mcp)
- [SDK Python MCP](https://github.com/modelcontextprotocol/python-sdk)

