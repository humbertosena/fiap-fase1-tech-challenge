import torch
import pandas as pd
import mlflow
import mlflow.pytorch
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import os
import sys

# Adiciona o diretório raiz ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.models.dataset import get_dataloader
from src.models.network import ChurnMLP

def evaluate():
    mlflow.set_tracking_uri("sqlite:///mlflow.db")
    
    # 1. Carregar Dados de Teste
    test_loader = get_dataloader("data/processed/test_processed.csv", batch_size=1000, shuffle=False)
    X_test, y_test = next(iter(test_loader))
    
    # 2. Carregar Melhor Modelo MLP
    model = ChurnMLP(input_dim=31)
    if os.path.exists("models/best_mlp_model.pth"):
        model.load_state_dict(torch.load("models/best_mlp_model.pth"))
    model.eval()
    
    # 3. Predições MLP
    with torch.no_grad():
        logits = model(X_test)
        probs = torch.sigmoid(logits)
        preds = (probs > 0.5).float()
    
    # 4. Cálculo de Métricas MLP
    y_test_np = y_test.numpy()
    preds_np = preds.numpy()
    probs_np = probs.numpy()
    
    report = classification_report(y_test_np, preds_np, output_dict=True)
    auc_mlp = roc_auc_score(y_test_np, probs_np)
    
    print("--- Performance MLP ---")
    print(f"AUC: {auc_mlp:.4f}")
    print(f"F1-Score (Classe 1): {report['1.0']['f1-score']:.4f}")
    print(f"Recall (Classe 1): {report['1.0']['recall']:.4f}")
    
    # 5. Buscar métricas do Baseline no MLflow
    # Assume-se que o experimento de baseline existe
    try:
        baseline_runs = mlflow.search_runs(experiment_names=["Default", "Baseline_Financial_Optimization"])
        if not baseline_runs.empty:
            best_baseline = baseline_runs.sort_values("metrics.f1_score", ascending=False).iloc[0]
            print("\n--- Comparação com Baseline ---")
            print(f"Baseline F1-Score: {best_baseline.get('metrics.f1_score', 'N/A')}")
    except Exception as e:
        print(f"\nNão foi possível recuperar métricas de baseline via MLflow: {e}")

    # 6. Registrar métricas de avaliação final da MLP no MLflow
    with mlflow.start_run(run_name="MLP_Final_Evaluation"):
        mlflow.log_metric("test_auc", auc_mlp)
        mlflow.log_metric("test_f1", report['1.0']['f1-score'])
        mlflow.log_metric("test_recall", report['1.0']['recall'])
        print("\nAvaliação final registrada no MLflow.")

if __name__ == "__main__":
    evaluate()
