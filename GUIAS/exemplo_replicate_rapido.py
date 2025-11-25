"""
Exemplo Rápido: Configurar e Usar Replicate API
================================================

Passos:
1. pip install replicate python-dotenv
2. Criar arquivo .env com: REPLICATE_API_TOKEN=r8_seu_token_aqui
3. Executar este script
"""

import os
from dotenv import load_dotenv
import replicate

# 1. Carregar variáveis de ambiente
load_dotenv()

# 2. Obter API token
api_token = os.getenv("REPLICATE_API_TOKEN")

if not api_token:
    raise ValueError(
        "❌ REPLICATE_API_TOKEN não encontrado!\n"
        "Crie um arquivo .env com: REPLICATE_API_TOKEN=r8_seu_token_aqui"
    )

print("✅ API Token encontrado!")

# 3. Criar cliente Replicate
client = replicate.Client(api_token=api_token)

# 4. Exemplo: Gerar imagem com Flux Schnell (mais rápido e barato)
print("\n🎨 Gerando imagem com Flux Schnell...")

try:
    output = client.run(
        "black-forest-labs/flux-schnell",
        input={
            "prompt": "Um gato astronauta no espaço, estilo realista, 4k",
            "num_outputs": 1,
            "aspect_ratio": "16:9",
        }
    )
    
    print(f"✅ Imagem gerada com sucesso!")
    print(f"🔗 URL: {output[0]}")
    
except Exception as e:
    print(f"❌ Erro ao gerar imagem: {e}")
    print("\n💡 Dicas:")
    print("   - Verifique se sua API token está correta")
    print("   - Verifique se tem créditos na conta Replicate")
    print("   - Consulte: https://replicate.com/account para ver seu saldo")

