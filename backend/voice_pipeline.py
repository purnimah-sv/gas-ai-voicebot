import requests
from google.cloud import speech
from config import ELEVENLABS_KEY

def speech_to_text(audio_file: str):
    client = speech.SpeechClient()

    with open(audio_file, "rb") as f:
        content = f.read()

    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        language_code="ta-IN",
        enable_automatic_punctuation=True
    )

    response = client.recognize(config=config, audio=audio)

    if not response.results:
        return ""

    return response.results[0].alternatives[0].transcript


def text_to_speech(text: str):
    url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"
    headers = {"xi-api-key": ELEVENLABS_KEY}
    data = {"text": text}

    r = requests.post(url, headers=headers, json=data)

    out = "reply.mp3"
    with open(out, "wb") as f:
        f.write(r.content)

    return out
