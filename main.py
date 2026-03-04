from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AI Voice Detector API",
    description="API for detecting AI-generated voices",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Welcome to AI Voice Detector API", "status": "running"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


@app.post("/detect")
async def detect_voice(file: UploadFile = File(...)):
    """
    Endpoint to detect if an audio file contains AI-generated voice.
    """
    # Validate file type
    if not file.content_type or not file.content_type.startswith("audio/"):
        raise HTTPException(status_code=400, detail="File must be an audio file")
    
    # Read the file content
    content = await file.read()
    
    # TODO: Implement actual AI voice detection logic here
    # For now, return a placeholder response
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size_bytes": len(content),
        "result": {
            "is_ai_generated": False,
            "confidence": 0.0,
            "message": "Detection model not yet implemented"
        }
    }
