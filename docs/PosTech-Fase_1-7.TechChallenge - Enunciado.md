# Tech Challenge - Rede Neural para Previsão de Churn

**Pós Tech - Atividade em Grupo Obrigatória Avaliada**

O objetivo deste desafio é construir um projeto **End-to-End** de uma rede neural para prever a rotatividade (churn) de clientes de uma operadora de telecomunicações, aplicando boas práticas de engenharia de Machine Learning.

## Entregas Obrigatórias

- [cite_start]**Repositório GitHub:** Código organizado e versionado[cite: 6, 15].
- [cite_start]**Vídeo de 5 minutos:** Apresentação utilizando o **método STAR** (Situation, Task, Action, Result)[cite: 6, 21].
- [cite_start]**Opcional:** Deploy da solução em nuvem (AWS, Azure ou GCP)[cite: 7].

---

## 🛠️ Requisitos Técnicos e Bibliotecas

- [cite_start]**Linguagem/Framework Core:** PyTorch para construção da rede neural (MLP)[cite: 13, 28].
- [cite_start]**Baseline:** Scikit-Learn para modelos iniciais e pipelines de pré-processamento[cite: 29, 30].
- [cite_start]**Tracking:** MLflow para rastreamento de experimentos, métricas e artefatos[cite: 31].
- [cite_start]**Serventia (API):** FastAPI para inferência do modelo[cite: 32].
- [cite_start]**Qualidade de Código:** \* `pyproject.toml` como fonte única de dependências[cite: 17].
  - [cite_start]Linting com **Ruff** (sem erros)[cite: 39].
  - [cite_start]Testes automatizados (mínimo 3: smoke, schema e API) usando **Pytest**[cite: 37, 57].
  - [cite_start]Logging estruturado (evitar o uso de `print()`)[cite: 38].

---

## 🚀 Etapas de Desenvolvimento

### Etapa 1: Entendimento e Preparação

[cite_start]Foco na formulação do problema e análise exploratória[cite: 41, 42].

- [cite_start]Preencher o **ML Canvas**[cite: 44].
- [cite_start]Realizar **EDA completa** (volume, qualidade, distribuição)[cite: 46].
- [cite_start]Definir métricas técnicas (AUC-ROC, F1) e de negócio (custo do churn)[cite: 46].
- [cite_start]Treinar baselines (DummyClassifier e Regressão Logística) e registrar no MLflow[cite: 46].

### Etapa 2: Modelagem com Redes Neurais

[cite_start]Construção e avaliação da MLP com PyTorch[cite: 48, 49].

- [cite_start]Definir arquitetura, função de ativação e loss function[cite: 50].
- [cite_start]Implementar loop de treinamento com **early stopping** e batching[cite: 50].
- [cite_start]Comparar a MLP contra os baselines usando pelo menos 4 métricas[cite: 50].

### Etapa 3: Engenharia e API

[cite_start]Refatoração profissional e criação do serviço de inferência[cite: 55, 56].

- [cite_start]Organizar o código na estrutura: `src/`, `data/`, `models/`, `tests/`, `notebooks/`, `docs/`[cite: 16].
- [cite_start]Criar pipelines reprodutíveis e validação de dados com **Pandera**[cite: 57].
- [cite_start]Construir endpoints na FastAPI (`/predict`, `/health`) com validação **Pydantic**[cite: 57].

### Etapa 4: Documentação e Finalização

[cite_start]Consolidação e apresentação[cite: 59, 60].

- [cite_start]Gerar **Model Card** detalhando limitações, vieses e cenários de falha[cite: 36, 61].
- [cite_start]Criar plano de monitoramento e playbook de resposta[cite: 61].
- [cite_start]Finalizar o README e gravar o vídeo STAR[cite: 61, 64].

---

## 📊 Critérios de Avaliação

| Critério                         | Peso | Descrição                                                             |
| :------------------------------- | :--- | :-------------------------------------------------------------------- |
| **Qualidade do Código**          | 20%  | [cite_start]Organização, modularidade e SOLID[cite: 69].              |
| **Rede Neural (PyTorch)**        | 25%  | [cite_start]MLP funcional, early stopping e comparação[cite: 69].     |
| **Pipeline e Reprodutibilidade** | 15%  | [cite_start]Pipeline Sklearn, seeds fixas e pyproject.toml[cite: 69]. |
| **API de Inferência**            | 15%  | [cite_start]FastAPI funcional, Pydantic e logs[cite: 69].             |
| **Documentação/Model Card**      | 10%  | [cite_start]Model Card completo e README claro[cite: 69].             |
| **Vídeo STAR**                   | 10%  | [cite_start]Clareza e cumprimento do tempo de 5 min[cite: 69].        |
| **Bônus: Deploy**                | 5%   | [cite_start]API acessível via URL pública[cite: 69].                  |

---

## 📂 Dataset Sugerido

- [cite_start]**Telco Customer Churn (IBM)** ou qualquer dataset de classificação binária com pelo menos 5.000 registros e 10 colunas[cite: 71, 74].

> [cite_start]**Nota:** Em caso de dúvidas, utilize o canal oficial no Discord[cite: 82].
