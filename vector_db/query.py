import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

client = chromadb.PersistentClient(path="../backend/chroma_db")
col = client.get_collection("gasbot")

q = input("Query: ")
emb = model.encode([q])[0]

res = col.query(query_embeddings=[emb], n_results=3)
print(res["documents"])
