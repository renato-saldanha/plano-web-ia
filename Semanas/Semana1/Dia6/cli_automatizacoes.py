#!/usr/bin/env python3
"""
CLI Integrado de Automações com IA Generativa - Template

TODO: Preencher docstring explicando o propósito do CLI

Este CLI integra os 3 scripts criados nos dias anteriores:
- Dia 2: Gerador de conteúdo para blog
- Dia 3: Analisador de sentimentos
- Dia 4: Resumidor de PDFs

Uso planejado:
    python cli_automatizacoes.py blog --tema "Python"
    python cli_automatizacoes.py sentimentos --arquivo reviews/reviews.txt
    python cli_automatizacoes.py resumir --pdf pdfs/arquivo.pdf --llm groq
    python cli_automatizacoes.py  # Menu interativo
"""

from Semanas.Semana1.Dia4.resumidor_pdf import resumir_pdf
from Semanas.Semana1.Dia3.analisador_sentimentos import comparar_reviews_llm
from Semanas.Semana1.Dia2.gerador_conteudo_blog import gerar_conteudo_tema
import argparse
import os
import sys
import logging
from pathlib import Path
from colorama import Fore, Back, Style, init

init(autoreset=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S',
)

raiz_projeto = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(raiz_projeto))


def comando_blog(tema: str) -> None:
    """
    Gerar conteúdo para um tema de blog.

    Args:
        tema: Tema do blog

    Returns:
        None
    """

    # Validar se tema não está vazio
    if not tema:
        tratar_erro(ValueError("Tema não pode estar vazio!"))

    # Chamar função do Dia 2 para gerar conteúdo
    try:
        # Função que gera conteúdo para um tema de blog
        resultado = gerar_conteudo_tema(tema)
        logging.info(f"{Fore.YELLOW}{Style.DIM}Conteúdo gerado: {resultado}")
    except Exception as e:
        tratar_erro(e)


def comando_sentimentos(arquivo: str) -> None:
    """
    Analisar sentimentos de reviews em um arquivo.

    Args:
        arquivo: Caminho para o arquivo com reviews

    Returns:
        None
    """
    if not arquivo:
        tratar_erro(ValueError("Arquivo não pode estar vazio!"))

    # Chamar funções do Dia 3 para analisar sentimentos
    try:
        resultado = comparar_reviews_llm(arquivo)
        logging.info(f"{Fore.YELLOW}{Style.DIM}Sentimento: {resultado}")
    except Exception as e:
        tratar_erro(e)


def comando_resumir(pdf: str, llm: str = "groq") -> None:
    """
    Resumir um arquivo PDF usando um LLM específico.

    Args:
        pdf: Caminho para o arquivo PDF
        llm: LLM a ser usado ('groq' ou 'gemini')

    Returns:
        None
    """

    # Chama função do Dia 4 para resumir o PDF
    try:
        resultado = resumir_pdf(pdf, llm)
        logging.info(f"{Fore.YELLOW}{Style.DIM}Resumo: {resultado}")
    except Exception as e:
        tratar_erro(e)


def mostrar_menu() -> int:
    """
    Mostrar menu interativo e retornar escolha do usuário.

    Args:
        None

    Returns:
        Escolha do usuário como inteiro (1, 2, 3 ou 4)
    """

    # Mostra o menu
    logging.info(f"{Fore.BLUE}{Style.BRIGHT}Escolha uma opção:")
    logging.info(f"{Fore.BLUE}{Style.BRIGHT}  1. Gerar conteúdo para blog")
    logging.info(
        f"{Fore.BLUE}{Style.BRIGHT}  2. Analisar sentimentos de reviews")
    logging.info(f"{Fore.BLUE}{Style.BRIGHT}  3. Resumir arquivo PDF")
    logging.info(f"{Fore.BLUE}{Style.BRIGHT}  4. Sair")
    logging.info(f"{Fore.BLUE}{Style.BRIGHT}-" * 60)
    return int(input(f"{Fore.BLUE}{Style.BRIGHT}\nDigite o número da opção: "))


def processar_menu() -> None:
    """
    Processar menu interativo

    Args:
        None

    Returns:
        None
    """

    # Loop que valida a escolha do usuário
    while True:
        escolha = mostrar_menu()

        match escolha:
            case 1:
                # Solicita o tema do blog
                tema = input("Digite o tema do blog: ")
                comando_blog(tema)
            case 2:
                # Solicita o arquivo com reviews
                arquivo = input("Digite o caminho do arquivo: ")
                comando_sentimentos(arquivo)
            case 3:
                # Solicita o arquivo PDF e LLM
                arquivo = input("Digite o caminho do arquivo PDF: ")
                llm = input("Digite o LLM a ser usado (groq/gemini): ")
                comando_resumir(arquivo, llm)
            case 4:
                # Sai do loop
                logging.info(f"{Fore.GREEN}{Style.DIM}Até logo!")
                break
            case _:
                logging.warning(f"{Back.YELLOW}{Fore.RED}Opção inválida!")
                logging.warning(f"{Back.YELLOW}{Fore.RED}{Style.DIM}=" * 60)


def criar_parser() -> argparse.ArgumentParser:
    """
    Criar parser principal e subparsers blog, sentimentos e resumir

    """

    try:
        parser = argparse.ArgumentParser(
            description="CLI para automação de blog, sentimentos e resumir",
            epilog="Exemplo de uso: python cli_automatizacoes.py blog --tema 'Python'"
            " ou python cli_automatizacoes.py sentimentos --arquivo 'reviews/reviews.txt'"
            " ou python cli_automatizacoes.py resumir --pdf 'pdfs/arquivo.pdf' --llm 'groq'"
        )

        subparsers = parser.add_subparsers(
            dest="comando", help="Comando a ser executado blog, sentimentos ou resumir")

        parser_blog = subparsers.add_parser(
            'blog', help="Gerar conteúdo para blog")
        parser_blog.add_argument(
            "--tema", required=True, help="Tema do conteúdo")

        parser_sentimentos = subparsers.add_parser(
            'sentimentos', help="Analisar sentimentos de reviews")
        parser_sentimentos.add_argument(
            "--arquivo", required=True, help="Arquivo com reviews")

        parser_resumir = subparsers.add_parser('resumir', help="Resumir PDF")
        parser_resumir.add_argument("--pdf", required=True, help="Arquivo PDF")
        parser_resumir.add_argument("--llm", required=True, help="LLM a ser usado", choices=["groq", "gemini"])

        return parser
    except Exception as e:
        tratar_erro(e)


def main() -> None:
    """
    Função principal do CLI.

    TODO: Implementar lógica principal que:
    1. Cria parser
    2. Parseia argumentos
    3. Se nenhum comando, mostra menu interativo
    4. Se comando específico, processa comando
    5. Trata erros (KeyboardInterrupt, Exception)

    Dica: Consulte exemplo_cli_simples.py para ver estrutura completa
    """

    try:
        parser = criar_parser()

        if len(sys.argv) == 1:
            processar_menu()
            return
        else:
            args = parser.parse_args()

            match args.comando:
                case "blog":
                    comando_blog(args.tema)
                case "sentimentos":
                    comando_sentimentos(args.arquivo)
                case "resumir":
                    comando_resumir(args.pdf, args.llm)
                case _:
                    logging.warning(f"{Back.RED}Comando inválido!")
    except KeyboardInterrupt:
        tratar_erro(KeyboardInterrupt)
    except Exception as e:
        tratar_erro(e)
    finally:
        logging.info(f"{Fore.GREEN}Comando executado com sucesso!")
        logging.info(f"{Fore.GREEN}{Style.DIM}Até logo!")


def tratar_erro(erro: Exception | KeyboardInterrupt) -> None:
    """
    Tratar erro

    Args:
        erro: Erro

    Returns:
        None
    """
    if isinstance(erro, KeyboardInterrupt):
        logging.error(f"{Back.RED}Interrompido pelo usuário!")
    elif isinstance(erro, ValueError):
        logging.error(f"{Back.RED}Verifique o valor informado: {erro.args[0]}")
    else:
        logging.error(f"{Back.RED}Erro inesperado: {erro.args[0]}")

    logging.error("=" * 60)


if __name__ == "__main__":
    main()
