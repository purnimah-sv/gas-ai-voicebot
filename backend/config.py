import os

OPENAI_KEY = os.getenv("OPENAI_KEY", "")
ELEVENLABS_KEY = os.getenv("ELEVENLABS_KEY", "")
GOOGLE_STT_KEY = os.getenv("GOOGLE_STT_KEY", "")

VECTOR_DB_PATH = "./chroma_db"
MODEL_NAME = "paraphrase-multilingual-MiniLM-L12-v2"
