# 📊 Review da Semana 1 - Fundamentos de IA Generativa

**Período:** 24 Nov - 30 Nov 2025
**Data do Review:** 30 Nov 2025

---

## 📋 Resumo da Semana

### Objetivos Alcançados
- [ X] Setup completo de ambiente Python e APIs
- [ X] Criação de 4 scripts funcionais de automação
- [ X] Comparação de 3 LLMs diferentes
- [ X] Criação de CLI integrado profissional
- [ X] Documentação completa do projeto
- [ X] Deploy no GitHub

### Tempo Investido
- **Tempo estimado:** ___ horas
- **Tempo real:** ___ horas
- **Diferença:** ___ horas

### Scripts Criados
1. `hello_ai_groq.py` - Hello AI básico
2. `gerador_conteudo_blog.py` - Gerador de conteúdo
3. `analisador_sentimentos.py` - Analisador de sentimentos
4. `resumidor_pdf.py` - Resumidor de PDFs
5. `cli_automatizacoes.py` - CLI integrado

---

## 🎓 O que foi Aprendido?

### Conceitos Novos

**TODO: Liste os conceitos que você aprendeu esta semana**

1. **Conceito 1:**
   - O que é: Mesmo prompt gera diferentes respostas.
   - Como funciona: Dar uma persona, contexto e objetivo claro do que deve ser feito, reduz drasticamente a falha.
   - Onde foi aplicado: Nos prompts desenvolvidos.

2. **Conceito 2:**
   - O que é: Tentar gravar um novo arquivo por caminho relativo gera erro de permissão.
   - Como funciona: Estando em modo debug ou em alguns outros casos isolados, ao tentar salvar uma imagem usando o caminho relativo, o sistema não permite por alguma forma de segurança nas permissões.
   - Onde foi aplicado: Nos exercícios de manipulação de pdf e gravação de texto.

3. **Conceito 3:**
   - O que é: Manipulação do pdflumber.
   - Como funciona: pdflumber é uma biblioteca usada para manipular arquivos em formato PDF.
   - Onde foi aplicado: Nos exercícios propostos onde houve necessidade de manipular um arquivo em formato PDF.

4. **Conceito 4:**
   - O que é: Exceções de arquivos.
   - Como funciona: Caso o arquivo esteja aberto ou bloqueado por algum motivo, é necessário usar o PDFSyntaxError do pdfminer para conseguir capturar a exception por conta da dependência que o pdflumber tem no pdfminer.
   - Onde foi aplicado: Ao efetuar a extração do PDF.

5. **Conceito 5:**
   - O que é: Importação de scripts de outros níveis de pasta usando o sys.path.insert.
   - Como funciona: Quando não há um arquivo __init__.py para modularizar uma pasta, se faz necessário o uso do sys.path.insert() para conseguir ler a pasta como um modulo.
   - Onde foi aplicado: Nos exercícios onde necessitei usar os scripts dos dias 2, 3 e 4.

6. **Conceito 6:**
   - O que é: Utilização do colorama para colorir as saída.
   - Como funciona: Aplica estilização nas saídas do terminal, para facilitar a identificação.
   - Onde foi aplicado: Nos tratamentos de exceções do script cli_automaticazoes.py.

7. **Conceito 7:**
   - O que é: Melhora no tratamento de erros.
   - Como funciona: Melhora visual e descritiva dos erros para falicitar o entendimento e busca.
   - Onde foi aplicado: Nos tratamentos de exceções do script cli_automaticazoes.py.


### Habilidades Desenvolvidas

**TODO: Liste habilidades práticas desenvolvidas**

- [ X] Configuração de APIs de IA
- [ X] Criação de scripts Python funcionais
- [ X] Tratamento de erros em Python
- [ X] Uso de logging para debug
- [ X] Criação de CLI com argparse
- [ X] Extração de texto de PDFs
- [ X] Comparação de diferentes LLMs
- [ X] Documentação técnica
- [ X] Versionamento com Git
- [ X] Deploy no GitHub

### Ferramentas Dominadas

**TODO: Liste ferramentas que você aprendeu a usar**

- **Groq API:** 
  - O que aprendi: Aprendi a instanciar e usar.
  - Dificuldades: Configuração inicial.
  
- **Google Gemini API:**
  - O que aprendi: Aprendi a instanciar e usar.
  - Dificuldades: Configuração inicial.

- **pdfplumber:**
  - O que aprendi: Aprendi a manipular arquivos PDF e capturar exceção.
  - Dificuldades: Sem dificuldade.

- **argparse:**
  - O que aprendi: Aprendi a criar CLI com comandos e subcomandos.
  - Dificuldades: Entender a estrutura.

---


