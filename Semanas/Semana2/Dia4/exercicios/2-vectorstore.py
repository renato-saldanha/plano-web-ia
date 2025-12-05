from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

"""
all-mpnet-base-v2
"""

embedding = HuggingFaceEmbeddings(
    model_name = "all-MiniLM-L6-v2",
    model_kwargs = {"device": "cpu"},
    encode_kwargs = {"normalize_embeddings": True}
)

def main():
    docs = [
        Document(page_content="O carro vermelho é muito rápido", metadata={"id": 1}),
        Document(page_content="O automóvel azul é econômico", metadata={"id": 2}),
        Document(page_content="O veículo verde é espaçoso", metadata={"id": 3}),
        Document(page_content="O computador está quebrado", metadata={"id": 4}),
        Document(page_content="A bicicleta é um meio de transporte", metadata={"id": 5})
    ]     

    vectorstore = FAISS.from_documents(
        documents = docs,
        embedding = embedding,
    )

    vectorstore.save_local("./faiss_index")

    retriever = vectorstore.as_retriever(
        search_kwargs = { "k": 3 }
    )

    print("\n=== Busca 1: Sinônimo 'veículo' ===")
    responses = retriever.invoke("veículo")
    for doc in responses:
        print(f"- {doc.page_content}")

    print("\n=== Busca 2: Palavra exata 'carro' ===")
    responses = retriever.invoke("carro")
    for doc in responses:
        print(f"- {doc.page_content}")

    print("\n=== Busca 3: Conceito 'transporte rápido' ===")
    responses = retriever.invoke("transporte rápido")
    for doc in responses:
        print(f"- {doc.page_content}")


if __name__ == "__main__":
    main()


"""
all-mpnet-base-v2
=== Busca 1: Sinônimo 'veículo' ===
- O veículo verde é espaçoso
- O carro vermelho é muito rápido
- O computador está quebrado

=== Busca 2: Palavra exata 'carro' ===
- O carro vermelho é muito rápido
- O computador está quebrado
- O veículo verde é espaçoso

=== Busca 3: Conceito 'transporte rápido' ===
- O carro vermelho é muito rápido
- A bicicleta é um meio de transporte
- O veículo verde é espaçoso
"""

"""
all-MiniLM-L6-v2
=== Busca 1: Sinônimo 'veículo' ===
- O veículo verde é espaçoso
- O carro vermelho é muito rápido
- O automóvel azul é econômico

=== Busca 2: Palavra exata 'carro' ===
- O carro vermelho é muito rápido
- O computador está quebrado
- O veículo verde é espaçoso

=== Busca 3: Conceito 'transporte rápido' ===
- A bicicleta é um meio de transporte
- O carro vermelho é muito rápido
- O veículo verde é espaçoso
"""