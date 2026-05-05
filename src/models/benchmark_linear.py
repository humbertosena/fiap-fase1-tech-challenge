import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, roc_auc_score, recall_score, precision_score
from src.utils.financial import optimize_financial_threshold
from src.utils.logging_config import setup_logging
from src.utils.seed_config import set_seeds

# ---------------------------------------------------------------------------
# Configurações
# ---------------------------------------------------------------------------
logger = setup_logging("benchmark_linear")
set_seeds(42)

# ---------------------------------------------------------------------------
# Pipeline de Benchmark (Linear)
# ---------------------------------------------------------------------------
def run_benchmark():
    """
    Treina e avalia uma Regressão Logística como baseline linear.
    Registra os resultados no MLflow da RAIZ para comparação tríade.
    """
    logger.info("Carregando dados processados para benchmark linear...")
    train_df = pd.read_csv("data/processed/train_processed.csv")
    test_df = pd.read_csv("data/processed/test_processed.csv")

    X_train = train_df.drop(columns=["Churn"])
    y_train = train_df["Churn"]
    
    X_test = test_df.drop(columns=["Churn"])
    y_test = test_df["Churn"]

    # 1. Configurar experimento unificado no MLflow
    mlflow.set_experiment("churn-prediction")

    with mlflow.start_run(run_name="LogisticRegression_v1"):
        mlflow.set_tag("mlflow.runType", "TRAINING")
        # 2. Inicializar e treinar o modelo
        logger.info("Treinando Regressão Logística (class_weight='balanced')...")
        model = LogisticRegression(class_weight='balanced', random_state=42, max_iter=1000)
        model.fit(X_train, y_train)

        # 3. Predições
        y_pred = model.predict(X_test)
        y_proba = model.predict_proba(X_test)[:, 1]

        # 4. Cálculo de Métricas
        opt_threshold, min_loss = optimize_financial_threshold(y_test, y_proba)
        metrics = {
            "test_f1_score": f1_score(y_test, y_pred),
            "test_precision": precision_score(y_test, y_pred),
            "test_recall": recall_score(y_test, y_pred),
            "test_auc_roc": roc_auc_score(y_test, y_proba),
            "optimal_threshold": opt_threshold,
            "min_financial_loss": min_loss,
        }

        # 5. Registro no MLflow (vocabulário canônico)
        mlflow.log_params({
            "model_type": "LogisticRegression",
            "class_weight": "balanced",
            "max_iter": 1000,
            "solver": "lbfgs",
            "random_state": 42,
            "data_split": "train_test_80_20_stratified",
            "cost_fn": 500,
            "cost_fp": 50,
        })
        mlflow.log_metrics(metrics)

        # Log do modelo como artefato
        mlflow.sklearn.log_model(model, "model")

        logger.info("─" * 40)
        logger.info("BENCHMARK LINEAR CONCLUÍDO")
        for k, v in metrics.items():
            logger.info(f"  {k}: {v:.4f}")
        logger.info("─" * 40)

if __name__ == "__main__":
    run_benchmark()
