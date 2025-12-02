# 📚 Estrutura e Metodologia do Projeto

Este documento explica a estrutura do projeto e como navegar pelos recursos de aprendizado.

---

## 🎯 Visão Geral

Este projeto segue uma **metodologia de ensino baseada em Scaffolding e Progressive Disclosure**, garantindo aprendizado efetivo através de prática guiada e progressiva.

---

## 📁 Estrutura de Diretórios

```
plano web+ia/
├── METODOLOGIA_ENSINO.md              # Metodologia geral do projeto
├── TEMPLATE_ESTRUTURA_DIA.md          # Template para criar novos dias
├── TEMPLATE_CONTEXTO_PROXIMO_DIA.md   # Template para transição entre dias
│
├── GUIAS/
│   ├── GUIA_DECISAO_SCAFFOLDING.md    # Como decidir nível de scaffolding
│   ├── GUIA_CRIAR_NOVO_DIA.md         # Processo completo para criar dia
│   └── [outros guias específicos]
│
├── Semanas/
│   ├── Semana1/
│   │   ├── README.md                  # Visão geral da semana
│   │   ├── Dia1/
│   │   │   ├── README.md
│   │   │   ├── CONTEXTO_AGENTE.md
│   │   │   ├── checklist.md
│   │   │   ├── journal.md
│   │   │   └── CONTEXTO_PROXIMO_DIA.md  # Guia para Dia 2
│   │   ├── Dia2/
│   │   └── ...
│   └── Semana2/
│       └── ...
│
└── [outros arquivos do projeto]
```

---

## 🎓 Como Usar Esta Estrutura

### Para Estudantes

1. **Começar um novo dia:**
   - Ler `README.md` do dia para contexto
   - Ler `CONTEXTO_PROXIMO_DIA.md` do dia anterior (se existir)
   - Seguir `checklist.md` passo a passo

2. **Durante o aprendizado:**
   - Consultar guias de aprendizado quando necessário
   - Usar templates/exemplos como referência
   - Tentar implementar antes de consultar soluções

3. **Ao finalizar:**
   - Preencher `journal.md`
   - Ler `CONTEXTO_PROXIMO_DIA.md` para preparar próximo dia

### Para Criadores de Conteúdo (Agentes IA)

1. **Criar novo dia:**
   - Seguir `GUIAS/GUIA_CRIAR_NOVO_DIA.md`
   - Usar `TEMPLATE_ESTRUTURA_DIA.md` como base
   - Determinar nível usando `GUIAS/GUIA_DECISAO_SCAFFOLDING.md`

2. **Garantir transição:**
   - Criar `CONTEXTO_PROXIMO_DIA.md` usando `TEMPLATE_CONTEXTO_PROXIMO_DIA.md`
   - Incluir guia completo para próximo dia
   - Listar recursos de preparação

---

## 📋 Documentos Principais

### Metodologia e Templates

1. **METODOLOGIA_ENSINO.md**
   - Metodologia geral (Scaffolding + Progressive Disclosure)
   - Níveis de scaffolding explicados
   - Fluxo de aprendizado
   - Critérios de sucesso

2. **TEMPLATE_ESTRUTURA_DIA.md**
   - Estrutura padrão de um dia
   - Templates de todos os arquivos
   - Exemplos por nível de scaffolding
   - Checklist de criação

3. **TEMPLATE_CONTEXTO_PROXIMO_DIA.md**
   - Template para transição entre dias
   - Estrutura completa de contexto
   - Guia para construir próximo dia

### Guias Práticos

4. **GUIAS/GUIA_DECISAO_SCAFFOLDING.md**
   - Matriz de decisão para nível de scaffolding
   - Exemplos práticos por tipo de conteúdo
   - Progressão natural por semana

5. **GUIAS/GUIA_CRIAR_NOVO_DIA.md**
   - Processo passo-a-passo completo
   - Checklist detalhado
   - Exemplos práticos

---

## 🔄 Fluxo de Criação de um Dia

```
1. Analisar contexto (dia anterior + plano)
   ↓
2. Determinar nível de scaffolding
   ↓
3. Criar estrutura básica (README, CONTEXTO_AGENTE, checklist, journal)
   ↓
4. Criar arquivos de aprendizado (conforme nível)
   ↓
5. Criar CONTEXTO_PROXIMO_DIA.md
   ↓
6. Revisão final
```

**Tempo estimado:** 2-3 horas por dia completo

---

## ✅ Garantias de Clareza

A estrutura garante clareza porque:

1. **Metodologia documentada:** `METODOLOGIA_ENSINO.md` explica o "porquê"
2. **Templates completos:** `TEMPLATE_ESTRUTURA_DIA.md` fornece o "como"
3. **Guia de decisão:** `GUIA_DECISAO_SCAFFOLDING.md` ajuda a decidir nível
4. **Processo passo-a-passo:** `GUIA_CRIAR_NOVO_DIA.md` guia criação completa
5. **Transição clara:** `CONTEXTO_PROXIMO_DIA.md` em cada dia explica próximo
6. **Exemplos práticos:** Dia 6 serve como referência completa

---

## 🎯 Exemplo de Uso

### Cenário: Criar Semana 2, Dia 1 (LangChain básico)

1. **Consultar:** `GUIAS/GUIA_CRIAR_NOVO_DIA.md`
2. **Decidir nível:** `GUIAS/GUIA_DECISAO_SCAFFOLDING.md` → Nível 1 (conceito novo)
3. **Usar template:** `TEMPLATE_ESTRUTURA_DIA.md` → Copiar estrutura Nível 1
4. **Criar arquivos:**
   - README.md (usar template)
   - CONTEXTO_AGENTE.md (usar template)
   - checklist.md (adaptar template)
   - exemplo_langchain_basico.py (código completo comentado)
   - GUIA_PASSO_A_PASSO.md (tutorial detalhado)
   - journal.md (usar template)
   - CONTEXTO_PROXIMO_DIA.md (usar `TEMPLATE_CONTEXTO_PROXIMO_DIA.md`)
5. **Revisar:** Consistência e completude

---

## 💡 Princípios Fundamentais

1. **Consistência:** Todos os dias seguem mesma estrutura
2. **Progressão:** Cada dia constrói sobre anteriores
3. **Clareza:** Contexto sempre disponível para próximo dia
4. **Flexibilidade:** Nível de scaffolding adaptado ao conteúdo
5. **Aprendizado ativo:** Aluno escreve código, não apenas copia

---

## 📚 Recursos por Necessidade

### Preciso criar um novo dia
→ `GUIAS/GUIA_CRIAR_NOVO_DIA.md`

### Não sei qual nível de scaffolding usar
→ `GUIAS/GUIA_DECISAO_SCAFFOLDING.md`

### Preciso de template de estrutura
→ `TEMPLATE_ESTRUTURA_DIA.md`

### Preciso criar transição para próximo dia
→ `TEMPLATE_CONTEXTO_PROXIMO_DIA.md`

### Quero entender a metodologia
→ `METODOLOGIA_ENSINO.md`

### Preciso de exemplo completo
→ Ver `Semanas/Semana1/Dia6/` como referência

---

**Última atualização:** 30 Nov 2025  
**Versão:** 1.1  
**Status:** ✅ Atualizado

