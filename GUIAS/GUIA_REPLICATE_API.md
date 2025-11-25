# 🎨 Guia Completo: Configurar Replicate API

Replicate é uma plataforma que permite executar modelos de IA (geração de imagens, vídeos, áudio) via API. É perfeito para usar modelos como **Flux**, **Stable Diffusion**, **DALL-E** e outros.

---

## 📋 Passo 1: Criar Conta e Obter API Key

### 1.1 Criar Conta
1. Acesse: https://replicate.com
2. Clique em **"Sign Up"** (canto superior direito)
3. Escolha uma opção:
   - **GitHub** (recomendado - mais rápido)
   - **Google**
   - **Email** (criar conta manualmente)

### 1.2 Obter API Key
1. Após fazer login, clique no seu **avatar** (canto superior direito)
2. Selecione **"Account"** ou **"API Tokens"**
3. Você verá sua **API Token** (começa com `r8_...`)
4. Clique em **"Copy"** para copiar

**⚠️ IMPORTANTE:** Guarde esta chave em local seguro! Ela dá acesso à sua conta.

---

## 🔐 Passo 2: Configurar Variáveis de Ambiente

### 2.1 Python (FastAPI/Flask)

#### Criar arquivo `.env`
Na raiz do seu projeto Python, crie um arquivo `.env`:

```env
REPLICATE_API_TOKEN=r8_seu_token_aqui
```

#### Instalar biblioteca python-dotenv
```bash
pip install python-dotenv replicate
```

#### Carregar no código Python
```python
import os
from dotenv import load_dotenv
import replicate

# Carregar variáveis do .env
load_dotenv()

# Obter API token
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

# Configurar Replicate
replicate.Client(api_token=REPLICATE_API_TOKEN)

# OU configurar via variável de ambiente diretamente
os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN
```

#### Exemplo Completo (Python)
```python
import os
from dotenv import load_dotenv
import replicate

# Carregar .env
load_dotenv()

# Obter token
api_token = os.getenv("REPLICATE_API_TOKEN")

if not api_token:
    raise ValueError("REPLICATE_API_TOKEN não encontrado no .env")

# Criar cliente Replicate
client = replicate.Client(api_token=api_token)

# Exemplo: Gerar imagem com Flux
def gerar_imagem(prompt: str):
    output = client.run(
        "black-forest-labs/flux-pro",
        input={
            "prompt": prompt,
            "num_outputs": 1,
            "aspect_ratio": "16:9"
        }
    )
    return output

# Usar
imagem_url = gerar_imagem("Um gato astronauta no espaço")
print(f"Imagem gerada: {imagem_url}")
```

---

### 2.2 Node.js/TypeScript (NextJS/Express)

#### Criar arquivo `.env.local` (NextJS) ou `.env` (Node.js)
Na raiz do projeto:

```env
REPLICATE_API_TOKEN=r8_seu_token_aqui
```

#### Instalar biblioteca
```bash
npm install replicate
# ou
bun add replicate
```

#### Carregar no código TypeScript/JavaScript
```typescript
import Replicate from "replicate";

// Obter token do ambiente
const apiToken = process.env.REPLICATE_API_TOKEN;

if (!apiToken) {
  throw new Error("REPLICATE_API_TOKEN não encontrado no .env");
}

// Criar cliente
const replicate = new Replicate({
  auth: apiToken,
});

// Exemplo: Gerar imagem
async function gerarImagem(prompt: string) {
  const output = await replicate.run(
    "black-forest-labs/flux-pro",
    {
      input: {
        prompt: prompt,
        num_outputs: 1,
        aspect_ratio: "16:9",
      },
    }
  );
  return output;
}

// Usar
const imagemUrl = await gerarImagem("Um gato astronauta no espaço");
console.log(`Imagem gerada: ${imagemUrl}`);
```

#### NextJS - API Route (exemplo)
```typescript
// app/api/generate-image/route.ts
import { NextRequest, NextResponse } from "next/server";
import Replicate from "replicate";

const replicate = new Replicate({
  auth: process.env.REPLICATE_API_TOKEN,
});

export async function POST(request: NextRequest) {
  try {
    const { prompt } = await request.json();

    const output = await replicate.run(
      "black-forest-labs/flux-pro",
      {
        input: {
          prompt: prompt,
          num_outputs: 1,
        },
      }
    );

    return NextResponse.json({ imageUrl: output });
  } catch (error) {
    return NextResponse.json(
      { error: "Erro ao gerar imagem" },
      { status: 500 }
    );
  }
}
```

---

## 🛡️ Passo 3: Segurança (IMPORTANTE!)

### 3.1 Adicionar `.env` ao `.gitignore`
**NUNCA** commite seu arquivo `.env` no GitHub!

```gitignore
# .gitignore
.env
.env.local
.env*.local
```

### 3.2 Criar `.env.example` (template)
Crie um arquivo `.env.example` para outros desenvolvedores:

```env
# .env.example
REPLICATE_API_TOKEN=seu_token_aqui
```

### 3.3 Variáveis de Ambiente no Deploy

#### Vercel (NextJS)
1. Acesse seu projeto no Vercel
2. Vá em **Settings** → **Environment Variables**
3. Adicione:
   - **Name:** `REPLICATE_API_TOKEN`
   - **Value:** `r8_seu_token_aqui`
4. Clique em **Save**

#### Railway/Render (Backend)
1. Acesse seu projeto
2. Vá em **Variables** ou **Environment**
3. Adicione a variável `REPLICATE_API_TOKEN`
4. Valor: `r8_seu_token_aqui`

---

## 🎨 Passo 4: Exemplos Práticos

### 4.1 Gerar Imagem com Flux (Python)
```python
import replicate
import os
from dotenv import load_dotenv

load_dotenv()

client = replicate.Client(api_token=os.getenv("REPLICATE_API_TOKEN"))

# Gerar imagem
output = client.run(
    "black-forest-labs/flux-pro",
    input={
        "prompt": "Um gato astronauta flutuando no espaço, estilo realista, 4k",
        "num_outputs": 1,
        "aspect_ratio": "16:9",
        "output_format": "webp",
        "output_quality": 90
    }
)

print(f"Imagem gerada: {output[0]}")
```

### 4.2 Gerar Imagem com Stable Diffusion (TypeScript)
```typescript
import Replicate from "replicate";

const replicate = new Replicate({
  auth: process.env.REPLICATE_API_TOKEN!,
});

async function gerarImagemStableDiffusion(prompt: string) {
  const output = await replicate.run(
    "stability-ai/stable-diffusion:db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",
    {
      input: {
        prompt: prompt,
        image_dimensions: "512x512",
        num_outputs: 1,
      },
    }
  );
  
  return output;
}
```

### 4.3 Gerar Vídeo (Python)
```python
import replicate
import os
from dotenv import load_dotenv

load_dotenv()

client = replicate.Client(api_token=os.getenv("REPLICATE_API_TOKEN"))

# Gerar vídeo com AnimateDiff
output = client.run(
    "lucataco/animate-diff",
    input={
        "prompt": "Um gato dançando, estilo cartoon",
        "num_frames": 16,
        "guidance_scale": 7.5
    }
)

print(f"Vídeo gerado: {output}")
```

---

## 📊 Passo 5: Modelos Populares no Replicate

### Geração de Imagens
- **Flux Pro:** `black-forest-labs/flux-pro` (melhor qualidade 2025)
- **Flux Schnell:** `black-forest-labs/flux-schnell` (mais rápido)
- **Stable Diffusion XL:** `stability-ai/sdxl`
- **DALL-E 3:** `openai/dall-e-3`

### Geração de Vídeo
- **AnimateDiff:** `lucataco/animate-diff`
- **Zeroscope:** `anotherjesse/zeroscope-v2-xl`

### Processamento de Imagem
- **Upscale:** `nightmareai/real-esrgan` (melhorar qualidade)
- **Remove Background:** `cjwbw/rembg` (remover fundo)

---

## 💰 Passo 6: Custos e Limites

### Plano Gratuito
- **$0.10 de créditos grátis** ao criar conta
- Permite testar modelos básicos

### Preços (2025)
- **Flux Pro:** ~$0.04 por imagem
- **Stable Diffusion:** ~$0.002 por imagem
- **Vídeos:** ~$0.10-0.50 por vídeo (depende do modelo)

### Dicas para Economizar
1. Use **Flux Schnell** para testes (mais barato que Flux Pro)
2. Use **Stable Diffusion** para prototipagem (muito barato)
3. Configure **webhooks** para processar assincronamente
4. Cache resultados quando possível

---

## 🐛 Troubleshooting

### Erro: "API token not found"
**Solução:** Verifique se:
- Arquivo `.env` está na raiz do projeto
- Variável está escrita corretamente: `REPLICATE_API_TOKEN`
- Você carregou o `.env` com `load_dotenv()` (Python) ou configurou no ambiente (Node.js)

### Erro: "Invalid API token"
**Solução:**
- Verifique se copiou o token completo (começa com `r8_`)
- Não há espaços antes/depois do token
- Token não expirou (geralmente não expiram, mas verifique na conta)

### Erro: "Rate limit exceeded"
**Solução:**
- Você atingiu o limite de requisições
- Aguarde alguns minutos ou faça upgrade do plano

### Erro: "Model not found"
**Solução:**
- Verifique se o nome do modelo está correto
- Consulte: https://replicate.com/explore para ver modelos disponíveis

---

## 📚 Recursos Adicionais

- **Documentação Oficial:** https://replicate.com/docs
- **Explorar Modelos:** https://replicate.com/explore
- **Python SDK:** https://github.com/replicate/replicate-python
- **JavaScript SDK:** https://github.com/replicate/replicate-javascript
- **Exemplos:** https://replicate.com/docs/get-started/python

---

## ✅ Checklist de Configuração

- [ ] Criei conta no Replicate
- [ ] Copiei minha API token (`r8_...`)
- [ ] Criei arquivo `.env` com `REPLICATE_API_TOKEN`
- [ ] Adicionei `.env` ao `.gitignore`
- [ ] Instalei biblioteca (`pip install replicate` ou `npm install replicate`)
- [ ] Testei gerar uma imagem simples
- [ ] Configurei variável de ambiente no deploy (Vercel/Railway)

---

## 🚀 Próximos Passos

1. **Teste básico:** Gere uma imagem simples com Flux
2. **Integre no projeto:** Adicione geração de imagens ao seu app
3. **Otimize custos:** Use modelos mais baratos para testes
4. **Adicione cache:** Evite gerar a mesma imagem duas vezes

**Boa sorte com Replicate!** 🎨

