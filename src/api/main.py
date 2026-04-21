from fastapi import FastAPI
from pydantic import BaseModel
from src.utils.logging_config import logger

app = FastAPI(title="Churn Prediction API")

class PredictionInput(BaseModel):
    # Exemplo de campos para churn (ajuste conforme seu dataset)
    tenure: int
    monthly_charges: float
    total_charges: float

@app.get("/")
def read_root():
    return {"status": "online", "model": "Churn Prediction MLP"}

@app.post("/predict")
def predict(data: PredictionInput):
    logger.info(f"Recebendo requisição de predição: {data}")
    # Aqui entraria a lógica de load_model() e predict()
    return {"churn_probability": 0.42}
