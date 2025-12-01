# Comparação de Análise de Sentimentos

**Data:** 2025-11-30 15:41:35

| # | Review | Sentimento Groq | Sentimento Gemini | Concordância |    Groq (ms)    |    Gemini (ms)    |    Tokens gastos Groq    |    Tokens gastos Gemini    |
|---|--------|-----------------|-------------------|--------------|-----------------|-------------------|--------------------------|----------------------------|
| 1 | ## Review 1 - Este produto é incrível! Funciona... | positivo | positivo | ✅ SIM | 518 | 1656 |   113   |   70   |
| 2 | ## Review 2 - Péssima qualidade, não recomendo.... | negativo | negativo | ✅ SIM | 214 | 1475 |   118   |   75   |
| 3 | ## Review 3 - O produto é ok, nada especial mas... | neutro. | neutro | ❌ NÃO | 213 | 2153 |   111   |   66   |
| 4 | ## Review 4 - Estou muito satisfeito com a comp... | positivo. | positivo | ❌ NÃO | 218 | 1181 |   149   |   95   |
| 5 | ## Review 5 - Decepcionado. O produto não corre... | negativo | negativo | ✅ SIM | 215 | 1727 |   145   |   92   |

## 📈 Estatísticas

- **Total de Reviews:** 5
- **Concordâncias:** 3/5
- **Percentual de Concordância:** 60.0%
- **LLM Mais Rápido:** Groq
- **Tempo Médio Groq:** 276ms
- **Tempo Médio Gemini:** 1638ms
