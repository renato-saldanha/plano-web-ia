from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from sympy.matrices.expressions.determinant import per

load_dotenv();

# Define o Embedding
embedding = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True},
)

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

def main():
    # Define a lista de documentos
    docs = [
        Document(page_content="O carro vermelho é muito rápido",
                 metadata={"id": 1}),
        Document(page_content="O automóvel azul é econômico",
                 metadata={"id": 2}),
        Document(page_content="O veículo verde é espaçoso",
                 metadata={"id": 3}),
        Document(page_content="O computador está quebrado",
                 metadata={"id": 4}),
        Document(page_content="A bicicleta é um meio de transporte",
                 metadata={"id": 5})
    ]

    # Define Vetor  
    vectorstore = FAISS.from_documents(
        documents = docs,
        embedding = embedding,
    )

    # Salva Vetor
    vectorstore.save_local(".faiss_index")

    # Define Retriever com top 3
    retriever = vectorstore.as_retriever(
        search_kwargs = {"k": 3}
    )
 
    print("-" * 60)  

    human_template ="""Responda baseado apenas no contexto:

    Contexto:
    {context}

    Pergunta: {question}

    Resposta:"""

    system_template = "Contexto:{context}\n\nPergunta:{question}\n\nResposta:\n"

    # Define template com as variáveis acima
    template = ChatPromptTemplate([
        ("system", system_template),
        ("human", human_template),
    ])

    def format_docs(docs):
        return "\n\n".join([doc.page_content for doc in docs])

    # Define Chain usando LCEL puro         
    rag_chain = (
        {
            "context" : retriever | format_docs,
            "question": RunnablePassthrough(),
        }
        | template
        | llm
        | StrOutputParser()
    )

    # Define perguntas
    answers = [
        "Qual veículo é mais rápido?",
        "Fale sobre automóveis econômicos",
        "Existe algum transporte espoaçoso?",
    ]

    # Loop que retorna a estrutura resposta de cada pergunta
    for answer in answers:
        response = rag_chain.invoke(answer)
        print("-" * 60)
        print(f"Pergunta: {answer}")
        print("-" * 60)
        print(f"Resposta: {response}")

    # Define a lista de textos
    textos = [doc.page_content for doc in docs]

    embs = [embedding.embed_query(texto) for texto in textos]
    
    # Loop que imprime a similaridade
    for i, emb in enumerate(embs, 1):
        similarity = cosine_similarity([embs[0]], [emb])[0][0]
        print(f"Similaridade: '{textos[0]}' vs '{textos[i]}: {similarity:.4f}'")

if __name__ == "__main__":
    main()
