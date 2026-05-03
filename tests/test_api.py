from fastapi.testclient import TestClient


def test_read_root(client: TestClient):
    """Teste de fumaça para o root."""
    response = client.get("/")
    assert response.status_code == 200
    assert "online" in response.json()["status"]

def test_health_check(client: TestClient):
    """Teste para o endpoint /health."""
    response = client.get("/health")
    assert response.status_code == 200
    assert "status" in response.json()

def test_version(client: TestClient):
    """Teste para o endpoint /version."""
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json()["api_version"] == "0.1.0"

def test_predict_invalid_payload(client: TestClient):
    """Teste para garantir que a API rejeita payloads incompletos."""
    response = client.post("/predict", json={"tenure": 10})
    assert response.status_code == 422 # Unprocessable Entity (Pydantic validation)
