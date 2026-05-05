import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, precision_score, recall_score, roc_auc_score

from src.utils.financial import optimize_financial_threshold
from src.utils.logging_config import setup_logging
from src.utils.seed_config import set_seeds

# ---------------------------------------------------------------------------
# Configurações
# ---------------------------------------------------------------------------
logger = setup_logging("benchmark_tree")
set_seeds(42)

# ---------------------------------------------------------------------------
# Pipeline de Benchmark (Árvore)
# ---------------------------------------------------------------------------
def run_benchmark():
    """
    Treina e avalia uma Random Forest como baseline de árvore.
    Registra os resultados no MLflow para comparação tríade.
    """
    logger.info("Carregando dados processados para benchmark de árvore...")
    train_df = pd.read_csv("data/processed/train_processed.csv")
    test_df = pd.read_csv("data/processed/test_processed.csv")

    X_train = train_df.drop(columns=["Churn"])
    y_train = train_df["Churn"]

    X_test = test_df.drop(columns=["Churn"])
    y_test = test_df["Churn"]

    # 1. Configurar experimento unificado no MLflow
    mlflow.set_experiment("churn-prediction")

    with mlflow.start_run(run_name="RandomForest_v1"):
        mlflow.set_tag("mlflow.runType", "TRAINING")
        # 2. Inicializar e treinar o modelo
        logger.info("Treinando Random Forest (n_estimators=100, class_weight='balanced')...")
        rf = RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            class_weight='balanced',
            random_state=42,
            n_jobs=-1
        )
        rf.fit(X_train, y_train)

        # 3. Predições
        y_pred = rf.predict(X_test)
        y_proba = rf.predict_proba(X_test)[:, 1]

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
            "model_type": "RandomForest",
            "n_estimators": 100,
            "max_depth": 10,
            "class_weight": "balanced",
            "n_jobs": -1,
            "random_state": 42,
            "data_split": "train_test_80_20_stratified",
            "cost_fn": 500,
            "cost_fp": 50,
        })
        mlflow.log_metrics(metrics)

        # Log do modelo como artefato
        mlflow.sklearn.log_model(rf, "model")

        logger.info("─" * 40)
        logger.info("BENCHMARK DE ÁRVORE CONCLUÍDO")
        for k, v in metrics.items():
            logger.info(f"  {k}: {v:.4f}")
        logger.info("─" * 40)

if __name__ == "__main__":
    run_benchmark()
