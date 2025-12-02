#!/usr/bin/env python3
"""
Exemplo Básico de LangChain
===========================

Este script demonstra uso básico do LangChain para criar
aplicações com LLMs de forma mais simples que código manual.

Comparação:
- Semana 1: Código manual com APIs diretas
- Semana 2: LangChain (framework profissional)

Requisitos:
- pip install langchain langchain-groq langchain-google-genai python-dotenv
- Arquivo .env com API keys (GROQ_API_KEY, GEMINI_API_KEY)

Autor: Baseado no plano de desenvolvimento
Data: 1 Dez 2025
"""

# ============================================================================
# SEÇÃO 1: IMPORTS E CONFIGURAÇÃO
# ============================================================================
# Por que precisamos destes imports:
# - os: Para acessar variáveis de ambiente
# - dotenv: Para carregar arquivo .env com API keys
# - langchain_groq: Integração do LangChain com Groq
# - langchain_google_genai: Integração do LangChain com Gemini
# - langchain_core.messages: Classes para mensagens estruturadas

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

# PASSO 1: Carregar variáveis de ambiente
# O arquivo .env deve estar na raiz do projeto
load_dotenv()

print("✅ Variáveis de ambiente carregadas!")
print()

# ============================================================================
# SEÇÃO 2: EXEMPLO BÁSICO (EQUIVALENTE AO hello_ai_groq.py DA SEMANA 1)
# ============================================================================

def exemplo_basico_groq():
    """
    Exemplo básico usando Groq com LangChain.
    
    Equivalente ao hello_ai_groq.py da Semana 1, mas usando LangChain.
    
    Comparação:
    - Semana 1: ~10 linhas, precisa entender estrutura da API Groq
    - Semana 2: ~5 linhas, sintaxe mais simples e intuitiva
    """
    print("=" * 60)
    print("EXEMPLO 1: Hello LangChain com Groq")
    print("=" * 60)
    print()
    
    # PASSO 1: Obter API key do ambiente
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key:
        print("❌ GROQ_API_KEY não encontrada!")
        print("   Crie um arquivo .env com: GROQ_API_KEY=sua_chave_aqui")
        return
    
    # PASSO 2: Criar instância do LLM usando LangChain
    # ChatGroq é a classe do LangChain para usar Groq
    # Parâmetros:
    # - model: Qual modelo usar (mesmos da Semana 1)
    # - temperature: Criatividade (0.0 = determinístico, 1.0 = muito criativo)
    # - api_key: Sua chave da API (opcional se estiver no .env)
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",  # Modelo rápido e eficiente
        temperature=0.7,                # Balanceado (padrão recomendado)
        api_key=api_key                 # API key (opcional se estiver no .env)
    )
    
    print("✅ LLM Groq criado com LangChain!")
    print()
    
    # PASSO 3: Criar mensagem usando HumanMessage
    # HumanMessage representa uma mensagem do usuário
    # No LangChain, mensagens são objetos estruturados, não apenas strings
    message = HumanMessage(content="Olá! Me apresente em 2 frases. Qual é seu nome e o que você pode fazer?")
    
    print(f"💬 Prompt: {message.content}")
    print()
    print("⏳ Gerando resposta com LangChain...")
    print()
    
    # PASSO 4: Invocar LLM usando método invoke()
    # invoke() recebe uma lista de mensagens e retorna resposta
    # Muito mais simples que código manual da Semana 1!
    try:
        response = llm.invoke([message])
        
        # PASSO 5: Acessar conteúdo da resposta
        # response é um objeto AIMessage, conteúdo está em .content
        resposta = response.content
        
        print("=" * 60)
        print("🤖 RESPOSTA DO LLM:")
        print("=" * 60)
        print(resposta)
        print("=" * 60)
        print()
        
        print("✅ Exemplo básico concluído!")
        print()
        
    except Exception as e:
        print(f"❌ Erro ao gerar resposta: {e}")
        print("\n💡 Dicas para resolver:")
        print("   1. Verifique se sua API key está correta no .env")
        print("   2. Verifique sua conexão com internet")
        print("   3. Consulte modelos disponíveis: https://console.groq.com/docs/models")


# ============================================================================
# SEÇÃO 3: EXEMPLO COM PROMPTS ESTRUTURADOS
# ============================================================================

def exemplo_com_system_message():
    """
    Exemplo usando SystemMessage para definir comportamento do LLM.
    
    SystemMessage permite definir "personalidade" ou "instruções" para o LLM.
    Útil para criar assistentes especializados.
    """
    print("=" * 60)
    print("EXEMPLO 2: LangChain com SystemMessage")
    print("=" * 60)
    print()
    
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key:
        print("❌ GROQ_API_KEY não encontrada!")
        return
    
    # Criar LLM
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.7,
        api_key=api_key
    )
    
    # PASSO 1: Criar SystemMessage
    # SystemMessage define instruções para o LLM
    # Neste caso, estamos criando um assistente de programação Python
    system_message = SystemMessage(
        content="Você é um assistente especializado em Python. "
                "Sempre responda de forma clara e didática, "
                "incluindo exemplos de código quando apropriado."
    )
    
    # PASSO 2: Criar HumanMessage (mensagem do usuário)
    user_message = HumanMessage(
        content="Explique o que são list comprehensions em Python. "
                "Dê um exemplo prático."
    )
    
    print(f"💬 System Message: {system_message.content[:50]}...")
    print(f"💬 User Message: {user_message.content}")
    print()
    print("⏳ Gerando resposta...")
    print()
    
    # PASSO 3: Invocar LLM com ambas as mensagens
    # A ordem importa: SystemMessage primeiro, depois HumanMessage
    try:
        response = llm.invoke([system_message, user_message])
        
        print("=" * 60)
        print("🤖 RESPOSTA DO ASSISTENTE PYTHON:")
        print("=" * 60)
        print(response.content)
        print("=" * 60)
        print()
        
        print("✅ Exemplo com SystemMessage concluído!")
        print()
        
    except Exception as e:
        print(f"❌ Erro: {e}")


# ============================================================================
# SEÇÃO 4: TROCAR LLM FACILMENTE (VANTAGEM DO LANGCHAIN)
# ============================================================================

def exemplo_trocar_llm():
    """
    Demonstra como trocar de LLM facilmente com LangChain.
    
    Vantagem do LangChain:
    - Trocar de Groq para Gemini = mudar apenas a classe
    - Resto do código permanece igual!
    
    No código manual (Semana 1), precisaria reescrever tudo.
    """
    print("=" * 60)
    print("EXEMPLO 3: Trocar LLM Facilmente")
    print("=" * 60)
    print()
    
    # EXEMPLO A: Usar Groq
    print("🔄 Testando com Groq...")
    groq_key = os.getenv("GROQ_API_KEY")
    
    if groq_key:
        try:
            llm_groq = ChatGroq(
                model="llama-3.3-70b-versatile",
                temperature=0.7,
                api_key=groq_key
            )
            
            message = HumanMessage(content="O que é Python? Responda em 1 frase.")
            response = llm_groq.invoke([message])
            
            print(f"✅ Groq: {response.content[:100]}...")
            print()
        except Exception as e:
            print(f"⚠️  Erro com Groq: {e}")
            print()
    else:
        print("⚠️  GROQ_API_KEY não encontrada, pulando Groq...")
        print()
    
    # EXEMPLO B: Usar Gemini (mesma sintaxe!)
    print("🔄 Testando com Gemini...")
    gemini_key = os.getenv("GEMINI_API_KEY")
    
    if gemini_key:
        try:
            # Veja: apenas mudamos a classe, resto igual!
            llm_gemini = ChatGoogleGenerativeAI(
                model="gemini-2.5-flash",
                temperature=0.7,
                google_api_key=gemini_key   
            )
            
            # Mesma mensagem
            message = HumanMessage(content="O que é Python? Responda em 1 frase.")
            
            # Mesmo método invoke()
            response = llm_gemini.invoke([message])
            
            print(f"✅ Gemini: {response.content[:100]}...")
            print()
            
            print("🎉 Veja: trocar LLM é muito fácil com LangChain!")
            print("   No código manual, precisaria reescrever tudo.")
            print()
            
        except Exception as e:
            print(f"⚠️  Erro com Gemini: {e}")
            print()
    else:
        print("⚠️  GEMINI_API_KEY não encontrada, pulando Gemini...")
        print()


# ============================================================================
# SEÇÃO 5: COMPARAÇÃO COM CÓDIGO MANUAL DA SEMANA 1
# ============================================================================

def comparacao_codigo_manual():
    """
    Compara código LangChain com código manual da Semana 1.
    
    Mostra diferenças práticas e vantagens do LangChain.
    """
    print("=" * 60)
    print("COMPARAÇÃO: Código Manual vs LangChain")
    print("=" * 60)
    print()
    
    print("📊 CÓDIGO MANUAL (Semana 1):")
    print("-" * 60)
    print("""
    # Código manual com Groq
    from groq import Groq
    
    client = Groq(api_key=api_key)
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": "Olá!"}],
        model="llama-3.3-70b-versatile"
    )
    resultado = response.choices[0].message.content
    """)
    print()
    
    print("📊 LANGCHAIN (Semana 2):")
    print("-" * 60)
    print("""
    # Código com LangChain
    from langchain_groq import ChatGroq
    from langchain_core.messages import HumanMessage
    
    llm = ChatGroq(model="llama-3.3-70b-versatile")
    message = HumanMessage(content="Olá!")
    resultado = llm.invoke([message]).content
    """)
    print()
    
    print("✅ VANTAGENS DO LANGCHAIN:")
    print("   1. Sintaxe mais intuitiva")
    print("   2. Trocar LLM = mudar 1 linha")
    print("   3. Padrão da indústria")
    print("   4. Funcionalidades avançadas (Chains, RAG, Agents)")
    print()
    
    print("⚠️  QUANDO USAR CÓDIGO MANUAL:")
    print("   1. Projeto muito simples (1-2 chamadas)")
    print("   2. Precisa controle total sobre requisições")
    print("   3. Não quer dependências extras")
    print()


# ============================================================================
# SEÇÃO 6: EXECUÇÃO PRINCIPAL
# ============================================================================

def main():
    """
    Função principal que executa todos os exemplos.
    
    Por que usamos __name__ == "__main__":
    - Permite executar script diretamente: python exemplo_langchain_basico.py
    - Permite importar funções em outros scripts sem executar main()
    """
    print("🚀 EXEMPLOS DE LANGCHAIN BÁSICO")
    print("=" * 60)
    print()
    print("Este script demonstra:")
    print("  1. Exemplo básico com Groq")
    print("  2. Uso de SystemMessage")
    print("  3. Trocar LLM facilmente")
    print("  4. Comparação com código manual")
    print()
    print("=" * 60)
    print()
    
    # Executar exemplos
    exemplo_basico_groq()
    
    print()
    input("Pressione Enter para continuar com próximo exemplo...")
    print()
    
    exemplo_com_system_message()
    
    print()
    input("Pressione Enter para continuar com próximo exemplo...")
    print()
    
    exemplo_trocar_llm()
    
    print()
    input("Pressione Enter para ver comparação...")
    print()
    
    comparacao_codigo_manual()
    
    print()
    print("=" * 60)
    print("✅ TODOS OS EXEMPLOS CONCLUÍDOS!")
    print("=" * 60)
    print()
    print("📚 Próximos passos:")
    print("   1. Complete os exercícios em exercicios_langchain.md")
    print("   2. Compare com código manual da Semana 1")
    print("   3. Crie seu próprio script usando LangChain")
    print("   4. Dia 2: Aprender Chains e sequências")
    print()


if __name__ == "__main__":
    main()

