"""
Hello AI - Primeira Integração com Groq
========================================

Este é o primeiro script do plano de desenvolvimento de 2 meses.
Objetivo: Testar integração básica com Groq API (gratuita e ultra-rápida).

Requisitos:
- pip install groq python-dotenv
- Arquivo .env com GROQ_API_KEY

Autor: [Seu Nome]
Data: 25 Nov 2024
"""

import os
from dotenv import load_dotenv
from groq import Groq

# Carregar variáveis de ambiente
load_dotenv()

# Obter API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "❌ GROQ_API_KEY não encontrada!\n"
        "Crie um arquivo .env com: GROQ_API_KEY=sua_chave_aqui"
    )

print("✅ API Key encontrada!")
print("🚀 Conectando com Groq...\n")

# Criar cliente Groq
client = Groq(api_key=api_key)

# Prompt de teste
prompt = "Olá! Me apresente em 2 frases. Qual é seu nome e o que você pode fazer?"

print(f"💬 Prompt: {prompt}\n")
print("⏳ Gerando resposta...\n")

try:
    # Fazer chamada à API
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="llama-3.2-3b-instruct",  # Modelo gratuito e rápido
        temperature=0.7,
        max_tokens=150
    )
    
    # Extrair resposta
    resposta = chat_completion.choices[0].message.content
    
    print("=" * 60)
    print("🤖 RESPOSTA DO LLAMA 3.2:")
    print("=" * 60)
    print(resposta)
    print("=" * 60)
    
    # Informações adicionais
    print(f"\n📊 Informações:")
    print(f"   - Modelo: {chat_completion.model}")
    print(f"   - Tokens usados: {chat_completion.usage.total_tokens}")
    print(f"   - Tempo de resposta: Ultra-rápido! ⚡")
    
    print("\n✅ Primeira integração com IA concluída com sucesso!")
    print("🎉 Parabéns! Você completou o Dia 1!")
    
except Exception as e:
    print(f"❌ Erro ao gerar resposta: {e}")
    print("\n💡 Dicas:")
    print("   - Verifique se sua API key está correta")
    print("   - Verifique sua conexão com internet")
    print("   - Consulte: https://console.groq.com/docs")

