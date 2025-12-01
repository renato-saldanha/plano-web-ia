"""
## 📋 Exercício 5: CLI Completo - Desafio Final (Nível Avançado)

### Objetivo
Criar um CLI completo integrando os scripts dos dias anteriores.

### Tarefa
Crie um CLI `cli_automatizacoes.py` que:
1. Tem 3 subcomandos: `blog`, `sentimentos`, `resumir`
2. Integra funções dos dias 2, 3 e 4
3. Tem menu interativo quando nenhum comando é passado
4. Trata erros adequadamente
5. Usa logging para feedback

### Requisitos:
- Comando `blog --tema "Python"` → chama função do Dia 2
- Comando `sentimentos --arquivo reviews\reviews.txt` → chama funções do Dia 3
- Comando `resumir --pdf 'D:\plano web+ia\Semanas\Semana1\Dia4\pdfs\Apresentação GERAL VETOR.pdf' --llm 'groq'` → chama função do Dia 4
- Menu interativo com todas as opções

### Dica
Use `template_cli.py` como base e preencha os TODOs.
"""

import argparse
import logging
import sys
import os
from pathlib import Path

# Adicionar o diretório raiz ao path para imports absolutos
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent.parent))

from Semanas.Semana1.Dia2.gerador_conteudo_blog import gerar_conteudo_tema
from Semanas.Semana1.Dia3.analisador_sentimentos import comparar_reviews_llm
from Semanas.Semana1.Dia4.resumidor_pdf import extrair_texto_pdf, resumir_pdf

logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    datefmt = '%H:%M:%S',
)

def main():
    """
    Função principal
    :return: None
    """

    try:        
        # Cria o parser principal
        arg_parser = argparse.ArgumentParser(
            description = "CLI com menu interativo, subcomandos e integração com funções existentes do Dia 2, 3 e 4",
            epilog = "Exemplo de uso: python 5-cli_automatizacoes.py"
        )

        # Cria o subparser para as operações matemáticas
        sub_parser = arg_parser.add_subparsers(dest = "comandos", help = "Comando `blog`, `sentimentos` ou `resumir`")
        
        parser_blog = sub_parser.add_parser ("blog", help = "Gera um blog sobre um tema")
        parser_blog.add_argument("--tema", required = True, type = str, help = "Tema do blog")

        parser_sentimentos = sub_parser.add_parser ("sentimentos", help = "Analisa o sentimento de um arquivo")
        parser_sentimentos.add_argument("--arquivo", required = True, type = str, help = "Arquivo a ser analisado")

        parser_resumir = sub_parser.add_parser ("resumir", help = "Resumir um arquivo PDF")
        parser_resumir.add_argument("--pdf", required = True, type = str, help = "PDF a ser resumido")
        parser_resumir.add_argument("--llm", choices = ['groq', 'gemini'], default = 'groq', type = str, help = "LLM a ser usado")

        # Faz o parse dos argumentos
        args = arg_parser.parse_args()
            
        # Faz o match do comando
        match args.comandos:
            case "blog":
                conteudo = gerar_conteudo_tema(args.tema)
                logging.info(f"Conteúdo gerado: {conteudo}")
            case "sentimentos":
                sentimento = comparar_reviews_llm(args.arquivo)
                logging.info(f"Sentimento: {sentimento}")
            case "resumir":
                texto = extrair_texto_pdf(args.pdf)
                resumo = resumir_pdf(texto, args.pdf, args.llm)
                logging.info(f"Resumo: {resumo}")
            case _:
                raise ValueError("Comando inválido \n" + "=" * 50)
    except Exception as e:
        logging.error(f"Erro ao executar comando: {e}")
        logging.error("=" * 50)
        return

# Executa a função principal
if __name__ == "__main__":
    main()
