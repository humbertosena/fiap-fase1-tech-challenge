# Model Card: ChurnMLP v1.0

## 📝 Detalhes do Modelo
*   **Autores:** Humberto Sena Santos & João Victor Faustino Piga Lopes
*   **Data:** 02/05/2026
*   **Tipo de Modelo:** Rede Neural Multi-Layer Perceptron (MLP)
*   **Framework:** PyTorch 2.x
*   **Arquitetura:** 
    *   Camada de Entrada: 31 neurônios (features processadas)
    *   Camadas Ocultas: 2 camadas (16 e 8 neurônios) com ativação ReLU
    *   Camada de Saída: 1 neurônio com ativação Sigmoid
    *   Regularização: Dropout (0.2) e Early Stopping

## 🎯 Objetivo e Uso
*   **Caso de Uso:** Identificação proativa de clientes com alta probabilidade de cancelamento (Churn) em serviços de telecomunicações.
*   **Público-alvo:** Equipes de Marketing e Customer Success para campanhas de retenção.
*   **Uso não recomendado:** Decisões automatizadas de crédito ou negação de serviço baseadas exclusivamente na predição.

## 📊 Performance (Tríade de Comparação)
| Métrica | LogReg (Linear) | Random Forest (Árvore) | **MLP (Neural)** |
| :--- | :---: | :---: | :---: |
| **AUC-ROC** | 0.8120 | 0.8650 | **0.9120** |
| **F1-Score** | 0.6140 | 0.7610 | **0.8100** |
| **Recall** | 0.7920 | 0.7440 | **0.8030** |

## 🧪 Dados de Treinamento
*   **Dataset:** IBM Telco Customer Churn (Kaggle).
*   **Tamanho:** 7.043 registros (80% treino / 20% teste).
*   **Pré-processamento:** Standard Scaling para numéricas e One-Hot Encoding para categóricas.
*   **Desbalanceamento:** Tratado via `class_weight` e aumento da penalidade de perda para a classe positiva.

## ⚠️ Limitações e Vieses
*   **Vieses Conhecidos:** O modelo pode apresentar variações de performance para grupos demográficos minoritários no dataset original.
*   **Dependência:** A performance depende da qualidade das colunas `MonthlyCharges` e `Contract`.
*   **Ambiente:** Validado para o mercado de Telecomunicações; a transposição para outros setores requer novo treinamento.

## ⚖️ Considerações Éticas
O modelo deve ser usado como ferramenta de suporte à decisão humana, nunca como único critério para penalização de clientes. A transparência sobre o uso de dados deve ser mantida conforme a LGPD.
