# ✅ Checklist - Dia 6 (Sábado, 29 Nov 2024)

## 🎯 Objetivo do Dia
Criar CLI integrado unificando os 3 scripts dos dias anteriores em uma interface profissional e intuitiva.

---

## 📋 FASE 1: PLANEJAMENTO E ESTRUTURA (30-45min)

### Análise dos Scripts Existentes
- [ ] Ler `Dia2/gerador_conteudo_blog.py` e entender estrutura
- [ ] Ler `Dia3/analisardor_sentimentos.py` e entender estrutura
- [ ] Ler `Dia4/resumidor_pdf.py` e entender estrutura
- [ ] Identificar funções principais de cada script
- [ ] Identificar dependências e imports necessários

### Planejamento do CLI
- [ ] Decidir biblioteca CLI (`argparse` ou `click`)
- [ ] Definir estrutura de comandos:
  - [ ] `blog` - Gerar conteúdo para blog
  - [ ] `sentimentos` - Analisar sentimentos
  - [ ] `resumir` - Resumir PDFs
- [ ] Planejar menu interativo opcional
- [ ] Definir tratamento de erros unificado

**Tempo estimado:** 30-45 minutos  
**Quando:** Início do dia

---

## 💻 FASE 2: CRIAÇÃO DA ESTRUTURA BASE (60-90min)

### Setup Inicial
- [ ] Criar arquivo `cli_automatizacoes.py`
- [ ] Configurar imports necessários
- [ ] Configurar logging unificado
- [ ] Configurar carregamento de `.env`

### Estrutura CLI com argparse
- [ ] Criar parser principal com descrição
- [ ] Criar subparsers para cada comando
- [ ] Adicionar argumentos para cada comando:
  - [ ] `blog --tema "Python"`
  - [ ] `sentimentos --arquivo reviews.txt`
  - [ ] `resumir --pdf arquivo.pdf --llm groq`
- [ ] Adicionar flags opcionais (`--help`, `--verbose`, etc.)

### Menu Interativo
- [ ] Criar função `mostrar_menu()`
- [ ] Criar função `processar_menu()`
- [ ] Integrar menu com comandos CLI
- [ ] Adicionar opção de sair

**Tempo estimado:** 60-90 minutos  
**Quando:** Após planejamento

---

## 🔗 FASE 3: INTEGRAÇÃO DOS SCRIPTS (90-120min)

### Integrar Gerador de Conteúdo (Dia 2)
- [ ] Importar funções necessárias de `Dia2/gerador_conteudo_blog.py`
- [ ] Criar função wrapper `comando_blog(tema: str)`
- [ ] Adicionar tratamento de erros específico
- [ ] Testar comando: `python cli_automatizacoes.py blog --tema "Python"`
- [ ] Verificar se arquivo é salvo corretamente

### Integrar Analisador de Sentimentos (Dia 3)
- [ ] Importar funções necessárias de `Dia3/analisardor_sentimentos.py`
- [ ] Criar função wrapper `comando_sentimentos(arquivo: str)`
- [ ] Adicionar validação de arquivo de reviews
- [ ] Adicionar tratamento de erros específico
- [ ] Testar comando: `python cli_automatizacoes.py sentimentos --arquivo reviews/reviews.txt`
- [ ] Verificar se resultado é salvo corretamente

### Integrar Resumidor de PDFs (Dia 4)
- [ ] Importar funções necessárias de `Dia4/resumidor_pdf.py`
- [ ] Criar função wrapper `comando_resumir(pdf: str, llm: str)`
- [ ] Adicionar validação de arquivo PDF
- [ ] Adicionar tratamento de erros específico
- [ ] Testar comando: `python cli_automatizacoes.py resumir --pdf pdfs/arquivo.pdf --llm groq`
- [ ] Verificar se resumo é salvo corretamente

**Tempo estimado:** 90-120 minutos  
**Quando:** Após estrutura base

---

## 🎨 FASE 4: MELHORIAS E POLIMENTO (60-90min)

### Tratamento de Erros Unificado
- [ ] Criar função `tratar_erro(erro: Exception, contexto: str)`
- [ ] Adicionar mensagens de erro claras e úteis
- [ ] Adicionar sugestões de solução nos erros
- [ ] Testar cenários de erro (arquivo não encontrado, API key inválida, etc.)

### Melhorias de UX
- [ ] Adicionar mensagens de progresso durante execução
- [ ] Adicionar cores no terminal (opcional, usando `colorama`)
- [ ] Adicionar formatação de saída melhorada
- [ ] Adicionar estatísticas de execução (tempo, tokens, etc.)

### Documentação Inline
- [ ] Adicionar docstrings em todas as funções
- [ ] Melhorar help text de cada comando
- [ ] Adicionar exemplos de uso no help
- [ ] Criar README com exemplos de uso

**Tempo estimado:** 60-90 minutos  
**Quando:** Após integração

---

## 🧪 FASE 5: TESTES E VALIDAÇÃO (45-60min)

### Testes Funcionais
- [ ] Testar comando `blog` com diferentes temas
- [ ] Testar comando `sentimentos` com arquivo válido
- [ ] Testar comando `resumir` com diferentes PDFs e LLMs
- [ ] Testar menu interativo
- [ ] Testar tratamento de erros (arquivo não encontrado, etc.)

### Testes de Integração
- [ ] Testar fluxo completo: blog → sentimentos → resumir
- [ ] Verificar se todos os arquivos são salvos corretamente
- [ ] Verificar se logs são gerados corretamente
- [ ] Verificar se mensagens de erro são claras

### Validação Final
- [ ] Executar `python cli_automatizacoes.py --help` e verificar saída
- [ ] Executar cada comando individualmente
- [ ] Verificar se código segue PEP 8 (`autopep8`)
- [ ] Verificar se não há imports não utilizados

**Tempo estimado:** 45-60 minutos  
**Quando:** Após melhorias

---

## 📝 FASE 6: FINALIZAÇÃO (30min)

### Git e Organização
- [ ] Adicionar arquivos: `git add .`
- [ ] Commit: `git commit -m "Dia 6: CLI integrado com 3 automações"`
- [ ] Push: `git push origin main`

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
- Python argparse: https://docs.python.org/3/library/argparse.html
- Python click: https://click.palletsprojects.com/
- CLI Design Best Practices: https://clig.dev/
- Dia 2: `../Dia2/gerador_conteudo_blog.py`
- Dia 3: `../Dia3/analisardor_sentimentos.py`
- Dia 4: `../Dia4/resumidor_pdf.py`

---

## 💡 Dicas Importantes

1. **Reutilização:** Importe funções dos scripts anteriores, não duplique código
2. **Tratamento de Erros:** Mensagens claras ajudam muito o usuário
3. **Help Text:** Documentação inline é essencial para CLI profissional
4. **Testes:** Teste cada comando após integrar
5. **Incremental:** Crie estrutura básica primeiro, depois integre cada script

---

**Última atualização:** 29 Nov 2025

