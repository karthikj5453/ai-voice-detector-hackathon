from fastapi.testclient import TestClient
from main import app
import io
import numpy as np
import soundfile as sf

client = TestClient(app)

def create_mock_audio():
    buf = io.BytesIO()
    samplerate = 16000
    data = np.random.uniform(-1, 1, samplerate)
    sf.write(buf, data, samplerate, format='WAV')
    buf.seek(0)
    return buf

def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_detect_success():
    audio_file = create_mock_audio()
    files = {'file': ('test.wav', audio_file, 'audio/wav')}
    response = client.post("/detect", files=files)
    assert response.status_code == 200
