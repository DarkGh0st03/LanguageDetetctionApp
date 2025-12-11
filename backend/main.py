from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import os

app = FastAPI()

# Path where the model volume will be mounted
MODEL_PATH = "/app/models/language_detector_CPU_NB_full_ngrams1-2.joblib"
model = None

class TextRequest(BaseModel):
    text: str

@app.on_event("startup")
def load_model():
    global model
    try:
        # Load the model only once at startup
        model = joblib.load(MODEL_PATH)
        print(f"✅ Model loaded from {MODEL_PATH}")
    except Exception as e:
        print(f"❌ Error loading model: {e}")

@app.post("/predict")
def predict(request: TextRequest):
    if not model:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    try:
        # Perform inference
        prediction = model.predict([request.text])[0]
        return {"language_code": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    return {"status": "ok"}