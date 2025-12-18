from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import requests
import os

# --- IMPORT CUSTOM MODULES ---
# Import maps for business logic (Dialect Aggregation)
# Ensure dialect_map.py and language_map.py are in the same directory
try:
    from dialect_map import DIALECT_TO_PARENT
    from language_map import LABEL_TO_NAME
except ImportError:
    print("WARNING: dialect_map or language_map not found. Grouping disabled.")
    DIALECT_TO_PARENT = {}
    LABEL_TO_NAME = {}

app = FastAPI()

# Jinja2 Template Configuration
templates = Jinja2Templates(directory="templates")

# Backend URL Configuration (Service Discovery)
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Renders the empty initial landing page."""
    return templates.TemplateResponse("index.html", {"request": request, "result": None})

@app.post("/detect", response_class=HTMLResponse)
async def detect_language(request: Request, text: str = Form(...)):
    """Handles form submission and post-processing logic."""
    result_display = None
    error_msg = None
    note_msg = None
    
    # Input Validation
    if not text.strip():
        return templates.TemplateResponse("index.html", {
            "request": request, 
            "error": "Please enter some text to analyze.",
            "input_text": ""
        })

    try:
        # 1. Backend Call (Inference Engine)
        response = requests.post(f"{BACKEND_URL}/predict", json={"text": text}, timeout=30)
        
        if response.status_code == 200:
            data = response.json()
            raw_code = data.get("language_code", "Unknown")
            
            # --- BUSINESS LOGIC: Dialect Aggregation ---
            # 2. Check if it's a dialect and find the parent (e.g., 'scn' -> 'ita')
            final_code = DIALECT_TO_PARENT.get(raw_code, raw_code)
            
            # 3. Convert Code -> Readable Name (e.g., 'ita' -> 'Italian')
            final_name = LABEL_TO_NAME.get(final_code, final_code)
            
            # Main result to display to the user
            result_display = final_name
            
            # 4. Generate Note (Transparency)
            # If raw code differs from final code, notify the user
            if raw_code != final_code:
                raw_name = LABEL_TO_NAME.get(raw_code, raw_code)
                note_msg = f"Specific dialect detected: {raw_name} ({raw_code}). Grouped under {final_name}."
                
        else:
            error_msg = f"Backend Error ({response.status_code}): {response.text}"
            
    except Exception as e:
        error_msg = f"Connection Error: {str(e)}"

    # Reload the page with processed data
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "result": result_display, 
        "note": note_msg,
        "error": error_msg,
        "input_text": text
    })