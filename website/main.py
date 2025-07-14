from fastapi import FastAPI
import pickle
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
import pandas as pd
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
current_dir = Path(__file__).parent

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to ["http://localhost:5500"] etc.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model and preprocessor
model = None
preprocessor = None

try:
    model_path = current_dir/ "crop_yield_model.pkl"
    preprocessor_path =current_dir / "crop_yield_preprocessor.pkl"
    
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
    with open(preprocessor_path, 'rb') as preprocessor_file:
        preprocessor = pickle.load(preprocessor_file)
    print("Model and preprocessor loaded successfully!")
except Exception as e:
    print(f"Error loading model or preprocessor: {str(e)}")

# Input data model
class YieldPredictionInput(BaseModel):
    Area: str
    Item: str
    Year: int
    average_rain_fall_mm_per_year: float
    pesticides_tonnes: float
    avg_temp: float

@app.get("/")
async def read_root():
    # Read the HTML file directly from the same directory
    with open(current_dir / "index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    # return HTMLResponse(content=html_content)
    if model is None or preprocessor is None:
        return JSONResponse(
            status_code=500,
            content={"error": "Model or preprocessor not loaded."}
        )
    return HTMLResponse(content=html_content)

@app.post("/predict")
async def predict_crop_yield(data: YieldPredictionInput):
    if model is None or preprocessor is None:
        return JSONResponse(
            status_code=500,
            content={"error": "Model or preprocessor not loaded."}
        )
    
    try:
        input_data = {
            'Area': [data.Area],
            'Item': [data.Item],
            'Year': [data.Year],
            'average_rain_fall_mm_per_year': [data.average_rain_fall_mm_per_year],
            'pesticides_tonnes': [data.pesticides_tonnes],
            'avg_temp': [data.avg_temp]
        }
        input_df = pd.DataFrame(input_data)
        
        processed_data = preprocessor.transform(input_df)
        prediction = model.predict(processed_data)
        
        return JSONResponse({
            "hg_ha_yield": float(prediction[0]),
            "status": "success"
        })
        
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "error": str(e),
                "input": input_data
            }

        )
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000 ,reload=True)