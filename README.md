# Tech Challenge - Fase 1 | Pós-Graduação Machine Learning Engineering - FIAP

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)
![MLflow](https://img.shields.io/badge/mlflow-%23d9ead3.svg?style=for-the-badge&logo=numpy&logoColor=blue)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

Este projeto é o requisito fundamental para a conclusão da **Fase 1** da Pós-Graduação em Machine Learning Engineering da **FIAP**.

## 🎯 Tema do Projeto

**Rede Neural para Previsão de Churn com Pipeline Profissional End-to-End.**

O objetivo é desenvolver uma solução robusta de Deep Learning para prever a evasão de clientes (Churn) em uma operadora de Telecomunicações, integrando práticas avançadas de Engenharia de Software e MLOps.

---

## 📋 Entregáveis por Etapa

| Etapa | Descrição                    | Entregáveis                                              | Data       |
| :---: | :--------------------------- | :------------------------------------------------------- | :--------- |
| **1** | Entendimento e Preparação    | Notebook de EDA + baselines registrados no MLflow        | 22/04/2026 |
| **2** | Modelagem com Redes Neurais  | MLP (PyTorch) com early stopping + comparação de métricas | —          |
| **3** | Engenharia e API             | `src/` modularizado + endpoints FastAPI + testes Pytest  | —          |
| **4** | Documentação e Finalização   | Model Card + README final + vídeo STAR (5 min)           | —          |

---

## 💼 Contexto de Negócio

No setor de Telecomunicações, o **Churn Rate** (taxa de rotatividade) é uma das métricas mais críticas de performance. Reter um cliente atual é estrategicamente mais barato do que adquirir um novo (CAC - Customer Acquisition Cost).

Esta solução visa identificar padrões de comportamento que precedem o cancelamento, permitindo que a equipe de marketing atue proativamente com campanhas de retenção personalizadas, maximizando o LTV (Lifetime Value) e a saúde financeira da companhia.

---

## 🏗️ Arquitetura da Solução

A solução foi construída sobre três pilares principais:

1.  **Deep Learning com PyTorch:** Implementação de uma rede neural **Multi-Layer Perceptron (MLP)**. A arquitetura foca na captura de relações não lineares complexas entre as variáveis de perfil de consumo, serviços assinados e dados demográficos.
2.  **MLOps com MLflow:** Todo o ciclo de vida do experimento (hiperparâmetros, métricas de loss, acurácia e o artefato do modelo final) é rastreado via MLflow, garantindo reprodutibilidade e governança.
3.  **Deploy via API (FastAPI):** O modelo é exposto através de uma API assíncrona de alta performance, pronta para integração com sistemas de CRM ou dashboards de monitoramento.

---

## 📂 Estrutura do Projeto

```text
├── data/               # Armazenamento de dados (raw/processed)
├── docs/               # Documentação técnica adicional
├── models/             # Artefatos de modelos treinados localmente
├── notebooks/          # Exploração de dados (EDA) e prototipagem
├── src/                # Código fonte modularizado
│   ├── api/            # Endpoints FastAPI para inferência
│   ├── data/           # Scripts de ingestão e limpeza de dados
│   ├── features/       # Pipeline de feature engineering
│   ├── models/         # Definição da arquitetura MLP e treinamento
│   └── utils/          # Helpers (logging, seeds, configs)
├── tests/              # Testes unitários e de integração
├── Makefile            # Automação de tarefas (instalação, lint, test)
├── pyproject.toml      # Gerenciamento de dependências e ferramentas
└── README.md           # Documentação principal
```

---

## 🛠️ Instalação e Execução

O projeto utiliza o **`uv`** como gerenciador de pacotes, garantindo instalações ultrarrápidas e determinísticas.

### 1. Preparar o Ambiente

Instala as dependências e cria o ambiente virtual:

```bash
make install
```

### 2. Pipeline de Dados (Pandera & Reprodutibilidade)

Antes de rodar a API ou treinar o modelo, é necessário baixar e processar o dataset. O projeto utiliza **Pandera** para garantir que os dados de entrada estejam em conformidade com as expectativas de negócio.

```bash
# Configura credenciais e roda o pipeline completo
export KAGGLE_USERNAME=seu_usuario
export KAGGLE_KEY=sua_chave_api
uv run python -m src.data.make_dataset
```

### 3. Qualidade de Código (Ruff)

Executa o linter e o formatador para garantir a aderência às normas da PEP 8 e critérios de avaliação da FIAP:

```bash
make lint
```

### 4. Execução de Testes (Pytest)

Roda a suíte de testes automatizados, cobrindo endpoints da API, schemas de dados e lógica de processamento:

```bash
make test
```

### 5. Treinamento da Rede Neural (PyTorch & MLflow)

Executa o treinamento modularizado da MLP. Este processo inclui batching, **Early Stopping** e registro automático de métricas no MLflow.

```bash
make train
```

### 6. Iniciar a API de Predição (FastAPI)

Sobe o servidor FastAPI localmente para realizar inferências. A API conta com validação **Pydantic**, documentação automática via Swagger e logging estruturado.

```bash
make run-api
```
*   **Acesse o Swagger:** [http://localhost:8000/docs](http://localhost:8000/docs)
*   **Endpoints principais:** `/predict` (POST), `/health` (GET), `/version` (GET).

---

## 📦 Reprodutibilidade & Dataset

O dataset utilizado é o **IBM Telco Customer Churn**, disponível publicamente no Kaggle:

> **🔗 Dataset:** [https://www.kaggle.com/datasets/blastchar/telco-customer-churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

Por boas práticas de MLOps, os arquivos de dados **não são versionados no repositório** (protegidos pelo `.gitignore`). Para reproduzir o pipeline do zero:

### Opção A — Download automático (recomendado)

Configure suas credenciais do Kaggle e execute:

```bash
# 1. Configure suas credenciais (somente na primeira vez)
#    Obtenha a API Key em: https://www.kaggle.com/settings/account
export KAGGLE_USERNAME=seu_usuario
export KAGGLE_KEY=sua_chave_api

# 2. Execute o script — ele baixa e processa tudo automaticamente
uv run python -m src.data.make_dataset
```

### Opção B — Download manual

1. Acesse o [link do dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) (conta gratuita no Kaggle)
2. Baixe e extraia o arquivo ZIP
3. Coloque o CSV em `data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv`
4. Execute o pipeline de pré-processamento:

```bash
uv run python -m src.data.make_dataset
```

> O script gera automaticamente `data/processed/train_processed.csv` e `data/processed/test_processed.csv` com o preprocessor salvo em `models/preprocessor.pkl`.

---

## 📊 Model Tracking (MLflow)

Para visualizar o histórico de experimentos, performance das épocas da rede neural e comparar diferentes arquiteturas de MLP:

1. Execute o servidor de tracking local:
   ```bash
   uv run mlflow ui --backend-store-uri sqlite:///notebooks/mlflow.db
   ```
2. Acesse no seu navegador: `http://localhost:5000`

### 💾 Armazenamento do Banco de Dados (Git LFS)

Neste projeto acadêmico, o arquivo `notebooks/mlflow.db` está sendo rastreado via **Git LFS (Large File Storage)**. 

*   **Por que Git LFS?** Isso permite preservar o tamanho do histórico do Git, evitando que o repositório fique excessivamente pesado com o crescimento do banco de dados SQLite. 
*   **Limites:** A conta gratuita do GitHub disponibiliza até **1 GB** de armazenamento LFS, o que é perfeitamente adequado para o escopo dos experimentos desta fase.

> **⚠️ Nota para Produção:** Para ambientes produtivos ou caso o histórico do MLflow ultrapasse 1 GB, é fortemente recomendado migrar o banco de dados e os artefatos para soluções mais robustas e escaláveis, como **Databricks**, **AWS/Azure/GCP File Storage (S3/Blob/GCS)** ou um banco de dados relacional gerenciado (PostgreSQL/MySQL) fora da estrutura do repositório Git.

---

## 🎥 Vídeo de Apresentação (Método STAR)

> **[LINK PARA O VÍDEO AQUI]**  
> _O vídeo detalha o **S**ituaton (Situação), **T**ask (Tarefa), **A**ction (Ação) e **R**esult (Resultado) do projeto, conforme os requisitos da FIAP._

---

## 👥 Autores

| Nome                                | RM       | Função no Projeto                               |
| :---------------------------------- | :------- | :---------------------------------------------- |
| **Humberto Sena Santos**            | RM370472 | ML Engineer / DevOps / Data Scientist / Analyst |
| **João Victor Faustino Piga Lopes** | RM374010 | ML Engineer / DevOps / Data Scientist / Analyst |

---

**FIAP - Machine Learning Engineering | 2026**
