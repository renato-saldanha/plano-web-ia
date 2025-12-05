# ✅ Checklist - Dia 3 (Quarta-feira, 3 Dez 2025)

## 🎯 Objetivo do Dia
RAG básico - Busca e geração com LangChain. Criar sistema que busca informações em documentos antes de gerar resposta.

---

## 📋 FASE 1: PREPARAÇÃO E LEITURA (20min)

### Leitura de Guias
- [ X] Ler `GUIA_RAG_BASICO.md` completo (seções 1-4)
- [ X] Entender o que é RAG e por que usar
- [ X] Entender componentes básicos:
  - [ X] Document Loaders (carregar documentos)
  - [ X] Text Splitters (dividir em chunks)
  - [ X] Retrievers (buscar chunks relevantes)
- [ ]X Revisar conceitos do Dia 2:
  - [ X] Como criar chains com LCEL
  - [ X] Sintaxe `|` (pipe)
  - [ X] Como conectar operações

**Como fazer:**
1. Abra `GUIA_RAG_BASICO.md` e leia seção por seção
2. Não pule a introdução - ela explica o "porquê" do RAG
3. Preste atenção especial na seção sobre componentes básicos
4. Anote mentalmente: "Como isso melhora respostas do LLM?"

**Por que:**
Entender o contexto e propósito é essencial antes de começar a codificar. RAG é um conceito novo que precisa ser compreendido antes da prática.

**Tempo estimado:** 20 minutos  
**Quando:** Início do dia

---

## 💻 FASE 2: PRIMEIRO SISTEMA RAG (50min)

### Entender Exemplo de Referência
- [ X] Abrir arquivo `exemplo_referencia.py`
- [ X] Ler comentários linha por linha
- [ X] Entender cada seção:
  - [ X] Seção 1: Imports e configuração
  - [ X] Seção 2: Carregar documento simples
  - [ X] Seção 3: Dividir em chunks
  - [ X] Seção 4: Criar sistema de busca simples
  - [ X] Seção 5: Criar chain RAG completa
- [ X] Executar script: `python exemplo_referencia.py`
- [ X] Verificar resposta e entender fluxo

**Como fazer:**
1. Abra `exemplo_referencia.py` no editor
2. Leia cada comentário cuidadosamente
3. Execute o script e observe a saída
4. Compare mentalmente com código do Dia 2 (chains simples)

**Por que:**
Exemplo completo comentado ajuda a entender cada parte do RAG. Execução prática consolida aprendizado.

**Tempo estimado:** 20 minutos  
**Quando:** Após Fase 1

### Criar Primeiro Sistema RAG Próprio
- [ ] Abrir arquivo `exercicios/1-rag_simples.py` OU `template.py` (TODO 1)
- [ ] Completar função `rag_simples()` ou TODO 1: Sistema RAG básico
  - [ ] Criar documento de texto simples
  - [ ] Carregar documento usando Document Loader
  - [ ] Dividir em chunks usando Text Splitter
  - [ ] Criar sistema de busca simples
  - [ ] Criar chain RAG (busca + LLM)
  - [ ] Testar com pergunta simples
- [ ] Testar sistema RAG criado
- [ ] Modificar pergunta para ver diferença

**Como fazer:**
1. **Opção A:** Abra `exercicios/1-rag_simples.py` e complete a função
2. **Opção B:** Abra `template.py` e encontre TODO 1
3. Siga as dicas fornecidas no comentário
4. Consulte `exemplo_referencia.py` seção 5 se precisar de ajuda
5. Execute e teste sua chain: `python exercicios/1-rag_simples.py` ou `python template.py`

**Por que:**
Prática guiada consolida aprendizado. Criar seu próprio sistema RAG ajuda a entender o conceito profundamente.

**Tempo estimado:** 30 minutos  
**Quando:** Após entender exemplo de referência

---

## 🔗 FASE 3: RAG COM DOCUMENTOS REAIS (60min)

### Carregar Documentos de Diferentes Formatos
- [ ] Ler seção sobre Document Loaders no `GUIA_RAG_BASICO.md`
- [ ] Completar `exercicios/2-rag_com_pdf.py` OU TODO 2 no `template.py`:
  - [ ] Carregar documento PDF (se disponível)
  - [ ] OU criar documento de texto mais complexo
  - [ ] Dividir em chunks apropriados
  - [ ] Criar sistema de busca
  - [ ] Testar com perguntas sobre o documento
- [ ] Entender diferenças entre loaders

**Como fazer:**
1. Consulte `GUIA_RAG_BASICO.md` para ver exemplos de loaders
2. **Opção A:** Complete `exercicios/2-rag_com_pdf.py`
3. **Opção B:** Complete TODO 2 no `template.py`
4. Teste com diferentes tipos de perguntas
5. Compare com sistema RAG simples anterior

**Por que:**
Documentos reais são mais complexos. Praticar com diferentes formatos prepara para casos reais.

**Tempo estimado:** 25 minutos  
**Quando:** Após Fase 2

### Criar Sistema RAG Funcional Completo
- [ ] Ler seção sobre chains RAG no `GUIA_RAG_BASICO.md`
- [ ] Completar `exercicios/3-rag_completo.py` OU TODO 3 no `template.py`:
  - [ ] Criar sistema RAG completo com múltiplos documentos
  - [ ] Implementar busca inteligente
  - [ ] Criar chain RAG otimizada
  - [ ] Adicionar tratamento de erros
  - [ ] Testar com perguntas complexas
- [ ] Entender como melhorar qualidade das respostas

**Como fazer:**
1. Consulte `GUIA_RAG_BASICO.md` para ver exemplos de chains RAG completas
2. **Opção A:** Complete `exercicios/3-rag_completo.py`
3. **Opção B:** Complete TODO 3 no `template.py`
4. Teste com diferentes perguntas
5. Experimente ajustar tamanho de chunks

**Por que:**
Sistema RAG completo consolida todos os conceitos aprendidos. Prática com casos reais prepara para projetos maiores.

**Tempo estimado:** 25 minutos  
**Quando:** Após carregar documentos

### Completar Exercícios Guiados
- [ ] Abrir `exercicios.md` para ver instruções detalhadas
- [ ] Completar Exercício 1: `exercicios/1-rag_simples.py`
  - [ ] Criar sistema RAG básico
  - [ ] Executar e testar: `python exercicios/1-rag_simples.py`
- [ ] Completar Exercício 2: `exercicios/2-rag_com_pdf.py`
  - [ ] Criar sistema RAG com documentos reais
  - [ ] Executar e testar: `python exercicios/2-rag_com_pdf.py`
- [ ] Completar Exercício 3: `exercicios/3-rag_completo.py`
  - [ ] Criar sistema RAG completo
  - [ ] Executar e testar: `python exercicios/3-rag_completo.py`
- [ ] (Opcional) Exercício 4: `exercicios/4-rag_avancado.py`
  - [ ] Melhorar sistema RAG com otimizações
  - [ ] Executar e testar: `python exercicios/4-rag_avancado.py`

**Como fazer:**
1. Abra `exercicios.md` para ver instruções detalhadas de cada exercício
2. Cada exercício está em um arquivo separado na pasta `exercicios/`
3. Complete a função principal em cada arquivo seguindo os comentários
4. Execute cada arquivo individualmente para testar
5. Não consulte solução antes de tentar
6. Compare sempre com geração simples (sem RAG)

**Por que:**
Prática guiada consolida aprendizado. Exercícios progressivos constroem conhecimento gradualmente.

**Tempo estimado:** 10 minutos  
**Quando:** Após sistema RAG completo

---

## 🔍 FASE 4: COMPARAÇÃO E REFLEXÃO (15min)

### Comparar Abordagens
- [ ] Criar tabela comparativa:
  - [ ] Geração simples (Dia 1) vs RAG básico
  - [ ] Chain simples (Dia 2) vs Chain RAG
  - [ ] Vantagens e desvantagens de cada abordagem
- [ ] Identificar vantagens do RAG:
  - [ ] Respostas baseadas em dados reais
  - [ ] Menos alucinações
  - [ ] Atualização fácil (adicionar documentos)
  - [ ] Rastreabilidade (mostrar fonte)
- [ ] Identificar casos onde RAG é especialmente útil

**Como fazer:**
1. Abra um script do Dia 1 (geração simples) e um sistema RAG criado hoje lado a lado
2. Compare linha por linha
3. Anote diferenças em um arquivo ou papel
4. Reflita sobre quando usar cada abordagem

**Por que:**
Comparação ajuda a entender valor do RAG. Reflexão consolida aprendizado.

**Tempo estimado:** 10 minutos  
**Quando:** Após Fase 3

### Preencher Journal
- [ ] Abrir arquivo `journal.md`
- [ ] Preencher seção "O que foi feito hoje"
- [ ] Preencher seção "O que aprendi hoje"
  - [ ] Conceitos novos aprendidos (RAG, Loaders, Splitters, Retrievers)
  - [ ] Diferenças entre RAG e geração simples
  - [ ] Vantagens identificadas
- [ ] Preencher seção "Insights e Reflexões"
  - [ ] O que funcionou bem?
  - [ ] O que foi difícil?
  - [ ] O que quer explorar mais?
- [ ] Adicionar métricas do dia:
  - [ ] Tempo total gasto
  - [ ] Exercícios completados
  - [ ] Sistemas RAG criados

**Como fazer:**
1. Abra `journal.md` neste diretório
2. Preencha honestamente cada seção
3. Seja específico sobre aprendizados
4. Inclua exemplos práticos

**Por que:**
Journal consolida aprendizado e cria registro pessoal do progresso. Reflexão ajuda a identificar pontos fortes e fracos.

**Tempo estimado:** 5 minutos  
**Quando:** Final do dia

### Git Commit
- [ ] Adicionar arquivos: `git add .`
- [ ] Commit: `git commit -m "feat: adiciona RAG básico - Dia 3 Semana 2"`
- [ ] Push: `git push origin main`

**Tempo estimado:** 5 minutos (incluído no tempo acima)

---

## 🎉 CONCLUSÃO

**Total estimado:** 2h a 2h30min (média de 2h25min)

### ✅ Critérios de Sucesso:
- [ ] Entendeu conceito de RAG e por que usar
- [ ] Entendeu componentes básicos (Loaders, Splitters, Retrievers)
- [ ] Criou pelo menos 1 sistema RAG simples funcional
- [ ] Criou chain RAG completa (busca + geração)
- [ ] Completou pelo menos 3 exercícios guiados
- [ ] Consegue explicar diferença entre RAG e geração simples
- [ ] Journal preenchido com reflexões
- [ ] Commit feito no GitHub

### 🎯 Streak: 10/56 dias

**Parabéns por completar o Dia 3 da Semana 2!** 🚀

Você aprendeu:
- ✅ O que é RAG e por que usar
- ✅ Componentes básicos do RAG (Loaders, Splitters, Retrievers)
- ✅ Como criar sistema RAG simples
- ✅ Como criar chain RAG completa
- ✅ Vantagens do RAG sobre geração simples

**Próximo passo:** Dia 4 - RAG avançado com vector databases (Quinta-feira)

---

**Última atualização:** 3 Dez 2025

