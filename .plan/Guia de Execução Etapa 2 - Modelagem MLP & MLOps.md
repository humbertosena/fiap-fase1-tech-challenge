# **🧠 Guia de Execução: Etapa 2 \- Modelagem MLP & MLOps**

Este guia orienta a transição do experimento estatístico para a construção de uma **Multi-Layer Perceptron (MLP)** utilizando **PyTorch**, integrada ao **MLflow** para governança e rastreabilidade centralizada.

## **📅 Cronograma Sugerido (Semana 2\)**

| Dia | Atividade | Entregável Técnico |
| :---- | :---- | :---- |
| **Dia 1** | Implementação do ChurnDataset e DataLoaders | src/models/dataset.py |
| **Dia 2** | Definição da Arquitetura ChurnMLP (SOLID) | src/models/network.py |
| **Dia 3** | Loop de Treino com Early Stopping e Validação | src/models/train\_model.py |
| **Dia 4** | Rastreamento Pro: Configuração de Backend Store e Logs | MLflow (sqlite:///mlflow.db) |
| **Dia 5** | Comparação Técnica: MLP vs Regressão Logística | Relatório de Performance |

## **🛠️ Passo a Passo Detalhado**

### **1\. Camada de Dados (PyTorch Dataset)**

**O que fazer:** Criar uma classe herdando de torch.utils.data.Dataset para consumir os arquivos data/processed/train\_processed.csv e test\_processed.csv.

**Por que:** O PyTorch exige objetos DataLoader para gerenciar o batching e o embaralhamento de forma eficiente, evitando gargalos de I/O.

### **2\. Arquitetura da MLP (Deep Learning)**

**O que fazer:** Definir uma rede com:

* **Input Layer:** 21 neurônios (ajustar conforme a saída do seu preprocessor.pkl).  
* **Hidden Layers:** Duas camadas ocultas (ex: 16 e 8 neurônios) com ativação ReLU.  
* **Dropout:** Adicionar nn.Dropout(0.2) entre as camadas.  
* **Output Layer:** 1 neurônio com saída linear (usaremos BCEWithLogitsLoss).

### **3\. Loop de Treino e Early Stopping**

**O que fazer:** Implementar um loop que monitore a val\_loss. Se a perda não diminuir por 5 épocas seguidas, interromper o treino.

### **4\. Rastreamento com MLflow (Governança Centralizada)**

**O que fazer:** 1\. **Centralização:** Mover o arquivo mlflow.db da pasta notebooks/ para a **raiz do projeto**.

2\. **URI de Tracking:** Em todos os scripts e notebooks, configurar o acesso via:

mlflow.set\_tracking\_uri("sqlite:///mlflow.db")

3. **Log de Experimento:** Envolver o treinamento em um with mlflow.start\_run() registrando:  
   * **Params:** lr, batch\_size, hidden\_units.  
   * **Metrics:** Logs por época de train\_loss e val\_loss.  
   * **Artifacts:** O arquivo de pesos .pth.

**Por que:** A centralização na raiz permite que os scripts em src/ e os notebooks em notebooks/ compartilhem a mesma base de dados de experimentos, seguindo princípios de Clean Architecture.

## **🏗️ Nota de Engenharia: Organização do Backend Store**

Para garantir nota máxima nos critérios de **Qualidade de Código** e **Pipelines**, a estrutura deve seguir o padrão:

1. **Localização:** mlflow.db deve residir em ./ (root).  
2. **Git LFS:** Certifique-se de que o Git LFS está rastreando o arquivo no novo caminho (git lfs track "mlflow.db").  
3. **Interoperabilidade:** O uso do URI sqlite:///mlflow.db garante que o MLflow utilize o SQLAlchemy para gerenciar os metadados de forma concorrente e segura.

## **✅ Checklist de Prontidão para Etapa 2**

* [x] Arquivo mlflow.db movido para a raiz do projeto.  
* [x] Scripts configurados com mlflow.set_tracking_uri("sqlite:///mlflow.db").  
* [x] Classe ChurnDataset pronta para carregar os tensores.  
* [x] Experimento Churn_Prediction_MLP criado no MLflow.  
* [x] .gitattributes atualizado para o novo caminho do banco de dados (se necessário).
* [x] Comparação técnica MLP vs Baseline realizada.