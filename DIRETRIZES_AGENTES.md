# 🤖 Diretrizes para Agentes IA

Este arquivo contém diretrizes importantes que agentes IA devem seguir ao trabalhar neste projeto.

---

## 📅 Referências e Documentação

### ⚠️ IMPORTANTE: Data de Referência para Documentação

**SEMPRE usar referências de julho de 2025 para frente.**

Ao criar ou atualizar guias, documentação, exemplos de código ou qualquer conteúdo técnico:

- ✅ **Usar:** Documentação, APIs, bibliotecas e padrões atualizados a partir de **julho de 2025**
- ✅ **Verificar:** Se há versões mais recentes das bibliotecas mencionadas
- ✅ **Atualizar:** Exemplos de código para refletir as melhores práticas atuais
- ✅ **Documentar:** Sempre incluir a data de referência no final do arquivo

**Exemplo de como documentar:**
```markdown
**Última atualização:** [Data]  
**Referências:** Baseado em documentação [Biblioteca/Framework] de julho de 2025 em diante
```

**Por que isso é importante:**
- APIs e bibliotecas evoluem rapidamente
- Sintaxe e padrões podem mudar entre versões
- Garante que exemplos funcionem com versões atuais
- Evita erros de compatibilidade

---

## 📚 Padrões de Qualidade

### Verificação de Código

Ao criar ou corrigir exemplos de código:

1. **Testar mentalmente o fluxo de dados:**
   - Verificar tipos de entrada e saída de cada componente
   - Garantir compatibilidade entre chains conectadas
   - Validar que templates recebem os dados corretos

2. **Verificar sintaxe atual:**
   - Consultar documentação oficial mais recente
   - Usar padrões recomendados pela biblioteca
   - Evitar sintaxe deprecada

3. **Incluir explicações:**
   - Comentar código complexo
   - Explicar por que certas conversões são necessárias
   - Adicionar avisos sobre erros comuns

### Exemplo de Boa Prática

```python
# ✅ BOM: Inclui explicação e aviso
# ⚠️ IMPORTANTE: generate_chain retorna string, mas format_chain espera dict
full_chain = (
    generate_chain 
    | RunnableLambda(lambda x: {"text": x})  # Converte string → dict
    | format_chain
)
```

```python
# ❌ RUIM: Sem explicação, código pode não funcionar
full_chain = generate_chain | format_chain  # Erro!
```

---

## 🔄 Processo de Criação de Novos Dias

Ao criar um novo dia (usando templates ou guias):

1. **Consultar diretrizes:**
   - Ler este arquivo primeiro
   - Verificar `METODOLOGIA_ENSINO.md` para estrutura
   - Consultar `TEMPLATE_CONTEXTO_PROXIMO_DIA.md` para transições

2. **Aplicar padrão de referências:**
   - Usar documentação de julho de 2025 em diante
   - Verificar se há atualizações nas bibliotecas mencionadas
   - Testar mentalmente exemplos de código

3. **Validar consistência:**
   - Seguir estrutura padrão de arquivos
   - Manter nomenclatura consistente
   - Garantir que exemplos sejam funcionais

---

## 📝 Checklist para Agentes

Antes de finalizar qualquer guia ou exemplo:

- [ ] Código usa sintaxe atualizada (julho 2025+)
- [ ] Exemplos foram verificados mentalmente para erros
- [ ] Explicações claras sobre conversões de tipos
- [ ] Avisos sobre erros comuns incluídos
- [ ] Data de referência documentada
- [ ] Links para documentação oficial incluídos quando relevante

---

## 🎯 Quando Criar ou Atualizar Conteúdo

### Criar novo conteúdo quando:
- Novo dia está sendo criado
- Novo conceito precisa ser explicado
- Exemplo adicional seria útil

### Atualizar conteúdo existente quando:
- Erro é identificado (como no GUIA_CHAINS.md)
- Sintaxe está desatualizada
- Melhor explicação é possível
- Padrões da biblioteca mudaram

---

## 📋 Padrões de Consistência do Projeto

### Arquivos Obrigatórios (Ordem Padrão)

Todos os dias devem ter estes arquivos na ordem especificada:

1. **README.md** - Contexto e objetivos do dia
2. **CONTEXTO_AGENTE.md** - Informações técnicas detalhadas
3. **checklist.md** - Tarefas práticas divididas em fases
4. **journal.md** - Template para reflexão
5. **requirements.txt** - Dependências Python (obrigatório sempre, mesmo que vazio)
6. **CONTEXTO_PROXIMO_DIA.md** - Guia para construir próximo dia (obrigatório para TODOS os dias)

**Por que esta ordem:** Segue o fluxo natural de aprendizado (contexto → detalhes → tarefas → reflexão → dependências → transição).

### Níveis de Scaffolding

**⚠️ IMPORTANTE:** Os níveis são determinados pelo **CONCEITO**, não pela posição temporal (dia/semana).

**Regra de Decisão:**
- **Nível 1:** Conceito completamente novo, primeira exposição
- **Nível 2:** Conceito parcialmente conhecido, aplicação em novo contexto
- **Nível 3:** Conceitos conhecidos, aplicação independente

**Exemplos:**
- Semana 1, Dia 1: Nível 1 (conceito novo: usar APIs diretamente)
- Semana 2, Dia 1: Nível 1 (conceito novo: LangChain)
- Semana 2, Dia 2: Nível 2 (conceito parcialmente conhecido: já sabe LangChain básico, agora aplica em chains)

**Consulte:** `GUIAS/GUIA_DECISAO_SCAFFOLDING.md` para matriz de decisão detalhada.

---

## 📚 Recursos de Referência

### Documentação Oficial (sempre verificar versões mais recentes):
- **LangChain:** https://python.langchain.com/docs/
- **LangChain Expression Language:** https://python.langchain.com/docs/expression_language/
- **Groq API:** https://console.groq.com/docs

### Arquivos de Referência no Projeto:
- `METODOLOGIA_ENSINO.md` - Metodologia de ensino
- `TEMPLATE_ESTRUTURA_DIA.md` - Estrutura padrão de um dia
- `TEMPLATE_CONTEXTO_PROXIMO_DIA.md` - Template para transições
- `GUIAS/GUIA_CRIAR_NOVO_DIA.md` - Processo de criação de dias
- `GUIAS/GUIA_DECISAO_SCAFFOLDING.md` - Decisão de nível de scaffolding

---

**Última atualização:** 2 Dez 2025  
**Versão:** 2.0

