from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

embedding = HuggingFaceEmbeddings(
    model_name = "all-mpnet-base-v2",
    model_kwargs = {"device": "cpu"},
    encode_kwargs = {"normalize_embeddings": True}
)

textos = [
    "O cachorro late no quintal",
    "O cão está latindo",
    "O gato mia na casa",
    "O computador está ligado",
    "A vaca está na casa",
    "O pato está no quintal",
]

embs = [embedding.embed_query(t) for t in textos]

for i in range(1, len(textos)):
    similarity = cosine_similarity([embs[0]], [embs[i]])[0][0]
    print(f"Similaridade '{textos[0]}' vs '{textos[i]}': {similarity:.4f}")



"""
ll-MiniLM-L6-v2
Similaridade 'O cachorro late no quintal' vs 'O cão está latindo': 0.5428
Similaridade 'O cachorro late no quintal' vs 'O gato mia na casa': 0.5161
Similaridade 'O cachorro late no quintal' vs 'O computador está ligado': 0.4778
Similaridade 'O cachorro late no quintal' vs 'A vaca está na casa': 0.4299
Similaridade 'O cachorro late no quintal' vs 'O pato está no quintal': 0.6952
"""

"""
all-mpnet-base-v2"
Similaridade 'O cachorro late no quintal' vs 'O cão está latindo': 0.5614
Similaridade 'O cachorro late no quintal' vs 'O gato mia na casa': 0.5075
Similaridade 'O cachorro late no quintal' vs 'O computador está ligado': 0.4797
Similaridade 'O cachorro late no quintal' vs 'A vaca está na casa': 0.4574
Similaridade 'O cachorro late no quintal' vs 'O pato está no quintal': 0.6955
"""