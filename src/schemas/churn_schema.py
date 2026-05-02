
import pandera as pa
from pydantic import BaseModel, Field

# ---------------------------------------------------------------------------
# Pydantic Schemas (API Validation)
# ---------------------------------------------------------------------------

class ChurnRequest(BaseModel):
    """
    Schema para validação do payload de entrada da API (FastAPI/Pydantic).
    Representa os dados brutos conforme chegam do cliente.
    """
    gender: str = Field(..., description="Gênero do cliente")
    SeniorCitizen: int = Field(..., ge=0, le=1)
    Partner: str
    Dependents: str
    tenure: int = Field(..., ge=0)
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float = Field(..., ge=0)
    TotalCharges: str = Field(..., description="Valor total em string, pode conter espaços vazios")

    class Config:
        json_schema_extra = {
            "example": {
                "gender": "Female",
                "SeniorCitizen": 0,
                "Partner": "Yes",
                "Dependents": "No",
                "tenure": 1,
                "PhoneService": "No",
                "MultipleLines": "No phone service",
                "InternetService": "DSL",
                "OnlineSecurity": "No",
                "OnlineBackup": "Yes",
                "DeviceProtection": "No",
                "TechSupport": "No",
                "StreamingTV": "No",
                "StreamingMovies": "No",
                "Contract": "Month-to-month",
                "PaperlessBilling": "Yes",
                "PaymentMethod": "Electronic check",
                "MonthlyCharges": 29.85,
                "TotalCharges": "29.85"
            }
        }

# ---------------------------------------------------------------------------
# Pandera Schemas (Data Pipeline Validation)
# ---------------------------------------------------------------------------

# Esquema para os dados brutos (Raw Data)
raw_churn_schema = pa.DataFrameSchema(
    columns={
        "gender": pa.Column(str),
        "SeniorCitizen": pa.Column(int, pa.Check.isin([0, 1])),
        "Partner": pa.Column(str),
        "Dependents": pa.Column(str),
        "tenure": pa.Column(int, pa.Check.greater_than_or_equal_to(0)),
        "PhoneService": pa.Column(str),
        "MultipleLines": pa.Column(str),
        "InternetService": pa.Column(str),
        "OnlineSecurity": pa.Column(str),
        "OnlineBackup": pa.Column(str),
        "DeviceProtection": pa.Column(str),
        "TechSupport": pa.Column(str),
        "StreamingTV": pa.Column(str),
        "StreamingMovies": pa.Column(str),
        "Contract": pa.Column(str),
        "PaperlessBilling": pa.Column(str),
        "PaymentMethod": pa.Column(str),
        "MonthlyCharges": pa.Column(float, pa.Check.greater_than_or_equal_to(0)),
        "TotalCharges": pa.Column(str), # Validado como string antes da conversão
    },
    coerce=True,
    strict=False, # Permite colunas extras como customerID se existirem
)

# Esquema para os dados após Feature Engineering
processed_churn_schema = pa.DataFrameSchema(
    columns={
        "tenure": pa.Column(float),
        "MonthlyCharges": pa.Column(float),
        "TotalCharges": pa.Column(float),
        "Charges_per_Tenure": pa.Column(float),
        # Churn é opcional aqui pois o mesmo schema pode ser usado na inferência (sem label)
        "Churn": pa.Column(int, pa.Check.isin([0, 1]), nullable=True, required=False),
    },
    coerce=True,
    strict=False, # Permite as colunas One-Hot Encoded
)
