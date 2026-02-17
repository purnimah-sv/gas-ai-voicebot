from fastapi import FastAPI
from exotel_webhook import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def health():
    return {"status": "running"}
