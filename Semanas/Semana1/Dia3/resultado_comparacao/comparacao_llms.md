# Comparação de Análise de Sentimentos

**Data:** 2025-11-30 01:01:31

| # | Review | Sentimento Groq | Sentimento Gemini | Concordância |    Groq (ms)    |    Gemini (ms)    |    Tokens gastos Groq    |    Tokens gastos Gemini    |
|---|--------|-----------------|-------------------|--------------|-----------------|-------------------|--------------------------|----------------------------|
| 1 | ## Review 1 - Este produto é incrível! Funciona... | positivo | positivo | ✅ SIM | 443 | 2213 |   113   |   70   |
| 2 | ## Review 2 - Péssima qualidade, não recomendo.... | negativo | negativo | ✅ SIM | 204 | 1438 |   118   |   75   |
| 3 | ## Review 3 - O produto é ok, nada especial mas... | neutro. | neutro | ❌ NÃO | 217 | 2282 |   111   |   66   |
| 4 | ## Review 4 - Estou muito satisfeito com a comp... | positivo | positivo | ✅ SIM | 213 | 1636 |   148   |   95   |
| 5 | ## Review 5 - Decepcionado. O produto não corre... | negativo | negativo | ✅ SIM | 215 | 1354 |   145   |   92   |

## 📈 Estatísticas

- **Total de Reviews:** 5
- **Concordâncias:** 4/5
- **Percentual de Concordância:** 80.0%
- **LLM Mais Rápido:** Groq
- **Tempo Médio Groq:** 258ms
- **Tempo Médio Gemini:** 1785ms
