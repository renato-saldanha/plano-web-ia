#!/usr/bin/env python3
"""
Exercício 3: RAG Avançado

Melhore sistema RAG com otimizações e features extras.

Tarefas:
1. Implementar diferentes tipos de chains
2. Adicionar filtros para melhorar busca
3. Comparar performance de diferentes configurações
"""

import os
import random
import time
from dotenv import load_dotenv  # type: ignore

# TODO: Importar bibliotecas necessárias
# Dica: Você precisará de:
# - TextLoader (de langchain_community.document_loaders)
# - RecursiveCharacterTextSplitter (de langchain_text_splitters)
# - BM25Retriever (de langchain_community.retrievers)
# - StrOutputParser (de langchain_core.output_parsers)
# - RunnablePassthrough (de langchain_core.runnables)
# - ChatGroq (de langchain_groq)
# - ChatPromptTemplate (de langchain_core.prompts)

from langchain_community.document_loaders import TextLoader
from langchain_core.tools import retriever
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.retrievers import BM25Retriever
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from concurrent.futures import ThreadPoolExecutor

load_dotenv()
# Define llm
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
)

# Define os templates MAP e REDUCE
map_template = ChatPromptTemplate.from_messages([
    ("system", "Resuma o seguinte trecho de documento. Mantenha apenas informações relevantes para responder perguntas."),
    ("human", "Trecho:\n{chunk}\n\nResumo:")
])

reduce_template = ChatPromptTemplate.from_messages([
    ("system", "Combine os seguintes resumos em uma resposta completa e coerente à pergunta. Se não houver informação suficiente, diga 'Não sei responder'."),
    ("human",
     "Resumos:\n{summaries}\n\nPergunta: {input}\n\nResposta completa:")
])

map_chain = (
    map_template
    | llm
    | StrOutputParser()
)

reduce_chain = (
    reduce_template
    | llm
    | StrOutputParser()
)


def map_reduce_parallel(retriever, question, max_workers=5):
    """
    Processa chunks em paralelo usando map-reduce

    Args:
        retriever: Retriever configurado
        question: Pergunta a ser respondida
        max_workers: Número de threads paralelas

    Returns:
        Resposta final combinada
    """
    
    # Busca chunks relevantes
    chunks = retriever.invoke(question)

    print(f"Processando {len(chunks)} chunks em paralelo...")

    # Processa chunks em paralelo (MAP)
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        summaries = list(executor.map(
            lambda chunk: map_chain.invoke({"chunk": chunk.page_content}),
            chunks
        ))

    # Combina resumos (REDUCE)
    combined = "\n\n".join(summaries)
    final_answer = reduce_chain.invoke({
        "summaries": combined,
        "input": question,
    })

    return final_answer


def comparar_chain_types():
    """
    TODO: Comparar diferentes tipos de chains RAG

    Compare:
    - "stuff" (mais simples, mais rápido)
    - "map_reduce" (funciona com muitos chunks)
    """
    print("=" * 60)
    print("Exercício 3: RAG Avançado")
    print("=" * 60)

    documentos_temp = [
        """
            O Python é a linguagem dominante para inteligência artificial (IA) devido à sua simplicidade e vasta coleção de bibliotecas especializadas. 
            Frameworks populares como o TensorFlow e o PyTorch facilitam a criação de modelos complexos de aprendizado de máquina e redes neurais. 
            A sintaxe intuitiva do Python permite que os desenvolvedores se concentrem na lógica da IA em vez de detalhes de implementação de baixo nível. 
            Bibliotecas adicionais como NumPy e Pandas oferecem ferramentas eficientes para manipulação e análise de dados, 
            etapas cruciais no desenvolvimento de soluções de IA. 
            Essa combinação de facilidade de uso e ecossistema robusto faz do Python a escolha ideal para o desenvolvimento de sistemas inteligentes.
        """,
        """
            A engenharia de software com IA representa a evolução natural do desenvolvimento de sistemas, 
            integrando técnicas de inteligência artificial para automatizar tarefas, melhorar a tomada de decisão e aumentar a eficiência no ciclo de vida do software. 
            Em vez de depender apenas de abordagens tradicionais, esse campo combina princípios de engenharia com modelos modernos como LLMs, 
            machine learning e agentes autônomos.
            Um dos pilares dessa área é a automação inteligente. Ferramentas de IA já conseguem gerar código, revisar pull requests, 
            detectar vulnerabilidades e até propor arquiteturas iniciais. Isso não substitui desenvolvedores, mas amplia sua capacidade produtiva,
            reduz erros e acelera entregas. 
            O profissional passa a assumir um papel mais estratégico e menos operacional.
        """,
        """
            A arquitetura de software é a disciplina responsável por definir a estrutura fundamental de um sistema, incluindo seus componentes principais,
            como eles se comunicam e quais decisões técnicas guiam a sua construção. 
            Ela funciona como o “plano diretor” que orienta o desenvolvimento, garantindo que o software seja escalável, seguro e mantenível ao longo do tempo.
            Um dos pilares da arquitetura é a separação de responsabilidades, que organiza o sistema em camadas, módulos ou serviços independentes. 
            Isso facilita manutenção, testes e evolução, evitando que mudanças pequenas afetem todo o sistema. 
            Padrões como MVC, hexagonal e DDD nascem justamente para estruturar essas responsabilidades de forma clara.
        """
    ]

    # Inicia a Lista de Chunks
    chunk_list = []
    arquivos_temp = []

    # Carrega documentos
    for i, documento in enumerate(documentos_temp, 1):
        # Cria arquivo e adiciona na lsita
        arquivo = f"documento{i}.txt"
        arquivos_temp.append(arquivo)

        # Grava arquivo temporário
        with open(arquivo, "w", encoding="utf-8") as f:
            f.write(documento)

        loader = TextLoader(arquivo, encoding="utf-8")
        documento_carregado = loader.load()

        size = random.randint(40, 200)
        overlap = random.randint(15, 90) 

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=size,
            chunk_overlap=overlap,
        )

        chunk_list.append(text_splitter.split_documents(documento_carregado))

    # for resumido pela facilidade de leitura criando uma lista de retrievers
    list_retriever_docs = [BM25Retriever.from_documents(chunk) for chunk in chunk_list]

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    # TODO: Criar chain tipo "stuff" usando LCEL puro
    # Dica:
    # 1. Criar função format_docs(docs) para formatar documentos
    # 2. Criar ChatPromptTemplate com {context} e {input}
    # 3. Criar chain usando LCEL puro com operador |
    # TODO: Medir tempo de resposta usando time.time() antes e depois

    # TODO: Criar variações da chain (diferentes tamanhos de chunks, diferentes k)
    # Dica: Experimente diferentes configurações do retriever e compare resultados
    # TODO: Medir tempo de resposta para cada variação

    # Template para STUFF
    stuff_template = ChatPromptTemplate.from_messages([
        ("system", "Responda a pergunta com base no contexto. Não invente informações. Se não souber diga: Não sei responder."),
        ("human", "Contexto:\n{contexto}\n\nPergunta: {input}\n\nResposta:\n")
    ])

    # Cria chains STUFF
    stuff_chains = []
    for retriever_doc in list_retriever_docs:
        retriever_doc.k = random.randint(3, 6) 
        stuff_chains.append(
            {
                "contexto": retriever_doc | format_docs,
                "input": RunnablePassthrough(),
            }
            | stuff_template
            | llm
            | StrOutputParser()
        )

    # Lista de perguntas
    answers_list = [
        "Quais bibliotecas são usadas para desenvolver com IA?",
        "O que a IA melhora na Engenharia de Softwares?",
        "Quais os pontos chaves da Arquitetura de Softwares?"
    ]
    
    # Compara STUFF vs MAP-REDUCE
    resultados = []    

    
    for i, (stuff_chain, retriever_doc) in enumerate(zip(stuff_chains, list_retriever_docs)):
        question = answers_list[i]
        
        print(f"\n{'='*60}")
        print(f"Pergunta {i+1}: {question}")
        print(f"{'='*60}")
        
        # Teste STUFF
        tempo_inicio = time.time()
        # Tenta a call da chain
        try:
            resposta_stuff = stuff_chain.invoke(question)
        except Exception as e:
            print(f"Erro em STUFF: {e}")
            resposta_stuff = "Erro ao processar"

        tempo_stuff = time.time() - tempo_inicio
        
        # Teste MAP-REDUCE
        tempo_inicio = time.time()
        resposta_map_reduce = map_reduce_parallel(retriever_doc, question)
        tempo_map_reduce = time.time() - tempo_inicio
        
        resultados.append({
            "pergunta": question,
            "stuff": {
                "resposta": resposta_stuff,
                "tempo": tempo_stuff
            },
            "map_reduce": {
                "resposta": resposta_map_reduce,
                "tempo": tempo_map_reduce
            }
        })
        
        print(f"\nSTUFF:")
        print(f"  Tempo: {tempo_stuff:.2f}s")
        print(f"  Resposta: {resposta_stuff[:150]}...")
        
        print(f"\nMAP-REDUCE:")
        print(f"  Tempo: {tempo_map_reduce:.2f}s")
        print(f"  Resposta: {resposta_map_reduce[:150]}...")
    
    # Limpa arquivos temporários
    for arquivo in arquivos_temp:
        if os.path.exists(arquivo):
            os.remove(arquivo)
    
    # Resumo final
    print("\n" + "=" * 60)
    print("RESUMO DA COMPARAÇÃO")
    print("=" * 60)
    
    tempo_total_stuff = sum(r["stuff"]["tempo"] for r in resultados)
    tempo_total_map_reduce = sum(r["map_reduce"]["tempo"] for r in resultados)
    
    print(f"\nTempo total STUFF: {tempo_total_stuff:.2f}s")
    print(f"Tempo total MAP-REDUCE: {tempo_total_map_reduce:.2f}s")
    print(f"Diferença: {abs(tempo_total_map_reduce - tempo_total_stuff):.2f}s")
    
    print("\n✅ Exercício 3 completo!")
    print("\n💡 Análise:")
    print("   - STUFF é mais rápido para poucos chunks")
    print("   - MAP-REDUCE processa melhor muitos chunks")
    print("   - Use STUFF quando contexto cabe no limite do LLM")
    print("   - Use MAP-REDUCE quando precisa processar muitos documentos")

if __name__ == "__main__":
    comparar_chain_types()
