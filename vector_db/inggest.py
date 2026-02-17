import json
import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

client = chromadb.PersistentClient(path="../backend/chroma_db")
col = client.get_or_create_collection("gasbot")

data = json.load(open("../data/corpus.json"))

for i, doc in enumerate(data):
    emb = model.encode([doc])[0]
    col.add(ids=[str(i)], documents=[doc], embeddings=[emb])

print("Vector DB ready")