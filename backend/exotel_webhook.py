from fastapi import APIRouter, UploadFile
from voice_pipeline import speech_to_text, text_to_speech
from rag_engine import answer

router = APIRouter()

@router.post("/exotel")
async def exotel_call(file: UploadFile):

    path = f"/tmp/{file.filename}"

    with open(path, "wb") as f:
        f.write(await file.read())

    text = speech_to_text(path)
    reply = answer(text)
    audio = text_to_speech(reply)

    return {"audio_file": audio}
