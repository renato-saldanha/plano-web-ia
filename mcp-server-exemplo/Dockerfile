# Dockerfile para Servidor MCP
FROM python:3.12-slim

# Definir diretório de trabalho
WORKDIR /app

# Copiar requirements primeiro (cache de layers)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código do servidor
COPY server.py .

# Garantir que o script seja executável
RUN chmod +x server.py

# Definir comando padrão
CMD ["python", "server.py"]

