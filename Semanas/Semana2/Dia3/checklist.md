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
- [X] Abrir arquivo `exercicios/1-rag_simples.py` OU `template.py` (TODO 1)
- [X] Completar função `rag_simples()` ou TODO 1: Sistema RAG básico
  - [X] Criar documento de texto simples
  - [X] Carregar documento usando Document Loader
  - [X] Dividir em chunks usando Text Splitter
  - [X] Criar sistema de busca simples
  - [X] Criar chain RAG (busca + LLM)
  - [X] Testar com pergunta simples
- [X] Testar sistema RAG criado
- [X] Modificar pergunta para ver diferença

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
- [X] Ler seção sobre Document Loaders no `GUIA_RAG_BASICO.md`
- [X] Completar `exercicios/2-rag_com_pdf.py` OU TODO 2 no `template.py`:
  - [X] Carregar documento PDF (se disponível)
  - [X] OU criar documento de texto mais complexo
  - [X] Dividir em chunks apropriados
  - [X] Criar sistema de busca
  - [X] Testar com perguntas sobre o documento
- [X] Entender diferenças entre loaders

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
- [X] Ler seção sobre chains RAG no `GUIA_RAG_BASICO.md`
- [X] Completar `exercicios/3-rag_avancado.py` OU TODO 3 no `template.py`:
  - [X] Criar sistema RAG completo com múltiplos documentos
  - [X] Implementar busca inteligente
  - [X] Criar chain RAG otimizada (STUFF e MAP-REDUCE)
  - [X] Adicionar tratamento de erros (limpeza de arquivos temporários)
  - [X] Testar com perguntas complexas
- [X] Entender como melhorar qualidade das respostas

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
- [ X] Abrir `exercicios.md` para ver instruções detalhadas
- [ X] Completar Exercício 1: `exercicios/1-rag_simples.py`
  - [ X] Criar sistema RAG básico
  - [ X] Executar e testar: `python exercicios/1-rag_simples.py`
- [ X] Completar Exercício 2: `exercicios/2-rag_com_pdf.py`
  - [ X] Criar sistema RAG com documentos reais
  - [ X] Executar e testar: `python exercicios/2-rag_com_pdf.py`
- [ X] Completar Exercício 3: `exercicios/3-rag_avancado.py`
  - [ X] Melhorar sistema RAG com otimizações
  - [ X] Executar e testar: `python exercicios/3-rag_avancado.py`

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
- [ X] Criar tabela comparativa:
  - [ X] Geração simples (Dia 1) vs RAG básico
  - [ X] Chain simples (Dia 2) vs Chain RAG
  - [ X] Vantagens e desvantagens de cada abordagem
- [ X] Identificar vantagens do RAG:
  - [ X] Respostas baseadas em dados reais
  - [ X] Menos alucinações
  - [ X] Atualização fácil (adicionar documentos)
  - [ X] Rastreabilidade (mostrar fonte)
- [ X] Identificar casos onde RAG é especialmente útil

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
- [X ] Abrir arquivo `journal.md`
- [ X] Preencher seção "O que foi feito hoje"
- [ X] Preencher seção "O que aprendi hoje"
  - [ X] Conceitos novos aprendidos (RAG, Loaders, Splitters, Retrievers)
  - [ X] Diferenças entre RAG e geração simples
  - [ X] Vantagens identificadas
- [ X] Preencher seção "Insights e Reflexões"
  - [ X] O que funcionou bem?
  - [ X] O que foi difícil?
  - [ X] O que quer explorar mais?
- [ X] Adicionar métricas do dia:
  - [ X] Tempo total gasto
  - [ X] Exercícios completados
  - [ X] Sistemas RAG criados

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
- [ X] Adicionar arquivos: `git add .`
- [ X] Commit: `git commit -m "feat: adiciona RAG básico - Dia 3 Semana 2"`
- [ X] Push: `git push origin main`

**Tempo estimado:** 5 minutos (incluído no tempo acima)

---

## 🎉 CONCLUSÃO

**Total estimado:** 2h a 2h30min (média de 2h25min)

### ✅ Critérios de Sucesso:
- [X] Entendeu conceito de RAG e por que usar
- [X] Entendeu componentes básicos (Loaders, Splitters, Retrievers)
- [X] Criou pelo menos 1 sistema RAG simples funcional (3 exercícios completos)
- [X] Criou chain RAG completa (busca + geração) - STUFF e MAP-REDUCE
- [X] Completou pelo menos 3 exercícios guiados (1-rag_simples, 2-rag_com_pdf, 3-rag_avancado)
- [X] Consegue explicar diferença entre RAG e geração simples
- [ X] Journal preenchido com reflexões (parcialmente preenchido)
- [ X] Commit feito no GitHub (verificar status)

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

