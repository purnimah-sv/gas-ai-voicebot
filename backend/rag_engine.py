import chromadb
from sentence_transformers import SentenceTransformer
from config import MODEL_NAME, VECTOR_DB_PATH

model = SentenceTransformer(MODEL_NAME)
client = chromadb.PersistentClient(path=VECTOR_DB_PATH)
collection = client.get_or_create_collection("gasbot")

def retrieve(query: str):
    emb = model.encode([query])[0]
    results = collection.query(query_embeddings=[emb], n_results=3)
    return " ".join(results["documents"][0])

def answer(query: str):
    context = retrieve(query)
    return f"According to records: {context}"
