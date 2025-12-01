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

import argparse
import os
import sys
from pathlib import Path
from typing import Optional

# TODO: Importar logging e configurar
# Dica: Use logging.basicConfig com level=logging.INFO
# Formato sugerido: '%(asctime)s - %(levelname)s - %(message)s'

# TODO: Importar load_dotenv e carregar variáveis de ambiente
# Dica: from dotenv import load_dotenv, depois load_dotenv()

# TODO: Importar funções dos scripts anteriores
# Dica 1: Para Dia 2: from Semanas.Semana1.Dia2.gerador_conteudo_blog import gerar_conteudo_tema
# Dica 2: Para Dia 3: from Semanas.Semana1.Dia3.analisador_sentimentos import [funções necessárias]
# Dica 3: Para Dia 4: from Semanas.Semana1.Dia4.resumidor_pdf import [funções necessárias]
# Consulte os scripts originais para ver quais funções exportar


def comando_blog(tema: str) -> None:
    """
    Gerar conteúdo para blog sobre um tema específico.
    
    TODO: Implementar função que:
    1. Valida se tema não está vazio
    2. Chama função do Dia 2 para gerar conteúdo
    3. Mostra resultado ou salva arquivo
    4. Trata erros adequadamente
    
    Args:
        tema: Tema do conteúdo a ser gerado
        
    Dica: Consulte exemplo_cli_simples.py para ver estrutura similar
    """
    # TODO: Validar entrada
    # if not tema or tema.strip() == "":
    #     logging.error("Tema não pode estar vazio!")
    #     sys.exit(1)
    
    # TODO: Chamar função do Dia 2
    # resultado = gerar_conteudo_tema(tema)
    
    # TODO: Processar resultado
    # logging.info(f"Conteúdo gerado: {resultado}")
    pass


def comando_sentimentos(arquivo: str) -> None:
    """
    Analisar sentimentos de reviews em um arquivo.
    
    TODO: Implementar função que:
    1. Valida se arquivo existe
    2. Lê arquivo de reviews
    3. Chama funções do Dia 3 para analisar
    4. Mostra ou salva resultados
    5. Trata erros adequadamente
    
    Args:
        arquivo: Caminho para o arquivo com reviews
        
    Dica: Use os.path.exists() para verificar se arquivo existe
    """
    # TODO: Validar se arquivo existe
    # if not os.path.exists(arquivo):
    #     logging.error(f"Arquivo não encontrado: {arquivo}")
    #     sys.exit(1)
    
    # TODO: Ler arquivo
    # with open(arquivo, 'r', encoding='utf-8') as f:
    #     reviews = f.readlines()
    
    # TODO: Chamar funções do Dia 3
    # resultado_groq = analisar_sentimento_groq(...)
    # resultado_gemini = analisar_sentimento_gemini(...)
    
    # TODO: Processar e mostrar resultados
    pass


def comando_resumir(pdf: str, llm: str = "groq") -> None:
    """
    Resumir um arquivo PDF usando um LLM específico.
    
    TODO: Implementar função que:
    1. Valida se PDF existe
    2. Valida se LLM é válido ('groq' ou 'gemini')
    3. Chama função do Dia 4 para resumir
    4. Mostra ou salva resumo
    5. Trata erros adequadamente
    
    Args:
        pdf: Caminho para o arquivo PDF
        llm: LLM a ser usado ('groq' ou 'gemini')
    """
    # TODO: Validar PDF existe
    # TODO: Validar LLM é válido
    # TODO: Chamar função do Dia 4
    # TODO: Processar resultado
    pass


def mostrar_menu() -> str:
    """
    Mostrar menu interativo e retornar escolha do usuário.
    
    TODO: Criar menu com opções:
    1. Gerar conteúdo para blog
    2. Analisar sentimentos de reviews
    3. Resumir arquivo PDF
    4. Sair
    
    Returns:
        Escolha do usuário como string
        
    Dica: Use print() para mostrar menu e input() para receber escolha
    """
    # TODO: Criar menu visualmente atraente
    # print("\n" + "=" * 60)
    # print("🤖 CLI de Automações com IA Generativa")
    # print("=" * 60)
    # print("\nEscolha uma opção:")
    # print("  1. Gerar conteúdo para blog")
    # print("  2. Analisar sentimentos de reviews")
    # print("  3. Resumir arquivo PDF")
    # print("  4. Sair")
    
    # escolha = input("\nDigite o número da opção: ").strip()
    # return escolha
    pass


def processar_menu() -> None:
    """
    Processar escolha do menu interativo.
    
    TODO: Implementar loop que:
    1. Mostra menu
    2. Recebe escolha do usuário
    3. Chama função apropriada baseada na escolha
    4. Continua até usuário escolher sair
    
    Dica: Use while True com break para sair
    """
    # TODO: Criar loop while True
    # while True:
    #     escolha = mostrar_menu()
    #     
    #     if escolha == "1":
    #         tema = input("\nDigite o tema do blog: ").strip()
    #         if tema:
    #             comando_blog(tema)
    #         else:
    #             print("❌ Tema não pode estar vazio!")
    #     
    #     elif escolha == "2":
    #         # TODO: Implementar opção 2
    #         pass
    #     
    #     elif escolha == "3":
    #         # TODO: Implementar opção 3
    #         pass
    #     
    #     elif escolha == "4":
    #         print("\n👋 Até logo!")
    #         break
    #     
    #     else:
    #         print("\n❌ Opção inválida!")
    #     
    #     input("\nPressione Enter para continuar...")
    pass


def criar_parser() -> argparse.ArgumentParser:
    """
    Criar parser de argumentos para o CLI.
    
    TODO: Criar parser com:
    1. Descrição do CLI
    2. Subparsers para cada comando (blog, sentimentos, resumir)
    3. Argumentos necessários para cada comando
    
    Returns:
        Parser configurado
        
    Dica: Consulte GUIA_CLI.md seção "Passo 2: Adicionar Subcomandos"
    """
    # TODO: Criar parser principal
    # parser = argparse.ArgumentParser(
    #     description="CLI Integrado de Automações com IA Generativa",
    #     formatter_class=argparse.RawDescriptionHelpFormatter
    # )
    
    # TODO: Criar subparsers
    # subparsers = parser.add_subparsers(dest='comando', help='Comandos disponíveis')
    
    # TODO: Adicionar subcomando 'blog'
    # parser_blog = subparsers.add_parser('blog', help='Gerar conteúdo para blog')
    # parser_blog.add_argument('--tema', required=True, help='Tema do conteúdo')
    
    # TODO: Adicionar subcomando 'sentimentos'
    # parser_sentimentos = subparsers.add_parser('sentimentos', help='Analisar sentimentos')
    # parser_sentimentos.add_argument('--arquivo', required=True, help='Arquivo com reviews')
    
    # TODO: Adicionar subcomando 'resumir'
    # parser_resumir = subparsers.add_parser('resumir', help='Resumir PDF')
    # parser_resumir.add_argument('--pdf', required=True, help='Arquivo PDF')
    # parser_resumir.add_argument('--llm', choices=['groq', 'gemini'], default='groq', help='LLM a usar')
    
    # return parser
    pass


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
    # TODO: Criar parser
    # parser = criar_parser()
    # args = parser.parse_args()
    
    # TODO: Se nenhum comando, mostrar menu
    # if not args.comando:
    #     processar_menu()
    #     return
    
    # TODO: Processar comando específico
    # try:
    #     if args.comando == 'blog':
    #         comando_blog(args.tema)
    #     elif args.comando == 'sentimentos':
    #         comando_sentimentos(args.arquivo)
    #     elif args.comando == 'resumir':
    #         comando_resumir(args.pdf, args.llm)
    # except KeyboardInterrupt:
    #     print("\n\n⚠️ Operação cancelada pelo usuário.")
    #     sys.exit(130)
    # except Exception as e:
    #     logging.error(f"❌ Erro ao executar comando: {e}")
    #     sys.exit(1)
    pass


if __name__ == "__main__":
    main()

