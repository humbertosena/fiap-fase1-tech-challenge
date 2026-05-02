# 📦 Estrutura Remota — GitHub

**Repositório**: `humbertosena/fiap-fase1-tech-challenge`  
**Branch**: `main`  
**Último commit**: `dca8cc1` — *feat: Execução da etapa Notebook EDA e fechamento da v0.3 do ML canvas*  
**Verificado em**: 22/04/2026  
**Divergência local**: Nenhuma (HEAD = origin/main). Único arquivo modificado localmente: `.gitignore`

---

## Árvore de Arquivos Sincronizados

| Caminho | Tipo | Tamanho | Descrição |
|:--------|:-----|--------:|:----------|
| `.gitignore` | config | 227 B | Regras de exclusão (venv, dados, artefatos) |
| `LICENSE` | doc | 1.1 KB | Licença MIT |
| `Makefile` | config | 325 B | Comandos rápidos: lint, test, run |
| `README.md` | doc | 4.9 KB | Guia de entrada do projeto |
| `pyproject.toml` | config | 581 B | Configuração central (Ruff, Pytest, Deps) |
| `requirements.txt` | config | 2.1 KB | Dependências congeladas |

### `data/` — Dados

| Caminho | Tamanho | Descrição |
|:--------|--------:|:----------|
| `data/raw/.gitkeep` | 0 B | Placeholder — dados brutos não versionados (`.gitignore`) |
| `data/processed/.gitkeep` | 0 B | Placeholder — dados processados não versionados |

> **Nota**: Os CSVs (`WA_Fn-UseC_-Telco-Customer-Churn.csv`, `train_processed.csv`, `test_processed.csv`) existem apenas localmente, protegidos pelo `.gitignore`.

### `docs/` — Documentação

| Caminho | Tamanho | Descrição |
|:--------|--------:|:----------|
| `docs/ml_canvas.md` | 5.0 KB | ML Canvas v0.3 — 10 seções (Value Prop → Monitoramento) |
| `docs/memoria_desenvolvimento.md` | 9.4 KB | Log cronológico de todas as atividades de desenvolvimento |

### `models/` — Artefatos de Modelo

| Caminho | Tamanho | Descrição |
|:--------|--------:|:----------|
| `models/.gitkeep` | 0 B | Placeholder — `preprocessor.pkl` existe apenas localmente |

### `notebooks/` — Experimentação

| Caminho | Tamanho | Descrição |
|:--------|--------:|:----------|
| `notebooks/01_eda_churn.ipynb` | 285 KB | Notebook principal de EDA (análise completa + baselines + ROI) |
| `notebooks/README.md` | 3.3 KB | Guia de configuração do ambiente (`uv`, `ipykernel`) |
| `notebooks/mlflow.db` | 664 KB | Banco SQLite do MLflow com 3 runs de experimentos |
| `notebooks/mlruns_artifacts/confusion_matrix.png` | 22.6 KB | Matriz de confusão do baseline (artefato MLflow) |
| `notebooks/mlruns_artifacts/cost_vs_threshold.png` | 48.2 KB | Curva de Custo vs. Threshold (artefato MLflow) |
| `notebooks/.ipynb_checkpoints/01_EDA_Telco_Churn-checkpoint.ipynb` | 1.9 KB | Checkpoint automático do Jupyter |

### `src/` — Código Fonte Modularizado

| Caminho | Tamanho | Descrição |
|:--------|--------:|:----------|
| `src/__init__.py` | 0 B | Inicializador do pacote raiz |
| **`src/api/`** | | **Endpoints FastAPI** |
| `src/api/__init__.py` | 0 B | Inicializador |
| `src/api/main.py` | 634 B | Endpoint base da API (scaffold) |
| **`src/data/`** | | **Loading e Split de Dados** |
| `src/data/__init__.py` | 0 B | Inicializador |
| `src/data/make_dataset.py` | 2.8 KB | Script orquestrador: raw → split → preprocess → CSVs |
| **`src/features/`** | | **Feature Engineering e Pipelines** |
| `src/features/__init__.py` | 0 B | Inicializador |
| `src/features/build_features.py` | 2.9 KB | ColumnTransformer + `Charges_per_Tenure` + export `.pkl` |
| **`src/models/`** | | **Definições de Modelos** |
| `src/models/__init__.py` | 0 B | Inicializador (MLP ainda não implementada) |
| **`src/utils/`** | | **Utilitários** |
| `src/utils/__init__.py` | 0 B | Inicializador |
| `src/utils/logging_config.py` | 603 B | Configuração de logging estruturado |
| `src/utils/seed_config.py` | 881 B | `set_seeds()` — determinismo (random, numpy, OS) |

---

## Resumo Quantitativo

| Métrica | Valor |
|:--------|------:|
| Total de arquivos no remoto | 28 |
| Tamanho total estimado | ~1.04 MB |
| Commits no `main` | 5 |
| Arquivos apenas locais (não sincronizados) | Dados CSV, `preprocessor.pkl`, `.venv/`, `mlruns/` |

---

## Histórico de Commits

| Hash | Mensagem |
|:-----|:---------|
| `dca8cc1` | feat: Execução da etapa Notebook EDA e fechamento da v0.3 do ML canvas |
| `e5d0c0d` | doc: Ajuste ML Canvas para v0.2 - Design Baseado em Experimentação |
| `fe6ae59` | doc: Preenchimento da v0.1 do documento ML Canvas |
| `55a1a59` | chore: Estrutura inicial do projeto criado por agents de desenvolvimento |
| `7562fb6` | chore: Criação do projeto |
