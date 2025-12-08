# Especificações - QA/Polish do Knowledge Assistant (Dia 7)

## Objetivo
Garantir que o agent LangGraph (calculator + RAG FAISS) responda de forma consistente, com docstrings claras, mensagens de erro amigáveis e evidências registradas.

## Requisitos Funcionais
1. **Escolha de tool correta:**  
   - Cálculo aritmético simples → usar `calculadora`.  
   - Perguntas conceituais sobre o corpus → usar `buscar_conhecimento` (FAISS).  
   - Perguntas mistas → combinar RAG + cálculo se necessário.
2. **Mensagens de erro claras:** falta de chave, falta de index, erro de rede devem retornar instruções breves de como corrigir.
3. **Recursion/loop:** `recursion_limit` entre 6 e 10; evitar loops ou chamadas inúteis de tool.
4. **Observabilidade mínima:** registrar `messages` de testes relevantes no journal (inputs, tools chamadas, resposta final).
5. **Handoff:** documentar passos mínimos de execução (setup do .env, localização do index, comando de execução) no README ou journal.

## Requisitos Técnicos
- Orquestração com `langchain.agents.create_agent` e tools decoradas com `@tool`.
- Index FAISS acessível em `../Dia4/faiss_index`; recriar se ausente.
- Python 3.12 recomendado (evita avisos do Pydantic).
- Descrições das tools devem explicitar “quando usar / quando NÃO usar”.

## Casos de Teste (mínimo)
1. **Só cálculo:** “Quanto é (12 * 3) - 7?” → deve chamar apenas calculator.
2. **Só RAG:** Pergunta conceitual coberta pelo corpus (ex.: guia RAG). → deve usar retriever.
3. **Misto:** “No corpus, qual a recomendação de recursion_limit e depois some 2+2?” → deve consultar RAG e calcular.
4. **Ambíguo:** Pergunta vaga (“Ajuda com números e contexto?”) → agent deve escolher a tool mais provável ou pedir clarificação, sem alucinar.
5. **Erro de recurso:** Simular falta do index ou da chave → mensagem amigável sugerindo recriar index ou configurar `.env`.

## Critérios de Aceitação
- Todos os 5 casos de teste registrados no journal com resultado esperado e observações.
- Nenhuma chamada de tool errada nos casos simples (calc vs RAG).
- Mensagens de erro revisadas e copiadas no handoff (onde encontrar/configurar recursos).
- README e CONTEXTO_PROXIMO_DIA atualizados com instruções mínimas para o Dia 8.

## Referências
- Dia 6: `template.py`, `exemplo_referencia.py`, `exercicios.md`
- RAG: `../Dia4/GUIA_RAG_AVANCADO.md`
- Tools/agents: `../Dia5/GUIA_AGENTS.md`
- Scaffolding: `../../GUIAS/GUIA_DECISAO_SCAFFOLDING.md`
- LangGraph Docs: https://python.langchain.com/docs/langgraph

