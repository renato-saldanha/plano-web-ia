# ✅ Checklist - Dia 6 (Sábado, 29 Nov 2024)

## 🎯 Objetivo do Dia
Criar CLI integrado unificando os 3 scripts dos dias anteriores em uma interface profissional e intuitiva.

---

## 📋 FASE 1: PREPARAÇÃO E APRENDIZADO (45-60min)

### Leitura e Compreensão
- [ X] Ler `GUIA_CLI.md` completo para entender conceitos de CLI
- [ X] Ler `exemplo_cli_simples.py` para ver exemplo completo comentado
- [ X] Revisar scripts dos dias anteriores:
  - [X ] `Dia2/gerador_conteudo_blog.py` - identificar função `gerar_conteudo_tema()`
  - [X ] `Dia3/analisador_sentimentos.py` - identificar funções de análise
  - [X ] `Dia4/resumidor_pdf.py` - identificar função `resumir_pdf()`
- [ X] Anotar nomes exatos das funções a serem importadas
- [ X] Anotar parâmetros necessários de cada função

**Como fazer:**
1. Abra `GUIA_CLI.md` e leia seção por seção
2. Execute `exemplo_cli_simples.py` para ver funcionamento: `python exemplo_cli_simples.py --help`
3. Abra cada script dos dias anteriores e identifique as funções principais
4. Anote em um papel ou arquivo: função, parâmetros, retorno

**Por que:**
Entender os conceitos antes de implementar evita erros e acelera o desenvolvimento.

**Tempo estimado:** 45-60 minutos  
**Quando:** Início do dia

---

## 💻 FASE 2: ESTRUTURA BASE COM TEMPLATE (60-90min)

### Usar Template como Base
- [ X] Copiar `template_cli.py` para `cli_automatizacoes.py`
- [ X] Ler todos os TODOs no template
- [ X] Entender estrutura geral antes de preencher

### Preencher TODOs - Parte 1: Configuração
- [ X] **TODO: Importar logging e configurar**
  - Adicionar: `import logging`
  - Adicionar: `logging.basicConfig(...)` (ver exemplo_cli_simples.py linha 20-24)
  - Testar: Adicionar `logging.info("Teste")` e executar script

- [ X] **TODO: Importar funções dos scripts anteriores**
  - Adicionar imports baseado nas anotações da Fase 1
  - Testar imports: executar script e verificar se não há erros

**Como fazer:**
1. Abra `template_cli.py` e `exemplo_cli_simples.py` lado a lado
2. Compare estrutura e copie configurações similares
3. Teste após cada mudança para garantir que funciona

**Por que:**
Configuração correta desde o início evita problemas depois.

**Tempo estimado:** 20-30 minutos  
**Quando:** Após Fase 1

---

### Preencher TODOs - Parte 2: Parser e Subcomandos
- [ X] **TODO: Criar parser principal**
  - Consultar `GUIA_CLI.md` seção "Passo 2: Adicionar Subcomandos"
  - Consultar `exemplo_cli_simples.py` função `criar_parser()` (linha 150+)
  - Implementar parser com descrição adequada

- [ X] **TODO: Criar subparsers**
  - Criar subparser para `blog` com argumento `--tema`
  - Criar subparser para `sentimentos` com argumento `--arquivo`
  - Criar subparser para `resumir` com `--pdf` e `--llm` (choices=['groq', 'gemini'])

- [ X] **Testar parser:**
  - Executar: `python cli_automatizacoes.py --help`
  - Verificar se mostra ajuda correta
  - Executar: `python cli_automatizacoes.py blog --help`
  - Verificar se mostra ajuda do subcomando

**Como fazer:**
1. Siga exemplo em `exemplo_cli_simples.py` linha 150-200
2. Adapte para seus comandos específicos
3. Teste cada subcomando após criar

**Por que:**
Parser correto é base para todo o CLI funcionar.

**Tempo estimado:** 30-40 minutos  
**Quando:** Após Parte 1

---

### Preencher TODOs - Parte 3: Menu Interativo
- [ X] **TODO: Criar função mostrar_menu()**
  - Consultar `exemplo_cli_simples.py` função `mostrar_menu()` (linha 80+)
  - Criar menu visualmente atraente com opções numeradas
  - Retornar escolha do usuário

- [ X] **TODO: Criar função processar_menu()**
  - Consultar `exemplo_cli_simples.py` função `processar_menu()` (linha 95+)
  - Criar loop while True
  - Processar cada escolha (1, 2, 3, 4)
  - Adicionar opção de sair

- [ X] **Testar menu:**
  - Executar: `python cli_automatizacoes.py` (sem argumentos)
  - Verificar se menu aparece
  - Testar cada opção

**Como fazer:**
1. Use exemplo como base
2. Adapte opções para seus comandos
3. Teste interativamente

**Por que:**
Menu interativo melhora experiência do usuário.

**Tempo estimado:** 20-30 minutos  
**Quando:** Após Parte 2

---

## 🔗 FASE 3: INTEGRAÇÃO DOS SCRIPTS (90-120min)

### Integrar Gerador de Conteúdo (Dia 2) - 30min
- [ X] **TODO: Implementar função comando_blog()**
  - Validar se tema não está vazio
  - Chamar função do Dia 2: `gerar_conteudo_tema(tema)`
  - Tratar erros com try/except
  - Mostrar resultado ou mensagem de sucesso

**Como fazer:**
1. Abra `Dia2/gerador_conteudo_blog.py` e veja como `gerar_conteudo_tema()` funciona
2. No template, preencha função `comando_blog()` seguindo estrutura:
   ```python
   def comando_blog(tema: str) -> None:
       if not tema or tema.strip() == "":
           logging.error("Tema não pode estar vazio!")
           sys.exit(1)
       try:
           resultado = gerar_conteudo_tema(tema)
           logging.info("✅ Conteúdo gerado com sucesso!")
       except Exception as e:
           logging.error(f"❌ Erro: {e}")
           sys.exit(1)
   ```
3. Teste: `python cli_automatizacoes.py blog --tema "Python"`

**Por que:**
Validação e tratamento de erros garantem CLI robusto.

**Tempo estimado:** 30 minutos

---

### Integrar Analisador de Sentimentos (Dia 3) - 30min
- [ X] **TODO: Implementar função comando_sentimentos()**
  - Validar se arquivo existe usando `os.path.exists()`
  - Ler arquivo de reviews
  - Chamar funções do Dia 3 para analisar
  - Processar e mostrar resultados

**Como fazer:**
1. Veja estrutura do Dia 3 para entender como funciona análise
2. Implemente validação de arquivo primeiro
3. Depois adicione chamadas às funções de análise
4. Teste: `python cli_automatizacoes.py sentimentos --arquivo ../Dia3/reviews/reviews.txt`

**Por que:**
Validação de arquivo evita erros em runtime.

**Tempo estimado:** 30 minutos

---

### Integrar Resumidor de PDFs (Dia 4) - 30min
- [ X] **TODO: Implementar função comando_resumir()**
  - Validar se PDF existe
  - Validar se LLM é válido ('groq' ou 'gemini')
  - Chamar função do Dia 4: `resumir_pdf(pdf, llm)`
  - Processar resultado

**Como fazer:**
1. Veja como `resumir_pdf()` funciona no Dia 4
2. Implemente validações antes de chamar função
3. Teste: `python cli_automatizacoes.py resumir --pdf ../Dia4/pdfs/arquivo.pdf --llm groq`

**Por que:**
Validação de LLM garante que apenas opções válidas sejam usadas.

**Tempo estimado:** 30 minutos

---

### Integrar Menu com Comandos - 30min
- [ X] **TODO: Atualizar processar_menu()**
  - Opção 1 deve chamar `comando_blog()` com input do usuário
  - Opção 2 deve chamar `comando_sentimentos()` com input do usuário
  - Opção 3 deve chamar `comando_resumir()` com inputs do usuário
  - Testar menu completo

**Como fazer:**
1. No `processar_menu()`, substitua `pass` por chamadas reais
2. Use `input()` para receber parâmetros do usuário
3. Valide entradas antes de chamar funções
4. Teste menu interativo completamente

**Por que:**
Menu deve funcionar igual aos comandos de linha.

**Tempo estimado:** 30 minutos  
**Quando:** Após integrar cada comando

---

## 🎨 FASE 4: MELHORIAS E POLIMENTO (60-90min)

### Tratamento de Erros Unificado
- [ X] Criar função `tratar_erro(erro: Exception, contexto: str)`
- [ X] Adicionar mensagens de erro claras e úteis
- [ X] Adicionar sugestões de solução nos erros
- [ X] Testar cenários de erro (arquivo não encontrado, API key inválida, etc.)

### Melhorias de UX
- [ X] Adicionar mensagens de progresso durante execução
- [ X] Adicionar cores no terminal (opcional, usando `colorama`)
- [ X] Adicionar formatação de saída melhorada
- [ X] Adicionar estatísticas de execução (tempo, tokens, etc.)

### Documentação Inline
- [ X] Adicionar docstrings em todas as funções
- [ X] Melhorar help text de cada comando
- [ X] Adicionar exemplos de uso no help
- [ X] Criar README com exemplos de uso

**Tempo estimado:** 60-90 minutos  
**Quando:** Após integração

---

## 🧪 FASE 5: TESTES E VALIDAÇÃO (45-60min)

### Testes Funcionais
- [ X] Testar comando `blog` com diferentes temas
- [ X] Testar comando `sentimentos` com arquivo válido
- [ X] Testar comando `resumir` com diferentes PDFs e LLMs
- [ X] Testar menu interativo
- [ X] Testar tratamento de erros (arquivo não encontrado, etc.)

### Testes de Integração
- [ X] Testar fluxo completo: blog → sentimentos → resumir
- [ X] Verificar se todos os arquivos são salvos corretamente
- [ X] Verificar se logs são gerados corretamente
- [ X] Verificar se mensagens de erro são claras

### Validação Final
- [ X] Executar `python cli_automatizacoes.py --help` e verificar saída
- [ X] Executar cada comando individualmente
- [ X] Verificar se código segue PEP 8 (`autopep8`)
- [ X] Verificar se não há imports não utilizados

**Tempo estimado:** 45-60 minutos  
**Quando:** Após melhorias

---

## 📝 FASE 6: FINALIZAÇÃO (30min)

### Git e Organização
- [ X] Adicionar arquivos: `git add .`
- [ X] Commit: `git commit -m "Dia 6: CLI integrado com 3 automações"`
- [ X] Push: `git push origin main`

### Journal e Planejamento
- [ ] Abrir arquivo `journal.md`
- [ ] Preencher journal com o que fez hoje
- [ ] Anotar dificuldades encontradas
- [ ] Anotar aprendizados sobre CLI e integração
- [ ] Planejar 3 tarefas para amanhã (Domingo - Deploy + Review):

**Seu planejamento:**
1. Criar README épico com documentação completa do projeto
2. Fazer deploy no GitHub e organizar repositório
3. Fazer review completo da semana e preparar para Semana 2

*(Veja mais exemplos em: `EXEMPLOS_TAREFAS.md`)*

### Revisão
- [ ] Revisar código escrito hoje
- [ ] Verificar se tudo está funcionando
- [ ] Confirmar commit no GitHub
- [ ] Preparar para Dia 7 (Deploy + Review)

**Tempo estimado:** 30 minutos  
**Quando:** Final do dia

---

## 🎉 CONCLUSÃO

**Total estimado:** 4-6 horas (meta realista: 3-5h)

### ✅ Critérios de Sucesso:
- [ ] CLI funcional com 3 comandos principais
- [ ] Menu interativo funcionando
- [ ] Todos os scripts integrados corretamente
- [ ] Tratamento de erros unificado
- [ ] Help text completo e claro
- [ ] Testes básicos realizados
- [ ] Código organizado e documentado
- [ ] Commit feito no GitHub
- [ ] Journal preenchido

### 🎯 Streak: 6/56 dias

**Parabéns por completar o Dia 6!** 🚀

---

## 📚 Recursos Úteis

### Guias de Aprendizado (Neste Diretório)
- `GUIA_CLI.md` - Conceitos teóricos e passo-a-passo completo
- `exemplo_cli_simples.py` - Exemplo completo comentado linha por linha
- `template_cli.py` - Template com TODOs para preencher
- `exercicios_cli.md` - Exercícios progressivos para praticar

### Scripts dos Dias Anteriores
- Dia 2: `../Dia2/gerador_conteudo_blog.py`
- Dia 3: `../Dia3/analisador_sentimentos.py`
- Dia 4: `../Dia4/resumidor_pdf.py`

### Documentação Externa
- Python argparse: https://docs.python.org/3/library/argparse.html
- CLI Design Best Practices: https://clig.dev/
- Python click (alternativa): https://click.palletsprojects.com/

---

## 💡 Dicas Importantes

1. **Reutilização:** Importe funções dos scripts anteriores, não duplique código
2. **Tratamento de Erros:** Mensagens claras ajudam muito o usuário
3. **Help Text:** Documentação inline é essencial para CLI profissional
4. **Testes:** Teste cada comando após integrar
5. **Incremental:** Crie estrutura básica primeiro, depois integre cada script

---

**Última atualização:** 29 Nov 2025


