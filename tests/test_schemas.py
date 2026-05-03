import pandas as pd
import pytest
from pandera.errors import SchemaError

from src.schemas.churn_schema import processed_churn_schema, raw_churn_schema


def test_raw_churn_schema_valid(valid_payload):
    """Testa se o schema Pandera valida corretamente dados íntegros."""
    df = pd.DataFrame([valid_payload])
    try:
        raw_churn_schema.validate(df)
    except SchemaError as e:
        pytest.fail(f"Pandera falhou ao validar dados válidos: {e}")

def test_raw_churn_schema_invalid():
    """Testa se o Pandera rejeita dados fora do range esperado."""
    invalid_data = {
        "gender": "Female",
        "SeniorCitizen": 3, # Inválido (deve ser 0 ou 1)
        "MonthlyCharges": -10.0 # Inválido (deve ser >= 0)
    }
    df = pd.DataFrame([invalid_data])
    with pytest.raises(SchemaError):
        raw_churn_schema.validate(df)

def test_processed_churn_schema_minimal():
    """Testa o schema de saída (processed) com as colunas obrigatórias."""
    data = {
        "tenure": 1.0,
        "MonthlyCharges": 20.0,
        "TotalCharges": 20.0,
        "Charges_per_Tenure": 20.0
    }
    df = pd.DataFrame([data])
    validated_df = processed_churn_schema.validate(df)
    assert "Charges_per_Tenure" in validated_df.columns
