
import os
from groq import Groq
from google import genai
from openai import OpenAI
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY não encontrada no .env")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY não encontrada no .env")

OPEN_API_KEY = os.getenv("OPEN_API_KEY")
if not OPEN_API_KEY:
    raise ValueError("OPEN_API_KEY não encontrada no .env")

llm_gemini = genai.Client(api_key=GEMINI_API_KEY)
llm_groq = Groq(api_key=GROQ_API_KEY)
llm_openai = OpenAI(api_key=OPEN_API_KEY)

# Função para criar uma resposta de LLM
def criar_llm_response(prompt: str, modelo: str) -> str:
    """
    Cria uma resposta de LLM.
    
    Args:
        prompt: str - O prompt para criar a resposta
        modelo: str - O modelo de LLM
    Returns:
        str - A resposta de LLM
    """
    if modelo == "groq":
        return llm_groq.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt[:1000],
                }
            ],
            temperature=0.3,
            max_tokens=100,
        )
    elif modelo == "gemini":
        config = types.GenerateContentConfig(
            temperature=0.3,
        )
        return llm_gemini.models.generate_content(
            model="gemini-2.5-flash",
            contents=[prompt],
            config=config
        )