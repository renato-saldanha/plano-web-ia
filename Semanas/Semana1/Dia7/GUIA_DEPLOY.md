# 🚀 Guia Completo: Deploy no GitHub

Este guia fornece passo-a-passo detalhado para fazer deploy do projeto no GitHub de forma profissional.

---

## 📋 O que é Deploy e Por Que Fazer?

### O que é Deploy?
Deploy (ou implantação) é o processo de colocar seu código em um repositório remoto (como GitHub) para:
- Compartilhar seu trabalho
- Manter backup do código
- Colaborar com outros desenvolvedores
- Mostrar seu portfólio
- Versionar mudanças

### Por Que Fazer Deploy?
1. **Backup:** Seu código fica seguro na nuvem
2. **Portfólio:** Mostra seu trabalho para recrutadores/empresas
3. **Colaboração:** Facilita trabalho em equipe
4. **Versionamento:** Histórico completo de mudanças
5. **Aprendizado:** Prática com ferramentas profissionais

---

## 🎯 Pré-requisitos

Antes de começar, certifique-se de ter:

- [ ] Git instalado localmente
- [ ] Conta GitHub criada
- [ ] Acesso à internet
- [ ] Projeto local funcionando

### Verificar Git Instalado

```bash
git --version
```

Se não estiver instalado, baixe em: https://git-scm.com/downloads

### Verificar Conta GitHub

Acesse https://github.com e faça login (ou crie conta se necessário).

---

## 📝 PASSO 1: Preparar Repositório Local

### 1.1 Inicializar Git (se necessário)

Navegue até a raiz do projeto:

```bash
cd "d:\plano web+ia"
```

Verifique se Git já está inicializado:

```bash
git status
```

Se aparecer erro "not a git repository", inicialize:

```bash
git init
```

### 1.2 Configurar Git (se necessário)

Configure seu nome e email (substitua pelos seus dados):

```bash
git config user.name "Seu Nome"
git config user.email "seu@email.com"
```

Verifique configuração:

```bash
git config user.name
git config user.email
```

### 1.3 Criar .gitignore

Crie arquivo `.gitignore` na raiz do projeto para excluir arquivos desnecessários:

```bash
# Criar arquivo .gitignore
```

Conteúdo do `.gitignore`:

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/
*.egg-info/
dist/
build/

# Environment variables
.env
.env.local
.env.*.local

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db
desktop.ini

# Logs
*.log
logs/

# Temporary files
*.tmp
*.temp
*.bak

# PDFs (opcional - remover se quiser versionar)
# *.pdf

# Resultados gerados (opcional)
# resultado_blog/
# resultado_comparacao/
# resumos/
```

**Por que:** `.gitignore` evita commitar arquivos desnecessários como `__pycache__`, `.env` (com chaves secretas), e arquivos temporários.

---

## 📝 PASSO 2: Criar Repositório no GitHub

### 2.1 Criar Repositório Novo

1. Acesse https://github.com e faça login
2. Clique no botão **"+"** no canto superior direito
3. Selecione **"New repository"**
4. Preencha:
   - **Repository name:** `plano-web-ia` (ou nome de sua escolha)
   - **Description:** "Plano de desenvolvimento de 2 meses em Web + IA Generativa"
   - **Visibility:** Public (ou Private se preferir)
   - **NÃO marque** "Initialize with README" (já temos README)
   - **NÃO marque** "Add .gitignore" (já criamos)
5. Clique em **"Create repository"**

### 2.2 Copiar URL do Repositório

Após criar, GitHub mostrará instruções. Copie a URL:
- **HTTPS:** `https://github.com/seu-usuario/plano-web-ia.git`
- **SSH:** `git@github.com:seu-usuario/plano-web-ia.git`

**Recomendação:** Use HTTPS se não configurou SSH.

---

## 📝 PASSO 3: Conectar Repositório Local ao GitHub

### 3.1 Adicionar Remote

No terminal, na raiz do projeto:

```bash
git remote add origin https://github.com/seu-usuario/plano-web-ia.git
```

**Substitua** `seu-usuario` e `plano-web-ia` pelos seus valores.

### 3.2 Verificar Remote

```bash
git remote -v
```

Deve mostrar:
```
origin  https://github.com/seu-usuario/plano-web-ia.git (fetch)
origin  https://github.com/seu-usuario/plano-web-ia.git (push)
```

---

## 📝 PASSO 4: Fazer Primeiro Commit

### 4.1 Adicionar Arquivos ao Staging

```bash
git add .
```

Isso adiciona todos os arquivos (exceto os no `.gitignore`).

### 4.2 Verificar o Que Será Commitado

```bash
git status
```

Revise a lista. Se houver arquivos que não devem ser commitados:

```bash
git reset HEAD caminho/do/arquivo
```

### 4.3 Fazer Commit

```bash
git commit -m "docs: adiciona documentação completa e estrutura do projeto"
```

**Boas práticas de mensagens de commit:**
- Use prefixos: `docs:`, `feat:`, `fix:`, `chore:`
- Seja descritivo mas conciso
- Use presente: "adiciona" não "adicionou"

### 4.4 Verificar Histórico

```bash
git log --oneline
```

Deve mostrar seu commit.

---

## 📝 PASSO 5: Push para GitHub

### 5.1 Fazer Push

```bash
git push -u origin main
```

**Nota:** Se sua branch principal for `master`, use:
```bash
git push -u origin master
```

**O que faz:** `-u` configura upstream, então futuros `git push` não precisam especificar `origin main`.

### 5.2 Autenticação

Se solicitado:
- **Username:** Seu usuário GitHub
- **Password:** Use Personal Access Token (não senha da conta)

**Como criar Personal Access Token:**
1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token (classic)
3. Selecione escopos: `repo` (acesso completo a repositórios)
4. Generate token
5. **Copie o token** (não será mostrado novamente!)
6. Use o token como senha

### 5.3 Verificar no GitHub

Acesse seu repositório no GitHub e verifique se todos os arquivos aparecem.

---

## 📝 PASSO 6: Commits Adicionais (Opcional)

Se quiser fazer commits separados por tipo:

```bash
# Adicionar apenas README
git add README.md
git commit -m "docs: adiciona README principal"

# Adicionar guias
git add GUIAS/
git commit -m "docs: adiciona guias de aprendizado"

# Adicionar scripts
git add Semanas/
git commit -m "feat: adiciona scripts da Semana 1"

# Push todos os commits
git push
```

---

## 🔧 Troubleshooting

### Erro: "remote origin already exists"

**Solução:**
```bash
git remote remove origin
git remote add origin https://github.com/seu-usuario/plano-web-ia.git
```

### Erro: "failed to push some refs"

**Causa:** Repositório remoto tem commits que local não tem.

**Solução:**
```bash
git pull origin main --allow-unrelated-histories
# Resolver conflitos se houver
git push origin main
```

### Erro: "authentication failed"

**Solução:**
- Use Personal Access Token em vez de senha
- Verifique se token tem escopo `repo`
- Verifique se URL está correta

### Arquivos não aparecem no GitHub

**Verificar:**
1. Arquivo está no `.gitignore`?
2. Arquivo foi adicionado ao staging (`git add`)?
3. Commit foi feito?
4. Push foi feito?

---

## ✅ Checklist de Deploy

- [ X] Git inicializado localmente
- [ X] `.gitignore` criado e configurado
- [ X] Repositório GitHub criado
- [ X] Remote adicionado
- [ X] Arquivos adicionados ao staging
- [ X] Primeiro commit feito
- [ X] Push realizado com sucesso
- [ X] Arquivos aparecem no GitHub
- [ X] README aparece corretamente no GitHub

---

## 🎯 Próximos Passos

Após deploy bem-sucedido:

1. **Adicionar descrição no GitHub:** Edite repositório e adicione descrição
2. **Adicionar tópicos:** Adicione tags como `python`, `ai`, `automation`
3. **Criar releases:** Se quiser versionar (ex: v1.0.0)
4. **Adicionar badges:** No README, adicione badges de status

---

## 💡 Dicas Finais

1. **Commits frequentes:** Faça commits pequenos e frequentes
2. **Mensagens descritivas:** Facilita entender histórico
3. **Não commitar secrets:** Nunca commite `.env` com chaves
4. **README sempre atualizado:** Mantenha README sincronizado com código
5. **Branch protection:** Configure proteção de branch `main` no GitHub

---

**Última atualização:** 30 Nov 2025

**Status:** ✅ Completo

