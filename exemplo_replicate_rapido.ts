/**
 * Exemplo Rápido: Configurar e Usar Replicate API (TypeScript/NextJS)
 * ====================================================================
 * 
 * Passos:
 * 1. npm install replicate (ou bun add replicate)
 * 2. Criar arquivo .env.local com: REPLICATE_API_TOKEN=r8_seu_token_aqui
 * 3. Usar este código
 */

import Replicate from "replicate";

// 1. Verificar se API token existe
const apiToken = process.env.REPLICATE_API_TOKEN;

if (!apiToken) {
  throw new Error(
    "❌ REPLICATE_API_TOKEN não encontrado!\n" +
    "Crie um arquivo .env.local com: REPLICATE_API_TOKEN=r8_seu_token_aqui"
  );
}

console.log("✅ API Token encontrado!");

// 2. Criar cliente Replicate
const replicate = new Replicate({
  auth: apiToken,
});

// 3. Função para gerar imagem
async function gerarImagem(prompt: string) {
  try {
    console.log("\n🎨 Gerando imagem com Flux Schnell...");
    
    const output = await replicate.run(
      "black-forest-labs/flux-schnell",
      {
        input: {
          prompt: prompt,
          num_outputs: 1,
          aspect_ratio: "16:9",
        },
      }
    );
    
    console.log("✅ Imagem gerada com sucesso!");
    console.log(`🔗 URL: ${output}`);
    
    return output;
  } catch (error) {
    console.error("❌ Erro ao gerar imagem:", error);
    console.log("\n💡 Dicas:");
    console.log("   - Verifique se sua API token está correta");
    console.log("   - Verifique se tem créditos na conta Replicate");
    console.log("   - Consulte: https://replicate.com/account para ver seu saldo");
    throw error;
  }
}

// 4. Exemplo de uso
async function exemplo() {
  const imagemUrl = await gerarImagem(
    "Um gato astronauta no espaço, estilo realista, 4k"
  );
  return imagemUrl;
}

// Para usar em NextJS API Route:
// app/api/generate-image/route.ts
export async function POST(request: Request) {
  try {
    const { prompt } = await request.json();
    
    const output = await replicate.run(
      "black-forest-labs/flux-schnell",
      {
        input: {
          prompt: prompt,
          num_outputs: 1,
        },
      }
    );
    
    return Response.json({ imageUrl: output });
  } catch (error) {
    return Response.json(
      { error: "Erro ao gerar imagem" },
      { status: 500 }
    );
  }
}

// Exportar para uso
export { gerarImagem, replicate };

