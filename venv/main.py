from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import Optional
import base64

app = FastAPI()

API_KEY = "my_secret_key"

class AudioRequest(BaseModel):
    audio_base64: str
    language: Optional[str] = "en"

@app.post("/detect")
def detect_voice(
    data: AudioRequest,
    authorization: str = Header(None)
):
    # 1. Check API key
    if authorization != f"Bearer {API_KEY}":
        raise HTTPException(status_code=401, detail="Unauthorized")

    # 2. Decode Base64 audio
    try:
        audio_bytes = base64.b64decode(data.audio_base64)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid Base64 audio")

    # 3. TEMPORARY dummy logic (we’ll replace later)
    classification = "Human"
    confidence = 0.55
    explanation = "Baseline check: audio decoded successfully."

    # 4. Return required JSON
    return {
        "classification": classification,
        "confidence": confidence,
        "explanation": explanation,
        "language": data.language
    }
