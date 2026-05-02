import os

import joblib
import pandas as pd
import torch
import torch.nn as nn

from src.features.build_features import engineer_features
from src.schemas.churn_schema import ChurnRequest

# ---------------------------------------------------------------------------
# Arquitetura da Rede Neural (MLP)
# ---------------------------------------------------------------------------

class ChurnMLP(nn.Module):
    """
    Definição da arquitetura da MLP para predição de Churn.
    Baseada nos requisitos da Etapa 2.
    """
    def __init__(self, input_dim: int):
        super(ChurnMLP, self).__init__()
        # Arquitetura sugerida: Input -> 16 -> 8 -> 1 (Sigmoid)
        self.layer1 = nn.Linear(input_dim, 16)
        self.layer2 = nn.Linear(16, 8)
        self.output = nn.Linear(8, 1)
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.relu(self.layer1(x))
        x = self.relu(self.layer2(x))
        x = self.sigmoid(self.output(x))
        return x

# ---------------------------------------------------------------------------
# Classe Wrapper de Inferência
# ---------------------------------------------------------------------------

class ChurnModelWrapper:
    """
    Wrapper para carregar artefatos e realizar predições pontuais.
    """
    def __init__(self, model_path: str = "models/model.pth", preprocessor_path: str = "models/preprocessor.pkl"):
        self.model_path = model_path
        self.preprocessor_path = preprocessor_path
        self.model = None
        self.preprocessor = None
        self.input_dim = None

    def load(self):
        """Carrega o preprocessor e o modelo PyTorch."""
        if not os.path.exists(self.preprocessor_path):
            raise FileNotFoundError(f"Preprocessor não encontrado em: {self.preprocessor_path}")

        self.preprocessor = joblib.load(self.preprocessor_path)

        # Identificar dimensão de entrada a partir do preprocessor
        # (Isso assume que o preprocessor já foi 'fitted')
        self.input_dim = self.preprocessor.get_feature_names_out().shape[0]

        # Inicializar e carregar modelo
        self.model = ChurnMLP(input_dim=self.input_dim)
        if os.path.exists(self.model_path):
            self.model.load_state_dict(torch.load(self.model_path, map_location=torch.device('cpu')))
            self.model.eval()
        else:
            # Caso o modelo .pth ainda não exista (Etapa 2 incompleta),
            # logamos um aviso. Em produção, isso seria um erro crítico.
            print(f"AVISO: Pesos do modelo não encontrados em {self.model_path}. Usando pesos aleatórios.")
            self.model.eval()

    def predict(self, request: ChurnRequest) -> float:
        """
        Realiza o pipeline completo:
        Raw JSON -> DataFrame -> Feature Engineering -> Preprocessing -> MLP -> Probabilidade
        """
        # 1. Converter Pydantic para DataFrame
        df_raw = pd.DataFrame([request.model_dump()])

        # 2. Feature Engineering (inclui validação Pandera)
        df_engineered = engineer_features(df_raw)

        # 3. Preprocessing (Sklearn Pipeline)
        # Nota: preprocessor espera X (features), mas o df_engineered pode conter o alvo se estivesse no treino.
        # Aqui, garantimos que passamos apenas as colunas que o preprocessor conhece.
        X_processed = self.preprocessor.transform(df_engineered)

        # 4. Inferência PyTorch
        X_tensor = torch.tensor(X_processed, dtype=torch.float32)

        with torch.no_grad():
            prob = self.model(X_tensor)

        return float(prob.item())

# Instância global para reuso na API (Singleton pattern)
model_service = ChurnModelWrapper()
