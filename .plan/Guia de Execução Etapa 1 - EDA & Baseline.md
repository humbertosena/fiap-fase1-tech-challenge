# **📊 Guia de Execução Etapa 1 - EDA & Baseline**

Este guia consolida o encerramento da engenharia de dados e inicia o ciclo de Deep Learning para o Tech Challenge.

## **1\. Setup e EDA (Passos 1 ao 2.3)**

**CONCLUÍDO:** Ambiente configurado, tipos tratados, desbalanceamento mapeado e perfis de risco identificados (Fibra Ótica/Contrato Mensal).

## **2\. Baselines e ROI (Passos 3 ao 5\)**

**CONCLUÍDO:** Baseline de Regressão Logística estabelecido (Recall 0.79) e Threshold Ótimo de **0.165** definido como meta financeira.

## **3\. Engenharia e Modularização (Passos 6 e 7\)**

**CONCLUÍDO:** \- Criada feature Charges\_per\_Tenure.

* Código migrado para src/.  
* **Status de Execução:** Script src/data/make\_dataset.py executado com sucesso.

## **4\. Transição para Fase 2: Redes Neurais (PyTorch)**

Agora que os dados estão processados, o objetivo é superar o custo de **R$ 35.850,00** usando uma MLP.

### **Passo 4.1: Definição do DataLoader**

Crie o notebook notebooks/02\_pytorch\_mlp.ipynb. A primeira tarefa é converter os CSVs processados em Tensores.

**Prompt para Gemini CLI:**

"Aja como um Deep Learning Engineer. Com base nos arquivos 'data/processed/train\_processed.csv' e 'test\_processed.csv':

1. Crie uma classe 'ChurnDataset' herdando de 'torch.utils.data.Dataset'.  
2. Implemente o 'DataLoader' para treino e teste com batch\_size=64.  
3. Garanta que o target 'Churn' seja convertido para 'torch.float32' para uso com 'BCEWithLogitsLoss'."

### **Passo 4.2: Arquitetura da MLP**

**Prompt para Gemini CLI:**

"Defina uma classe 'ChurnMLP' em PyTorch com:

* Camada de Entrada: 21 neurônios (conforme nosso dataset processado).  
* Camadas Ocultas: Duas camadas (ex: 16 e 8 neurônios) com ativação ReLU.  
* Camada de Saída: 1 neurônio (saída linear para Logits).  
* Inclua 'Dropout' de 0.2 para evitar overfitting."

## **5\. Rastreamento de Experimentos MLP (MLflow)**

Diferente do baseline, aqui vamos rastrear a **curva de perda (loss curve)**.

**Métricas obrigatórias FIAP para MLP:**

* learning\_rate  
* epochs  
* batch\_size  
* val\_loss (para Early Stopping)

## **Checklist de Prontidão para o Modelo Central:**

* \[X\] Arquivo models/preprocessor.pkl gerado (essencial para a API futura).  
* \[X\] Dados de treino/teste prontos em data/processed/.  
* \[ \] Classe de arquitetura da MLP definida.  
* \[ \] Loop de treinamento com **Early Stopping** implementado (Requisito Obrigatório).