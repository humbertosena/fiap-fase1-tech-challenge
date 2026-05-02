# **🚀 Planejamento Estratégico: Tech Challenge \- Fase 1 (Churn MLP)**

Este documento estabelece o cronograma, a arquitetura e os padrões de qualidade para a entrega do Tech Challenge da Fase 1 da Pós-Tech FIAP, conforme o enunciado oficial.

## **1\. Visão Geral do Projeto**

* **Objetivo:** Previsão de Churn para operadora de Telecom (End-to-End).  
* **Modelo Principal:** Multi-Layer Perceptron (MLP) via PyTorch.  
* **Stack Técnica:** Python, PyTorch, Scikit-Learn, MLflow, FastAPI, Pytest, Ruff.  
* **Deadline Final:** 05/05/2026.

## **2\. Cronograma de Execução (4 Etapas)**

| Etapa | Fase | Atividades Principais | Prazo | Status |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **Entendimento & Preparação** | ML Canvas; EDA completa; Definição de métricas; Treino de Baselines + MLflow. | 24/04 | ✅ Concluída |
| **2** | **Modelagem (PyTorch)** | Arquitetura MLP; Loop de treino com **Early Stopping**; Comparação vs Baselines. | 28/04 | ✅ Concluída |
| **3** | **Engenharia & API** | Refatoração `src/`; Validação **Pandera**; Endpoints FastAPI (`/predict`, `/health`). | 02/05 | 🔄 Planejada |
| **4** | **Doc & Finalização** | Model Card; Playbook de Resposta; README Final; Vídeo STAR (5 min). | 05/05 | 🔄 Planejada |

## **3\. Arquitetura do Repositório (Standard FIAP)**

Seguiremos rigorosamente a estrutura modular para garantir a nota máxima em "Qualidade de Código":

├── data/               \# Dados brutos e processados  
├── docs/               \# Model Card, ML Canvas e Playbook  
├── models/             \# Artefatos (.pth, .pkl)  
├── notebooks/          \# EDA e experimentação  
├── src/                \# Código fonte modularizado  
│   ├── api/            \# Endpoints FastAPI e Schemas Pydantic  
│   ├── data/           \# Scripts de limpeza e split  
│   ├── features/       \# Feature Engineering e Pandera Schemas  
│   ├── models/         \# Arquitetura MLP e Treinamento  
│   └── utils/          \# Logging, Seeds e Helpers  
├── tests/              \# Pytest (Smoke, Schema, API)  
├── pyproject.toml      \# Dependências e Ruff Config  
├── Makefile            \# Automação (make lint, make test)  
└── README.md           \# Guia de execução

## **4\. Checklist de Requisitos Obrigatórios**

### **🛠️ Etapa 1: Preparação (Engenharia e MLOps)**
* [x] **Seeds Fixados:** Garantir reprodutibilidade (random, numpy, torch).  
* [x] **MLflow Tracking:** Registro de parâmetros, métricas e artefatos.  
* [x] **Logging Estruturado:** Uso de `logging` em vez de `print()`.  
* [x] **Linting:** Zero erros no Ruff.
* [x] **EDA & Baselines:** ML Canvas e Regressão Logística finalizados.

### **🧠 Etapa 2: Modelagem (Rede Neural)**
* [x] **Arquitetura MLP:** Implementação em PyTorch (Input/Hidden/Output).  
* [x] **Loss & Optimizer:** Definição adequada para classificação binária.
* [x] **Treinamento Pro:** Implementar batching e **Early Stopping**.  
* [x] **Comparação:** Avaliar MLP vs Baselines em pelo menos 4 métricas.

### **🔌 Etapa 3: Engenharia & API**
* [ ] **Modularização:** Código 100% migrado para a pasta `src/`.  
* [ ] **Validação Pandera:** Garantir integridade dos DataFrames no pipeline.
* [ ] **FastAPI:** Endpoints `/predict`, `/health` e `/version` funcionais.  
* [ ] **Suíte de Testes:** Mínimo de 3 testes (Smoke, Schema e API).

### **📄 Etapa 4: Documentação & Vídeo**
* [ ] **Model Card:** Detalhamento de limitações, vieses e cenários de falha.  
* [ ] **Plano de Monitoramento:** Playbook de resposta a incidentes.  
* [ ] **Vídeo STAR:** Apresentação de exatamente 5 minutos.

## **5\. Critérios de Avaliação (Foco Total)**
1. **Qualidade de Código (20%):** Modularidade e SOLID.
2. **Rede Neural (25%):** MLP funcional com Early Stopping.
3. **Pipeline (15%):** Reprodutibilidade e `pyproject.toml`.
4. **API (15%):** FastAPI com logs e Pydantic.
5. **Doc/Vídeo (25%):** Model Card, README e Método STAR.

**Dica do Mentor:** O foco agora é a **Etapa 2**. Certifique-se de que o loop de treinamento da MLP registre o progresso no MLflow para facilitar a comparação final.
