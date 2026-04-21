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

### 2. Qualidade de Código (Linting)

Executa o Ruff para garantir a aderência às normas da PEP 8:

```bash
make lint
```

### 3. Execução de Testes

Roda a suíte de testes automatizados com Pytest:

```bash
make test
```

### 4. Iniciar a API de Predição

Sobe o servidor FastAPI localmente:

```bash
make run-api
```

---

## 📊 Model Tracking (MLflow)

Para visualizar o histórico de experimentos, performance das épocas da rede neural e comparar diferentes arquiteturas de MLP:

1. Execute o servidor de tracking local:
   ```bash
   uv run mlflow ui
   ```
2. Acesse no seu navegador: `http://localhost:5000`

---

## 🎥 Vídeo de Apresentação (Método STAR)

> **[LINK PARA O VÍDEO AQUI]**  
> _O vídeo detalha o **S**ituaton (Situação), **T**ask (Tarefa), **A**ction (Ação) e **R**esult (Resultado) do projeto, conforme os requisitos da FIAP._

---

## 👥 Autores

| Nome                     | RM       | Função no Projeto                               |
| :----------------------- | :------- | :---------------------------------------------- |
| **Humberto Sena Santos** | RM370472 | ML Engineer / DevOps / Data Scientist / Analyst |

---

**FIAP - Machine Learning Engineering | 2026**
