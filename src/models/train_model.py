import torch
import torch.nn as nn
import torch.optim as optim
import mlflow
import mlflow.pytorch
import os
import sys

# Adiciona o diretório raiz ao path para permitir imports modulares
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.models.dataset import get_dataloader
from src.models.network import ChurnMLP

# Configuração do MLflow Backend Store
mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("Churn_Prediction_MLP")

def train_model():
    """
    Executa o pipeline de treinamento da MLP com Early Stopping e MLflow.
    """
    # Hiperparâmetros base
    params = {
        "lr": 0.001,
        "epochs": 100,
        "batch_size": 64,
        "hidden_units": [16, 8],
        "dropout": 0.2,
        "patience": 5
    }
    
    # Preparação de Dados
    train_loader = get_dataloader("data/processed/train_processed.csv", batch_size=params["batch_size"])
    val_loader = get_dataloader("data/processed/test_processed.csv", batch_size=params["batch_size"], shuffle=False)
    
    # Inicialização do Modelo, Perda e Otimizador
    model = ChurnMLP(input_dim=31)
    criterion = nn.BCEWithLogitsLoss()
    optimizer = optim.Adam(model.parameters(), lr=params["lr"])
    
    best_val_loss = float('inf')
    epochs_no_improve = 0
    
    print(f"Iniciando treinamento do experimento: Churn_Prediction_MLP")
    
    with mlflow.start_run(run_name="MLP_Base_Training") as run:
        # Log de Hiperparâmetros
        mlflow.log_params(params)
        
        for epoch in range(params["epochs"]):
            # Fase de Treino
            model.train()
            train_loss = 0.0
            for X_batch, y_batch in train_loader:
                optimizer.zero_grad()
                outputs = model(X_batch)
                loss = criterion(outputs, y_batch)
                loss.backward()
                optimizer.step()
                train_loss += loss.item()
            
            avg_train_loss = train_loss / len(train_loader)
            
            # Fase de Validação
            model.eval()
            val_loss = 0.0
            with torch.no_grad():
                for X_batch, y_batch in val_loader:
                    outputs = model(X_batch)
                    loss = criterion(outputs, y_batch)
                    val_loss += loss.item()
            
            avg_val_loss = val_loss / len(val_loader)
            
            # Log de Métricas por Época
            mlflow.log_metric("train_loss", avg_train_loss, step=epoch)
            mlflow.log_metric("val_loss", avg_val_loss, step=epoch)
            
            if (epoch + 1) % 5 == 0 or epoch == 0:
                print(f"Época [{epoch+1}/{params['epochs']}] - Train Loss: {avg_train_loss:.4f} - Val Loss: {avg_val_loss:.4f}")
            
            # Lógica de Early Stopping
            if avg_val_loss < best_val_loss:
                best_val_loss = avg_val_loss
                epochs_no_improve = 0
                # Salvar o melhor estado do modelo
                torch.save(model.state_dict(), "models/best_mlp_model.pth")
            else:
                epochs_no_improve += 1
                if epochs_no_improve >= params["patience"]:
                    print(f"Early stopping ativado na época {epoch+1}")
                    break
        
        # Log Final do Modelo e Artefatos
        mlflow.pytorch.log_model(model, "churn_mlp_model")
        if os.path.exists("models/best_mlp_model.pth"):
            mlflow.log_artifact("models/best_mlp_model.pth")
            print("Melhor modelo registrado no MLflow.")

if __name__ == "__main__":
    train_model()
