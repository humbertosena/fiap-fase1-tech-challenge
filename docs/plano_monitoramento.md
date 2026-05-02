# Plano de Monitoramento e Resposta

Este documento detalha a estratégia para garantir a saúde e a performance do modelo de Churn em ambiente produtivo.

---

## 🛰️ 1. Métricas de Serviço (Saúde da API)

| Métrica | Ferramenta | Alerta |
| :--- | :--- | :--- |
| Latência da Predição | API Logs / CloudWatch | > 500ms (P99) |
| Erros HTTP (5xx) | API Logs | > 1% das requisições |
| Status do Modelo | Endpoint `/health` | status == "degraded" |

---

## 🧠 2. Métricas de Performance de ML (Drift)

O monitoramento de Churn requer a detecção de mudanças no comportamento do consumidor.

### Data Drift (Input)
*   **Métrica:** PSI (Population Stability Index).
*   **Frequência:** Mensal.
*   **Ação:** Se PSI > 0.2 em features críticas (`Contract`, `tenure`), disparar investigação.

### Model Drift (Output)
*   **Métrica:** Desvio na distribuição das probabilidades.
*   **Gatilho:** Se a taxa de Churn predita desviar > 10% da taxa histórica sem mudança externa aparente.

---

## 🔄 3. Playbook de Resposta

1.  **Alerta de Drift:** Iniciar retreino automático utilizando o comando `make train` com a safra de dados mais recente.
2.  **Degradação de Performance:** Se o retreino não resolver, reverter para o baseline linear (Regressão Logística) até a revisão do cientista de dados.
3.  **Erro de API:** Escalonamento para o time de SRE.

