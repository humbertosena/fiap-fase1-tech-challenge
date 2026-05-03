# Churn Prediction System | Telecom End-to-End Solution

[![Python](https://img.shields.io/badge/python-3.10+-3670A0?style=flat&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch)](https://pytorch.org/)
[![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=flat&logo=mlflow)](https://mlflow.org/)

Este repositório contém a solução completa para o **Tech Challenge (Fase 1)** da Pós-Graduação em **Machine Learning Engineering (FIAP)**. O sistema utiliza Deep Learning para prever a evasão de clientes (Churn) com foco em resiliência industrial e governança.

---

## 📈 Visão Executiva
O Churn (rotatividade de clientes) custa à operadora de telecomunicações aproximadamente **R$ 500,00 por cliente perdido** (LTV médio). Nossa solução reduz esse impacto ao identificar com **91% de AUC-ROC** os perfis de risco, permitindo ações de retenção cirúrgicas.

### Principais Resultados:
*   **Modelo Neural:** Superou baselines lineares em **15%** de F1-Score.
*   **Confiabilidade:** Sistema de gatekeeping que impede a inferência sobre dados corrompidos.
*   **Governança:** 100% dos experimentos rastreados e auditáveis via MLflow.

---

## 🏗️ Arquitetura do Sistema

```mermaid
graph TD
    A[Raw Data] --> B[Pipeline src.data]
    B --> C{Validação Pandera}
    C -->|Sucesso| D[Feature Engineering]
    D --> E[Treino PyTorch MLP]
    E --> F[MLflow Tracking]
    F --> G[Model Registry .pth]
    G --> H[FastAPI Service]
    H --> I[/predict Endpoint]
    I --> J{Pydantic Check}
    J -->|OK| K[Inferência]
    K --> L[Resposta JSON]
```

---

## 🛠️ Guia de Início Rápido

### 1. Requisitos
*   Python 3.10+
*   [uv](https://github.com/astral-sh/uv) (Gerenciador de pacotes ultrarrápido)

### 2. Instalação e Preparação
```bash
make install
# Para fins de teste/validação (gera dados sintéticos):
uv run python tests/create_raw_dummy.py
uv run python -m src.data.make_dataset
```

### 3. Comandos Principais (Makefile)
| Comando | Descrição |
| :--- | :--- |
| `make train` | Treina a MLP com Early Stopping e loga no MLflow. |
| `make benchmark` | Executa o comparativo contra Random Forest. |
| `make test` | Roda a suíte de testes automatizados e de integração. |
| `make run-api` | Inicia o servidor FastAPI (Porta 8000). |

---

## 📊 Governança & MLOps (MLflow)
O projeto utiliza **MLflow** para rastreamento de experimentos. Para visualizar a performance de todos os modelos (Linear vs Árvore vs Neural):

1. Inicie a UI: \`uv run mlflow ui --backend-store-uri sqlite:///mlflow.db\`
2. Acesse: \`http://localhost:5000\`

---

## 📄 Documentação Técnica


Para uma visão aprofundada, consulte os artefatos de governança:

1.  **[Model Card](docs/model_card.md)**: Detalhes da arquitetura, métricas e vieses.
2.  **[Monitoring Playbook](docs/monitoring_playbook.md)**: Estratégia de Drift e resposta a incidentes.
3.  **[ADRs (Decisões de Arquitetura)](docs/adr/)**: Por que escolhemos FastAPI e Pandera.
4.  **[Comparativo da Tríade](docs/comparativo_triade_modelos.md)**: Análise entre Linear, Árvore e MLP.

---

## 🎥 Pitch de Apresentação
O vídeo detalhando a jornada técnica e os resultados de negócio pode ser acessado em:
> **[LINK DO VÍDEO AQUI]** (Duração: 5 minutos | Método STAR)

---

## 👥 Autores (Equipe)
*   **Humberto Sena Santos** (RM370472)
*   **João Victor Faustino Piga Lopes** (RM374010)

---
**FIAP - MLET | 2026**
