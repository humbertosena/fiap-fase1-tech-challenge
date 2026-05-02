# 📋 Resumo da Etapa 1 — Exploração & Design

**Projeto**: Previsão de Churn – FIAP Tech Challenge Fase 1  
**Data de Verificação**: 22/04/2026  
**Referências**: [Planejamento Tech Challenge](Planejamento%20Tech%20Challenge%20-%20Fase%201.md) | [Guia de Execução Etapa 1 - EDA & Baseline](Guia%20de%20Execução%20Etapa%201%20-%20EDA%20&%20Baseline.md)

---

## 1. Semana 1 — Exploração & Design

| # | Entregável | Critério (Planejamento) | Evidência no Repositório | Status |
|:-:|:-----------|:------------------------|:-------------------------|:------:|
| 1 | ML Canvas preenchido | PDF/IMG em `docs/` | `docs/ml_canvas.md` — v0.3 com 10 seções completas (Value Prop, ML Task, Features, Avaliação, Monitoramento) | ✅ |
| 2 | Notebook de EDA | Notebook em `notebooks/` com análise Pandas/Seaborn | `notebooks/01_eda_churn.ipynb` (~285 KB) — sanidade de tipos, desbalanceamento, análise bivariada, boxplots | ✅ |
| 3 | Definição de métricas (negócio vs. técnicas) | Métricas documentadas | ML Canvas §9 — AUC-ROC, F1, PR-AUC (técnicas) + ROI Campanha, Churn Evitado, Matriz de Custo FN/FP (negócio) | ✅ |
| 4 | Feature Engineering | Criação de features sintéticas | Feature `Charges_per_Tenure` criada e documentada (EDA + `build_features.py`) | ✅ |

---

## 2. Semana 2 — Baselines & Tracking

| # | Entregável | Critério (Planejamento) | Evidência no Repositório | Status |
|:-:|:-----------|:------------------------|:-------------------------|:------:|
| 5 | Setup MLflow | Experimentos registrados | `notebooks/mlflow.db` (663 KB) + `notebooks/mlruns/` com 3 runs registradas | ✅ |
| 6 | Baseline Regressão Logística | Modelo treinado com métricas logadas | Run com `class_weight='balanced'`, Recall 0.79, Feature Importance logada | ✅ |
| 7 | Otimização de Threshold (ROI) | Análise de custo financeiro | Threshold ótimo **0.165** calculado; Curva de Custo vs. Threshold logada como artefato MLflow | ✅ |
| 8 | Versionamento de dados | Dados brutos e processados versionados | `data/raw/` (dataset original) + `data/processed/` (train/test CSVs + telco_final_for_mlp.csv) | ✅ |

---

## 3. Semana 3 (parcial) — Engenharia & Modularização

| # | Entregável | Critério (Guia de Execução Etapa 1) | Evidência no Repositório | Status |
|:-:|:-----------|:---------------------------|:-------------------------|:------:|
| 9 | Migração para `src/` | Código modularizado em produção | `src/data/make_dataset.py`, `src/features/build_features.py`, `src/utils/seed_config.py` | ✅ |
| 10 | Pipeline Sklearn (`ColumnTransformer`) | Preprocessor exportável | `models/preprocessor.pkl` (7.6 KB) gerado via `build_features.py` | ✅ |
| 11 | Seed determinístico | Função `set_seeds()` | `src/utils/seed_config.py` — seeds para `random`, `numpy`, SO | ✅ |

---

## 4. Checklist de Prontidão para MLP (Guia de Execução Etapa 1 §Checklist)

| Item | Status |
|:-----|:------:|
| Arquivo `models/preprocessor.pkl` gerado | ✅ |
| Dados treino/teste prontos em `data/processed/` | ✅ |
| Classe de arquitetura da MLP definida | ❌ Pendente |
| Loop de treinamento com Early Stopping | ❌ Pendente |

---

## Conclusão

> **A fase "Exploração & Design" (Semanas 1-2) está 100% concluída.** Todos os 8 entregáveis obrigatórios foram verificados no repositório.  
> A Semana 3 (Engenharia) também está concluída na parte de dados/pipeline. Os itens pendentes pertencem à **Fase 2 — Deep Learning (PyTorch)**, que é a próxima etapa a ser iniciada.
