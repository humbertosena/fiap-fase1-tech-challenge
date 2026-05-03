# Monitoring Playbook: Churn Prediction Service

Este documento define os SLOs, métricas de drift e ações de resposta para o modelo ChurnMLP em produção.

---

## 🛰️ 1. MLOps SLOs (Service Level Objectives)

| Indicador | Objetivo (Target) | Ferramenta |
| :--- | :--- | :--- |
| **Latência de Inferência** | < 200ms (P95) | FastAPI Logs |
| **Disponibilidade** | 99.9% | Health Check Endpoint |
| **Acurácia (Recall)** | > 0.75 | MLflow / Produção |

---

## 🧠 2. Detecção de Model Drift & Data Drift

### Data Drift (Entrada)
*   **Métrica:** Population Stability Index (PSI).
*   **Frequência:** Semanal.
*   **Threshold:** PSI > 0.2 em colunas críticas como `MonthlyCharges`.
*   **Ação:** Validar se houve mudança no catálogo de produtos da empresa.

### Concept Drift (Saída)
*   **Métrica:** Distribuição das probabilidades de predição.
*   **Gatilho:** Se a média de probabilidade de Churn subir > 15% em 24h sem campanhas externas.

---

## 🔄 3. Playbook de Resposta (Incidentes)

### Cenário A: Erro de Validação (422 Unprocessable Entity)
1. Verificar logs da API para identificar qual campo falhou no contrato **Pandera/Pydantic**.
2. Notificar o time de Engenharia de Dados sobre mudança no schema da fonte.

### Cenário B: Queda de Performance (Recall < 0.70)
1. Executar o script de retreino: `make train`.
2. Comparar a nova run no MLflow com a baseline de produção.
3. Se a performance não subir, realizar rollback para o modelo de **Random Forest** (mais estável).

### Cenário C: Latência Alta (> 500ms)
1. Verificar carga de CPU no servidor FastAPI.
2. Escalar horizontalmente o serviço de inferência.

---
**Data:** 02 de maio de 2026  
**Responsável:** MLOps Team
