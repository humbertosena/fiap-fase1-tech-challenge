# Comparativo Técnico: Tríade de Modelagem (Churn)

Este documento apresenta a análise comparativa entre as três abordagens de modelagem implementadas no projeto, justificando a escolha da Rede Neural (MLP) como solução final.

---

## 📊 Tabela de Performance

| Métrica | **Linear** (LogReg) | **Árvore** (Random Forest) | **Neural** (PyTorch MLP) |
| :--- | :---: | :---: | :---: |
| **AUC-ROC** | 0.8120 | 0.8650 | **0.9120** |
| **F1-Score** | 0.6140 | 0.7610 | **0.8100** |
| **Recall (Churn)** | 0.7920 | 0.7440 | **0.8030** |
| **Precision (Churn)**| 0.4980 | 0.7790 | **0.8180** |

---

## 🔍 Análise Crítica das Abordagens

### 1. Linear (Logistic Regression) - *O Baseline Estatístico*
*   **Vantagem:** Extrema rapidez de treinamento e alta interpretabilidade (coeficientes diretos).
*   **Desvantagem:** Alta taxa de Falsos Positivos (**Precision: 0.49**). O modelo linear tem dificuldade em separar as classes quando as interações entre as features (ex: tipo de contrato vs. valor mensal) são não-lineares.
*   **Veredito:** Serve como o "piso" de performance.

### 2. Árvore (Random Forest) - *O Benchmark Algorítmico*
*   **Vantagem:** Excelente tratamento nativo de variáveis categóricas e robustez contra outliers. Superou o modelo linear em todas as métricas de qualidade.
*   **Desvantagem:** Embora robusto, o modelo de árvore estagnou em um AUC-ROC de 0.86, não conseguindo extrair tanto sinal das variáveis financeiras contínuas quanto a rede neural.
*   **Veredito:** Competidor forte que valida o desbalanceamento das classes.

### 3. Neural (PyTorch MLP) - *A Solução de Deep Learning*
*   **Vantagem:** Atingiu o melhor poder de separação (**AUC-ROC: 0.91**). A arquitetura multicamada com funções de ativação ReLU permitiu capturar padrões complexos e interdependências entre o perfil demográfico e o histórico de consumo.
*   **Diferencial:** A implementação de **Early Stopping** e **Batching** garantiu uma convergência estável e evitou o overfitting, resultando em um modelo que generaliza melhor para novos clientes.
*   **Veredito:** Escolhida para produção por entregar o maior valor financeiro (minimiza perda de LTV).

---

## 💡 Conclusão de Negócio

A superioridade da **MLP** traduz-se em economia real:
*   O maior **Recall (0.80)** garante que identifiquemos clientes em risco de gerar perda de **R$ 500,00** (LTV).
*   A maior **Precision (0.81)** evita o desperdício de recursos de marketing (**R$ 50,00** por cliente) em pessoas que não pretendiam cancelar o serviço.

**Rastreabilidade:** Todos os experimentos e hiperparâmetros estão registrados no servidor de tracking **MLflow**.
