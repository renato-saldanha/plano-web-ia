"""
Hello AI - Primeira Integração com Groq
========================================

Este é o primeiro script do plano de desenvolvimento de 2 meses.
Objetivo: Testar integração básica com Groq API (gratuita e ultra-rápida).

Requisitos:
- pip install groq python-dotenv
- Arquivo .env com GROQ_API_KEY

Autor: Renato Saldanha
Data: 24 Nov 2025
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
prompt2 = "Me diga como funciona um padrão MCP no contexto de IA?"
prompt3 = "Me explique em 3000 palavras como funciona a rede neural de uma IA?"

print(f"💬 Prompt: {prompt3}\n")
print("⏳ Gerando resposta...\n")

# Lista de modelos para tentar (em ordem de preferência)
modelos = [
    "llama-3.1-8b-instant",      # Modelo rápido e eficiente
    "llama-3.1-70b-versatile",   # Modelo mais poderoso
    "mixtral-8x7b-32768",        # Alternativa
]

try:
    # Tentar cada modelo até um funcionar
    chat_completion = None
    modelo_usado = None
    
    for modelo in modelos:
        try:
            print(f"🔄 Tentando modelo: {modelo}...")
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt3
                    }
                ],
                model=modelo,
                temperature=0.7,
                max_tokens=150
            )
            modelo_usado = modelo
            print(f"✅ Modelo {modelo} funcionou!\n")
            break
        except Exception as e:
            if "model_not_found" in str(e) or "404" in str(e):
                print(f"⚠️  Modelo {modelo} não disponível, tentando próximo...\n")
                continue
            else:
                raise
    
    if not chat_completion:
        raise Exception("Nenhum modelo disponível funcionou. Verifique sua conta Groq.")
    
    # Extrair resposta
    resposta = chat_completion.choices[0].message.content
    
    print("=" * 60)
    print("🤖 RESPOSTA DO LLAMA 3.1:")
    print("=" * 60)
    print(resposta)
    print("=" * 60)
    
    # Informações adicionais
    print(f"\n📊 Informações:")
    print(f"   - Modelo usado: {modelo_usado}")
    print(f"   - Tokens usados: {chat_completion.usage.total_tokens}")
    print(f"   - Tempo de resposta: Ultra-rápido! ⚡")
    
    print("\n✅ Primeira integração com IA concluída com sucesso!")
    print("🎉 Parabéns! Você completou o Dia 1!")
    
except Exception as e:
    print(f"❌ Erro ao gerar resposta: {e}")
    print("\n💡 Dicas para resolver:")
    print("   1. Verifique se sua API key está correta no arquivo .env")
    print("   2. Verifique sua conexão com internet")
    print("   3. Consulte modelos disponíveis: https://console.groq.com/docs/models")
    print("   4. Verifique se aceitou os termos de uso no console Groq")
    print("   5. Veja arquivo modelos_groq.md para lista de modelos alternativos")

