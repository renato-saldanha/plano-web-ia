#!/usr/bin/env python3
"""
CLI Integrado de Automações com IA Generativa

Este script integra os 3 scripts criados nos dias anteriores:
- Dia 2: Gerador de conteúdo para blog
- Dia 3: Analisador de sentimentos
- Dia 4: Resumidor de PDFs

Uso:
    python cli_automatizacoes.py blog --tema "Python"
    python cli_automatizacoes.py sentimentos --arquivo reviews/reviews.txt
    python cli_automatizacoes.py resumir --pdf pdfs/arquivo.pdf --llm groq
    python cli_automatizacoes.py  # Menu interativo
"""

import argparse
import os
import sys
from pathlib import Path
from typing import Optional

# Adicionar caminhos dos scripts anteriores ao path
sys.path.insert(0, str(Path(__file__).parent.parent / "Dia2"))
sys.path.insert(0, str(Path(__file__).parent.parent / "Dia3"))
sys.path.insert(0, str(Path(__file__).parent.parent / "Dia4"))

import logging
from dotenv import load_dotenv

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S',
)

# Carregar variáveis de ambiente
load_dotenv()

# Imports dos scripts anteriores (serão implementados)
# TODO: Importar funções dos scripts dos dias anteriores


def comando_blog(tema: str) -> None:
    """
    Gerar conteúdo para blog sobre um tema específico.
    
    Args:
        tema: Tema do conteúdo a ser gerado
        
    Example:
        >>> comando_blog("Python")
    """
    logging.info(f"Gerando conteúdo para blog sobre: {tema}")
    # TODO: Integrar com Dia2/gerador_conteudo_blog.py
    print(f"⚠️ Funcionalidade em desenvolvimento: Gerar conteúdo sobre '{tema}'")


def comando_sentimentos(arquivo: str) -> None:
    """
    Analisar sentimentos de reviews em um arquivo.
    
    Args:
        arquivo: Caminho para o arquivo com reviews
        
    Example:
        >>> comando_sentimentos("reviews/reviews.txt")
    """
    logging.info(f"Analisando sentimentos do arquivo: {arquivo}")
    # TODO: Integrar com Dia3/analisardor_sentimentos.py
    print(f"⚠️ Funcionalidade em desenvolvimento: Analisar sentimentos de '{arquivo}'")


def comando_resumir(pdf: str, llm: str = "groq") -> None:
    """
    Resumir um arquivo PDF usando um LLM específico.
    
    Args:
        pdf: Caminho para o arquivo PDF
        llm: LLM a ser usado ('groq' ou 'gemini')
        
    Example:
        >>> comando_resumir("pdfs/arquivo.pdf", "groq")
    """
    logging.info(f"Resumindo PDF: {pdf} com LLM: {llm}")
    # TODO: Integrar com Dia4/resumidor_pdf.py
    print(f"⚠️ Funcionalidade em desenvolvimento: Resumir '{pdf}' com {llm}")


def mostrar_menu() -> str:
    """
    Mostrar menu interativo e retornar escolha do usuário.
    
    Returns:
        Escolha do usuário como string
    """
    print("\n" + "=" * 60)
    print("🤖 CLI de Automações com IA Generativa")
    print("=" * 60)
    print("\nEscolha uma opção:")
    print("  1. Gerar conteúdo para blog")
    print("  2. Analisar sentimentos de reviews")
    print("  3. Resumir arquivo PDF")
    print("  4. Sair")
    print("\n" + "-" * 60)
    
    escolha = input("\nDigite o número da opção: ").strip()
    return escolha


def processar_menu() -> None:
    """
    Processar escolha do menu interativo.
    """
    while True:
        escolha = mostrar_menu()
        
        if escolha == "1":
            tema = input("\nDigite o tema do blog: ").strip()
            if tema:
                comando_blog(tema)
            else:
                print("❌ Tema não pode estar vazio!")
        
        elif escolha == "2":
            arquivo = input("\nDigite o caminho do arquivo de reviews: ").strip()
            if arquivo:
                comando_sentimentos(arquivo)
            else:
                print("❌ Caminho do arquivo não pode estar vazio!")
        
        elif escolha == "3":
            pdf = input("\nDigite o caminho do arquivo PDF: ").strip()
            if pdf:
                llm = input("Escolha o LLM (groq/gemini) [padrão: groq]: ").strip().lower()
                if llm not in ["groq", "gemini"]:
                    llm = "groq"
                comando_resumir(pdf, llm)
            else:
                print("❌ Caminho do PDF não pode estar vazio!")
        
        elif escolha == "4":
            print("\n👋 Até logo!")
            break
        
        else:
            print("\n❌ Opção inválida! Escolha um número de 1 a 4.")
        
        input("\nPressione Enter para continuar...")


def criar_parser() -> argparse.ArgumentParser:
    """
    Criar parser de argumentos para o CLI.
    
    Returns:
        Parser configurado
    """
    parser = argparse.ArgumentParser(
        description="CLI Integrado de Automações com IA Generativa",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:
  %(prog)s blog --tema "Python"
  %(prog)s sentimentos --arquivo reviews/reviews.txt
  %(prog)s resumir --pdf pdfs/arquivo.pdf --llm groq
  %(prog)s  # Menu interativo
        """
    )
    
    subparsers = parser.add_subparsers(dest='comando', help='Comandos disponíveis')
    
    # Comando blog
    parser_blog = subparsers.add_parser(
        'blog',
        help='Gerar conteúdo para blog sobre um tema'
    )
    parser_blog.add_argument(
        '--tema',
        required=True,
        help='Tema do conteúdo a ser gerado'
    )
    
    # Comando sentimentos
    parser_sentimentos = subparsers.add_parser(
        'sentimentos',
        help='Analisar sentimentos de reviews em um arquivo'
    )
    parser_sentimentos.add_argument(
        '--arquivo',
        required=True,
        help='Caminho para o arquivo com reviews (uma por linha)'
    )
    
    # Comando resumir
    parser_resumir = subparsers.add_parser(
        'resumir',
        help='Resumir um arquivo PDF usando IA'
    )
    parser_resumir.add_argument(
        '--pdf',
        required=True,
        help='Caminho para o arquivo PDF a ser resumido'
    )
    parser_resumir.add_argument(
        '--llm',
        choices=['groq', 'gemini'],
        default='groq',
        help='LLM a ser usado para resumir (padrão: groq)'
    )
    
    return parser


def main() -> None:
    """
    Função principal do CLI.
    """
    parser = criar_parser()
    args = parser.parse_args()
    
    # Se nenhum comando foi passado, mostrar menu interativo
    if not args.comando:
        processar_menu()
        return
    
    # Processar comando específico
    try:
        if args.comando == 'blog':
            comando_blog(args.tema)
        
        elif args.comando == 'sentimentos':
            comando_sentimentos(args.arquivo)
        
        elif args.comando == 'resumir':
            comando_resumir(args.pdf, args.llm)
        
        else:
            parser.print_help()
            sys.exit(1)
    
    except KeyboardInterrupt:
        print("\n\n⚠️ Operação cancelada pelo usuário.")
        sys.exit(130)
    
    except Exception as e:
        logging.error(f"❌ Erro ao executar comando: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

