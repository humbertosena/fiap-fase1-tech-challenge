
import mlflow
import mlflow.pytorch
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

from src.models.predict_model import ChurnMLP
from src.utils.logging_config import setup_logging
from src.utils.seed_config import set_seeds

# ---------------------------------------------------------------------------
# Configurações e Hiperparâmetros
# ---------------------------------------------------------------------------
logger = setup_logging("train_logger")
set_seeds(42)

BATCH_SIZE = 32
LEARNING_RATE = 0.001
EPOCHS = 100
PATIENCE = 10  # Para Early Stopping
MODEL_PATH = "models/model.pth"

# ---------------------------------------------------------------------------
# Classe Early Stopping
# ---------------------------------------------------------------------------
class EarlyStopping:
    """
    Interrompe o treinamento se a perda de validação não melhorar após um
    número determinado de épocas (patience).
    """
    def __init__(self, patience=7, delta=0, path=MODEL_PATH):
        self.patience = patience
        self.delta = delta
        self.path = path
        self.counter = 0
        self.best_score = None
        self.early_stop = False
        self.val_loss_min = np.inf

    def __call__(self, val_loss, model):
        score = -val_loss

        if self.best_score is None:
            self.best_score = score
            self.save_checkpoint(val_loss, model)
        elif score < self.best_score + self.delta:
            self.counter += 1
            logger.info(f"EarlyStopping counter: {self.counter} out of {self.patience}")
            if self.counter >= self.patience:
                self.early_stop = True
        else:
            self.best_score = score
            self.save_checkpoint(val_loss, model)
            self.counter = 0

    def save_checkpoint(self, val_loss, model):
        """Salva o modelo quando a perda de validação diminui."""
        logger.info(f"Validation loss decreased ({self.val_loss_min:.6f} --> {val_loss:.6f}). Saving model...")
        torch.save(model.state_dict(), self.path)
        self.val_loss_min = val_loss

# ---------------------------------------------------------------------------
# Pipeline de Treinamento
# ---------------------------------------------------------------------------
def train():
    # 1. Carregar dados processados
    logger.info("Carregando dados processados para treinamento...")
    train_df = pd.read_csv("data/processed/train_processed.csv")
    test_df = pd.read_csv("data/processed/test_processed.csv")

    X_train = train_df.drop(columns=["Churn"]).values
    y_train = train_df["Churn"].values.reshape(-1, 1)

    X_test = test_df.drop(columns=["Churn"]).values
    y_test = test_df["Churn"].values.reshape(-1, 1)

    # 2. Criar DataLoaders
    train_tensor = TensorDataset(torch.tensor(X_train, dtype=torch.float32), torch.tensor(y_train, dtype=torch.float32))
    test_tensor = TensorDataset(torch.tensor(X_test, dtype=torch.float32), torch.tensor(y_test, dtype=torch.float32))

    train_loader = DataLoader(train_tensor, batch_size=BATCH_SIZE, shuffle=True)
    test_loader = DataLoader(test_tensor, batch_size=BATCH_SIZE, shuffle=False)

    # 3. Inicializar Modelo, Loss e Otimizador
    input_dim = X_train.shape[1]
    model = ChurnMLP(input_dim=input_dim)
    criterion = nn.BCELoss()
    optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)

    early_stopping = EarlyStopping(patience=PATIENCE, path=MODEL_PATH)

    # 4. Loop de Treinamento com MLflow
    mlflow.set_experiment("Telco_Churn_MLP")

    with mlflow.start_run(run_name="MLP_PyTorch_Final"):
        mlflow.log_param("batch_size", BATCH_SIZE)
        mlflow.log_param("learning_rate", LEARNING_RATE)
        mlflow.log_param("max_epochs", EPOCHS)
        mlflow.log_param("patience", PATIENCE)

        logger.info("Iniciando loop de treinamento...")
        for epoch in range(EPOCHS):
            # Treino
            model.train()
            train_losses = []
            for batch_x, batch_y in train_loader:
                optimizer.zero_grad()
                outputs = model(batch_x)
                loss = criterion(outputs, batch_y)
                loss.backward()
                optimizer.step()
                train_losses.append(loss.item())

            avg_train_loss = np.mean(train_losses)

            # Validação
            model.eval()
            val_losses = []
            with torch.no_grad():
                for val_x, val_y in test_loader:
                    val_outputs = model(val_x)
                    val_loss = criterion(val_outputs, val_y)
                    val_losses.append(val_loss.item())

            avg_val_loss = np.mean(val_losses)

            # Logs por época
            mlflow.log_metric("train_loss", avg_train_loss, step=epoch)
            mlflow.log_metric("val_loss", avg_val_loss, step=epoch)

            if epoch % 5 == 0:
                logger.info(f"Epoch {epoch}: Train Loss {avg_train_loss:.4f} | Val Loss {avg_val_loss:.4f}")

            # Check Early Stopping
            early_stopping(avg_val_loss, model)
            if early_stopping.early_stop:
                logger.info(f"Early stopping at epoch {epoch}")
                break

        # 5. Avaliação Final
        logger.info("Treinamento finalizado. Avaliando métricas finais...")
        model.load_state_dict(torch.load(MODEL_PATH))
        model.eval()

        all_preds = []
        all_targets = []
        with torch.no_grad():
            for x, y in test_loader:
                preds = model(x)
                all_preds.extend(preds.numpy())
                all_targets.extend(y.numpy())

        all_preds = np.array(all_preds)
        all_targets = np.array(all_targets)

        # Calcular métricas simples para log (F1, AUC-ROC seriam melhores mas requerem sklearn)
        from sklearn.metrics import f1_score, roc_auc_score
        final_f1 = f1_score(all_targets, (all_preds >= 0.5).astype(int))
        final_auc = roc_auc_score(all_targets, all_preds)

        mlflow.log_metric("final_f1_score", final_f1)
        mlflow.log_metric("final_auc_roc", final_auc)

        logger.info(f"Métricas Finais -> F1-Score: {final_f1:.4f} | AUC-ROC: {final_auc:.4f}")

        # Salvar o modelo no MLflow
        mlflow.pytorch.log_model(model, "model")

if __name__ == "__main__":
    train()
