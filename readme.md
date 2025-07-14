# Crop Yield Prediction System

A machine learning system for predicting crop yields based on environmental factors and agricultural inputs.

## Features
- Predicts crop yields (hg/ha) based on:
  - Area (country)
  - Crop type
  - Year
  - Average rainfall (mm/year)
  - Pesticide usage (tonnes)
  - Average temperature
- FastAPI web interface for easy predictions
- Pre-trained machine learning models

## Installation
1. Create and activate a virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
1. Start the FastAPI server:
```bash
cd website
uvicorn main:app --reload
```

2. Access the web interface at `http://localhost:8000`

3. Make predictions via API:
```bash
POST http://localhost:8000/predict
Content-Type: application/json

{
  "Area": "Albania",
  "Item": "Maize",
  "Year": 2020,
  "average_rain_fall_mm_per_year": 1485.0,
  "pesticides_tonnes": 121.0,
  "avg_temp": 16.37
}
```

## Project Structure
- `CropYeild_prediction.ipynb`: Jupyter notebook for data analysis and model training
- `website/`: FastAPI application serving predictions
  - `main.py`: API endpoints and model loading
  - `index.html`: Web interface
  - `*.pkl`: Serialized model and preprocessor
- `yield_df.csv`: Dataset used for training

## Dependencies
- Python 3.11+
- FastAPI
- scikit-learn
- pandas
- numpy

## License
MIT License