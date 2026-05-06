import time
import uuid

from fastapi import FastAPI, HTTPException, Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

from src.models.predict_model import model_service
from src.schemas.churn_schema import ChurnRequest
from src.utils.logging_config import setup_logging

# ---------------------------------------------------------------------------
# Configuração de Rate Limiting
# ---------------------------------------------------------------------------
limiter = Limiter(key_func=get_remote_address)

# ---------------------------------------------------------------------------
# Configuração Global
# ---------------------------------------------------------------------------
app = FastAPI(
    title="Churn Prediction API",
    description="API para predição de rotatividade de clientes (Churn) utilizando MLP em PyTorch.",
    version="0.1.0"
)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

logger = setup_logging("api_logger")

# Inicializar o modelo no startup da aplicação
@app.on_event("startup")
def startup_event():
    try:
        logger.info("Carregando modelos e artefatos de inferência...")
        model_service.load()
        logger.info("Modelos carregados com sucesso.")
    except Exception as e:
        logger.error(f"Erro ao carregar modelos: {str(e)}")
        # Em produção, poderíamos impedir o startup se o modelo for essencial
        pass

# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@app.get("/", tags=["General"])
def read_root():
    """Endpoint de boas-vindas."""
    return {
        "status": "online",
        "message": "FIAP Tech Challenge - Churn Prediction API is running."
    }

@app.get("/health", tags=["Monitoring"])
def health_check():
    """Verifica a saúde da API e se o modelo está carregado."""
    model_ready = model_service.model is not None
    return {
        "status": "healthy" if model_ready else "degraded",
        "model_loaded": model_ready,
        "timestamp": time.time()
    }

@app.get("/version", tags=["Monitoring"])
def get_version():
    """Retorna a versão da API para rastreabilidade."""
    return {
        "api_version": "0.1.0",
        "model_type": "PyTorch MLP",
        "framework": "FastAPI"
    }

@app.post("/predict", tags=["ML Inference"])
@limiter.limit("10/minute")
def predict(payload: ChurnRequest, request: Request):
    """
    Recebe dados brutos do cliente e retorna a probabilidade de Churn.
    Rate limit: 10 requisições por minuto por IP.
    """
    start_time = time.time()
    request_id = str(uuid.uuid4())

    if model_service.model is None:
        logger.error(f"[{request_id}] Tentativa de predição sem modelo carregado.")
        raise HTTPException(status_code=503, detail="Modelo não disponível no servidor.")

    try:
        logger.info(f"[{request_id}] Recebendo requisição de predição para cliente.")

        # Realizar a inferência via service
        probability = model_service.predict(payload)

        # Lógica de decisão simples baseada em threshold de 0.5
        prediction = "Yes" if probability >= 0.5 else "No"

        latency = time.time() - start_time
        logger.info(f"[{request_id}] Predição concluída em {latency:.4f}s. Resultado: {prediction} (Prob: {probability:.4f})")

        return {
            "request_id": request_id,
            "churn_probability": round(probability, 4),
            "prediction": prediction,
            "threshold": 0.5,
            "latency_s": round(latency, 4)
        }

    except Exception as e:
        logger.error(f"[{request_id}] Erro durante a inferência: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro interno no processamento do modelo: {str(e)}")
