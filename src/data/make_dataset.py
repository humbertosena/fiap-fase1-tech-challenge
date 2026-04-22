"""
make_dataset.py
===============
Script de ingestão e pré-processamento do dataset IBM Telco Customer Churn.

Reprodutibilidade:
    Este script garante a reprodutibilidade completa do pipeline de dados.
    Ele tentará baixar o dataset automaticamente via kagglehub.
    Caso o download automático falhe (sem credenciais do Kaggle), as instruções
    manuais serão exibidas no terminal.

    Fonte do dataset:
        https://www.kaggle.com/datasets/blastchar/telco-customer-churn

Uso:
    uv run python -m src.data.make_dataset
"""

import logging
import os
import shutil
import sys

import pandas as pd
from sklearn.model_selection import train_test_split

# ---------------------------------------------------------------------------
# Logging estruturado (substitui print() conforme boas práticas do enunciado)
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s — %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("make_dataset")

# Garante que o Python enxergue o pacote 'src' a partir da raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.features.build_features import engineer_features, preprocess_data
from src.utils.seed_config import set_seeds

# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------
DATASET_SLUG = "blastchar/telco-customer-churn"
DATASET_FILENAME = "WA_Fn-UseC_-Telco-Customer-Churn.csv"
KAGGLE_DATASET_URL = "https://www.kaggle.com/datasets/blastchar/telco-customer-churn"


# ---------------------------------------------------------------------------
# Funções auxiliares
# ---------------------------------------------------------------------------
def _resolve_project_root() -> str:
    """Retorna o caminho absoluto da raiz do projeto."""
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def _download_dataset(raw_data_path: str) -> bool:
    """
    Tenta fazer o download automático do dataset via kagglehub.

    Requer credenciais do Kaggle configuradas:
      - Via ~/.kaggle/kaggle.json, ou
      - Via variáveis de ambiente KAGGLE_USERNAME e KAGGLE_KEY.

    Retorna True se o download foi bem-sucedido, False caso contrário.
    """
    try:
        import kagglehub  # type: ignore

        logger.info("Iniciando download automático via kagglehub...")
        dataset_dir = kagglehub.dataset_download(DATASET_SLUG)
        src_file = os.path.join(dataset_dir, DATASET_FILENAME)

        if not os.path.exists(src_file):
            logger.error("Arquivo não encontrado no diretório baixado: %s", dataset_dir)
            return False

        os.makedirs(os.path.dirname(raw_data_path), exist_ok=True)
        shutil.copy2(src_file, raw_data_path)
        logger.info("Dataset copiado com sucesso para: %s", raw_data_path)
        return True

    except ImportError:
        logger.warning(
            "Pacote 'kagglehub' não encontrado. "
            "Instale com: pip install kagglehub"
        )
        return False
    except Exception as exc:
        logger.warning("Download automático falhou: %s", exc)
        return False


def _print_manual_instructions(raw_data_path: str) -> None:
    """Exibe instruções claras para download manual do dataset."""
    instructions = f"""
╔══════════════════════════════════════════════════════════════════════════╗
║          DATASET NÃO ENCONTRADO — INSTRUÇÃO DE REPRODUTIBILIDADE        ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  O dataset IBM Telco Customer Churn deve ser baixado manualmente:        ║
║                                                                          ║
║  1. Acesse: {KAGGLE_DATASET_URL:<54}  ║
║  2. Clique em "Download" (requer conta gratuita no Kaggle)               ║
║  3. Extraia o arquivo ZIP e coloque o CSV em:                            ║
║     {raw_data_path:<67}  ║
║                                                                          ║
║  OU configure suas credenciais do Kaggle e re-execute:                   ║
║     export KAGGLE_USERNAME=seu_usuario                                   ║
║     export KAGGLE_KEY=sua_chave_api                                      ║
║     uv run python -m src.data.make_dataset                               ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
"""
    print(instructions)


# ---------------------------------------------------------------------------
# Pipeline principal
# ---------------------------------------------------------------------------
def main() -> None:
    """Pipeline completo de ingestão e pré-processamento de dados."""
    # 1. Semente para reprodutibilidade rigorosa
    set_seeds(42)

    project_root = _resolve_project_root()
    raw_data_path = os.path.join(project_root, "data", "raw", DATASET_FILENAME)

    # 2. Verificar se o dataset já existe; se não, tentar download automático
    if not os.path.exists(raw_data_path):
        logger.warning("Dataset não encontrado em: %s", raw_data_path)
        logger.info("Tentando download automático...")

        downloaded = _download_dataset(raw_data_path)

        if not downloaded:
            _print_manual_instructions(raw_data_path)
            sys.exit(1)

    logger.info("Carregando dados brutos de: %s", raw_data_path)
    df = pd.read_csv(raw_data_path)
    logger.info("Dataset carregado. Shape: %s", df.shape)

    # 3. Feature Engineering
    logger.info("Executando Feature Engineering e sanidade de tipos...")
    df_engineered = engineer_features(df)

    # 4. Split Features / Target
    X = df_engineered.drop(columns=["Churn"])
    y = df_engineered["Churn"]

    # 5. Train/Test split estratificado (80/20)
    logger.info("Separando Treino e Teste (80/20, stratify=y)...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # 6. Pipeline de pré-processamento: Fit no Treino, Transform em ambos
    logger.info("Fit-Transform no Treino | Transform no Teste (sem Data Leakage)...")
    model_path = os.path.join(project_root, "models", "preprocessor.pkl")
    X_train_processed, X_test_processed, _ = preprocess_data(
        X_train, X_test, save_path=model_path
    )

    # 7. Reatribuir target e salvar CSVs processados
    train_final = X_train_processed.copy()
    train_final["Churn"] = y_train.values

    test_final = X_test_processed.copy()
    test_final["Churn"] = y_test.values

    out_dir = os.path.join(project_root, "data", "processed")
    os.makedirs(out_dir, exist_ok=True)

    train_path = os.path.join(out_dir, "train_processed.csv")
    test_path = os.path.join(out_dir, "test_processed.csv")

    train_final.to_csv(train_path, index=False)
    test_final.to_csv(test_path, index=False)

    # 8. Resumo final
    logger.info("─" * 60)
    logger.info("PIPELINE CONCLUÍDO COM SUCESSO")
    logger.info("  Preprocessor  → %s", model_path)
    logger.info("  Treino         → %s | Shape: %s", train_path, train_final.shape)
    logger.info("  Teste          → %s | Shape: %s", test_path, test_final.shape)
    logger.info("─" * 60)


if __name__ == "__main__":
    main()
