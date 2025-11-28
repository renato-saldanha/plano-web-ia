"""
EXEMPLO: Analisador de Sentimentos com Múltiplos LLMs
======================================================

Este é um EXEMPLO/REFERÊNCIA para o Dia 3.
Você deve criar seu próprio script seguindo as instruções do checklist.md

Objetivo: Analisar sentimentos de reviews usando múltiplos LLMs e comparar resultados.

Requisitos:
- pip install groq google-generativeai anthropic python-dotenv
- Arquivo .env com:
  - GROQ_API_KEY
  - GEMINI_API_KEY
  - ANTHROPIC_API_KEY (opcional)

Autor: Referência para Dia 3
Data: 26 Nov 2024
"""

import os
import time
from dotenv import load_dotenv
from groq import Groq

# Carregar variáveis de ambiente
load_dotenv()

# ========================================
# EXEMPLO: Análise com Groq
# ========================================

def analisar_sentimento_groq(texto: str) -> dict:
    """
    Analisa sentimento usando Groq API.
    
    Retorna:
        dict: {
            'sentimento': 'positivo' | 'negativo' | 'neutro',
            'tempo_ms': float,
            'tokens': int
        }
    """
    try:
        groq_api_key = os.getenv("GROQ_API_KEY")
        if not groq_api_key:
            raise ValueError("GROQ_API_KEY não encontrada no .env")
        
        client = Groq(api_key=groq_api_key)
        
        prompt = f"""Analise o sentimento do seguinte texto e retorne APENAS uma palavra: "positivo", "negativo" ou "neutro".

Texto: {texto}

Sentimento:"""
        
        inicio_ms = time.perf_counter() * 1000
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,  # Baixa temperatura para respostas mais consistentes
            max_tokens=10
        )
        
        fim_ms = time.perf_counter() * 1000
        tempo_resposta_ms = fim_ms - inicio_ms
        
        sentimento = response.choices[0].message.content.strip().lower()
        
        # Normalizar resposta (pode vir como "positivo.", "Positivo", etc)
        if "positivo" in sentimento:
            sentimento = "positivo"
        elif "negativo" in sentimento:
            sentimento = "negativo"
        elif "neutro" in sentimento:
            sentimento = "neutro"
        else:
            sentimento = "neutro"  # Fallback
        
        return {
            'sentimento': sentimento,
            'tempo_ms': tempo_resposta_ms,
            'tokens': response.usage.total_tokens,
            'modelo': response.model
        }
    except Exception as e:
        print(f"Erro ao analisar com Groq: {e}")
        return None

# ========================================
# EXEMPLO: Análise com Gemini
# ========================================

def analisar_sentimento_gemini(texto: str) -> dict:
    """
    Analisa sentimento usando Google Gemini API.
    
    Retorna:
        dict: {
            'sentimento': 'positivo' | 'negativo' | 'neutro',
            'tempo_ms': float,
            'tokens': int
        }
    """
    try:
        import google.generativeai as genai
        
        gemini_api_key = os.getenv("GEMINI_API_KEY")
        if not gemini_api_key:
            raise ValueError("GEMINI_API_KEY não encontrada no .env")
        
        genai.configure(api_key=gemini_api_key)
        model = genai.GenerativeModel('gemini-pro')
        
        prompt = f"""Analise o sentimento do seguinte texto e retorne APENAS uma palavra: "positivo", "negativo" ou "neutro".

Texto: {texto}

Sentimento:"""
        
        inicio_ms = time.perf_counter() * 1000
        
        response = model.generate_content(prompt)
        
        fim_ms = time.perf_counter() * 1000
        tempo_resposta_ms = fim_ms - inicio_ms
        
        sentimento = response.text.strip().lower()
        
        # Normalizar resposta
        if "positivo" in sentimento:
            sentimento = "positivo"
        elif "negativo" in sentimento:
            sentimento = "negativo"
        elif "neutro" in sentimento:
            sentimento = "neutro"
        else:
            sentimento = "neutro"
        
        # Gemini não retorna tokens diretamente na mesma estrutura
        return {
            'sentimento': sentimento,
            'tempo_ms': tempo_resposta_ms,
            'tokens': 0,  # Ajustar conforme disponibilidade da API
            'modelo': 'gemini-pro'
        }
    except Exception as e:
        print(f"Erro ao analisar com Gemini: {e}")
        return None

# ========================================
# EXEMPLO: Função de Comparação
# ========================================

def comparar_analises(texto: str) -> dict:
    """
    Compara análise de sentimentos entre múltiplos LLMs.
    
    Retorna:
        dict: {
            'texto': str,
            'groq': dict,
            'gemini': dict,
            'concordancia': bool,
            'sentimentos': list
        }
    """
    print(f"\n📝 Analisando: {texto[:50]}...")
    
    resultado_groq = analisar_sentimento_groq(texto)
    resultado_gemini = analisar_sentimento_gemini(texto)
    
    # Verificar concordância
    concordancia = False
    sentimentos = []
    
    if resultado_groq:
        sentimentos.append(resultado_groq['sentimento'])
    if resultado_gemini:
        sentimentos.append(resultado_gemini['sentimento'])
    
    if len(set(sentimentos)) == 1:
        concordancia = True
    
    return {
        'texto': texto,
        'groq': resultado_groq,
        'gemini': resultado_gemini,
        'concordancia': concordancia,
        'sentimentos': sentimentos
    }

# ========================================
# EXEMPLO: Teste Rápido
# ========================================

if __name__ == "__main__":
    print("🧪 Teste Rápido - Analisador de Sentimentos\n")
    
    review_teste = "Este produto é incrível! Funciona perfeitamente."
    
    resultado = comparar_analises(review_teste)
    
    print("\n" + "=" * 60)
    print("📊 RESULTADO DA COMPARAÇÃO:")
    print("=" * 60)
    print(f"Review: {resultado['texto']}")
    print(f"\nGroq: {resultado['groq']['sentimento'] if resultado['groq'] else 'Erro'}")
    print(f"Gemini: {resultado['gemini']['sentimento'] if resultado['gemini'] else 'Erro'}")
    print(f"Concordância: {'✅ SIM' if resultado['concordancia'] else '❌ NÃO'}")
    print("=" * 60)
    
    print("\n💡 Este é apenas um exemplo!")
    print("📋 Siga o checklist.md para criar seu script completo.")

