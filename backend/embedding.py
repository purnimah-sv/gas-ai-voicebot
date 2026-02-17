import json
import chromadb
from sentence_transformers import SentenceTransformer
from config import MODEL_NAME, VECTOR_DB_PATH

model = SentenceTransformer(MODEL_NAME)
client = chromadb.PersistentClient(path=VECTOR_DB_PATH)
collection = client.get_or_create_collection("gasbot")

data = json.load(open("../data/corpus.json"))

for i, doc in enumerate(data):
    emb = model.encode([doc])[0]
    collection.add(ids=[str(i)], documents=[doc], embeddings=[emb])

print("Embeddings stored")
