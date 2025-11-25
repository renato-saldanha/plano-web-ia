# 🔧 Guia de Setup - APIs de IA

Este guia te ajudará a configurar as APIs de IA necessárias para o Dia 1.

---

## 🚀 1. Groq (PRIORIDADE - Gratuito e Ultra-Rápido)

### Passo 1: Criar Conta
1. Acesse: https://console.groq.com
2. Clique em **"Sign Up"** ou **"Get Started"**
3. Escolha uma opção:
   - **Google** (recomendado - mais rápido)
   - **GitHub**
   - **Email**

### Passo 2: Obter API Key
1. Após fazer login, você será redirecionado para o dashboard
2. Clique em **"API Keys"** no menu lateral
3. Clique em **"Create API Key"**
4. Dê um nome (ex: "dev-journey-2025")
5. Copie a chave (começa com `gsk_...`)
6. **⚠️ IMPORTANTE:** Salve em local seguro! Você só verá uma vez.

### Passo 3: Configurar no Projeto
1. Crie arquivo `.env` na raiz do projeto
2. Adicione:
   ```env
   GROQ_API_KEY=gsk_sua_chave_aqui
   ```
3. Instale biblioteca:
   ```bash
   pip install groq python-dotenv
   ```

### Modelos Disponíveis (Gratuitos)
- `llama-3.2-3b-instruct` - Rápido, ideal para testes
- `llama-3.1-70b-versatile` - Mais poderoso
- `mixtral-8x7b-32768` - Boa qualidade

**Limite:** Generoso, suficiente para desenvolvimento e testes!

---

## ✨ 2. Google Gemini (Gratuito)

### Passo 1: Criar Conta
1. Acesse: https://ai.google.dev
2. Clique em **"Get API Key"**
3. Faça login com sua conta Google
4. Aceite os termos

### Passo 2: Obter API Key
1. Clique em **"Create API Key"**
2. Escolha projeto (ou crie um novo)
3. Copie a chave (começa com `AIza...`)
4. Salve em local seguro

### Passo 3: Configurar no Projeto
1. Adicione ao `.env`:
   ```env
   GEMINI_API_KEY=AIza_sua_chave_aqui
   ```
2. Instale biblioteca:
   ```bash
   pip install google-generativeai python-dotenv
   ```

### Limites
- **60 requisições/minuto** (muito generoso!)
- Gratuito para desenvolvimento

---

## 🧠 3. Anthropic Claude (Opcional - $5 Grátis)

### Passo 1: Criar Conta
1. Acesse: https://console.anthropic.com
2. Clique em **"Sign Up"**
3. Escolha:
   - **Google**
   - **Email**

### Passo 2: Obter API Key
1. Após login, vá em **"API Keys"**
2. Clique em **"Create Key"**
3. Dê um nome (ex: "dev-journey")
4. Copie a chave (começa com `sk-ant-...`)
5. Salve em local seguro

### Passo 3: Configurar no Projeto
1. Adicione ao `.env`:
   ```env
   ANTHROPIC_API_KEY=sk-ant-sua_chave_aqui
   ```
2. Instale biblioteca:
   ```bash
   pip install anthropic python-dotenv
   ```

### Créditos Iniciais
- **$5 grátis** ao criar conta
- Suficiente para testes e desenvolvimento inicial

---

## 🔐 4. Configuração de Segurança

### Criar .env.example
Crie um arquivo `.env.example` (template para outros desenvolvedores):

```env
# .env.example
GROQ_API_KEY=your_groq_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

### Adicionar ao .gitignore
Certifique-se de que `.env` está no `.gitignore`:

```gitignore
# .gitignore
.env
.env.local
*.env
venv/
__pycache__/
*.pyc
```

**⚠️ NUNCA commite seu arquivo .env no GitHub!**

---

## ✅ Checklist de Verificação

- [ ] Conta Groq criada
- [ ] API Key Groq obtida e salva
- [ ] Conta Gemini criada
- [ ] API Key Gemini obtida e salva
- [ ] (Opcional) Conta Claude criada
- [ ] (Opcional) API Key Claude obtida e salva
- [ ] Arquivo `.env` criado com todas as keys
- [ ] Bibliotecas instaladas (`pip install groq anthropic google-generativeai python-dotenv`)
- [ ] `.env` adicionado ao `.gitignore`
- [ ] `.env.example` criado (template)

---

## 🧪 Teste Rápido

Execute o script `hello_ai_groq.py` para testar:

```bash
python hello_ai_groq.py
```

Se funcionar, você verá uma resposta do Llama 3.2! 🎉

---

## 📚 Recursos Adicionais

- **Groq Docs:** https://console.groq.com/docs
- **Gemini Docs:** https://ai.google.dev/docs
- **Claude Docs:** https://docs.anthropic.com
- **Troubleshooting:** Consulte documentação oficial se encontrar problemas

---

## 💡 Dicas

1. **Priorize Groq** - É gratuito e ultra-rápido, perfeito para desenvolvimento
2. **Use Gemini** - Para tarefas que precisam de mais criatividade
3. **Claude** - Para análise de código e textos longos (quando necessário)
4. **Economize** - Use modelos menores para testes, maiores para produção

---

**Boa sorte com o setup!** 🚀

