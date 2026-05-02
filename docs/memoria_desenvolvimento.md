# Memória de Desenvolvimento - Previsão de Churn

Este documento tem como objetivo registrar cronologicamente todas as atividades, etapas e configurações realizadas no desenvolvimento do projeto (Log de Passos).

---

## [Iteração v0.2] - Etapa Inicial de EDA e Configuração - 21/04/2026

**Objetivo da Fase:** 
Preparar o repositório para a fase de experimentação (Exploratory Data Analysis), definindo a estrutura de arquivos e o gerenciamento de dependências, seguindo as diretrizes apontadas no `docs/ml_canvas.md`.

### Resumo de Atividades:

- **`feat(notebooks): criação do notebook base para EDA`**
  - **O que foi feito:** Criado o arquivo `notebooks/01_EDA_Telco_Churn.ipynb`.
  - **Detalhes:** O notebook foi inicializado com as bibliotecas padrão de ciência de dados (`pandas`, `numpy`, `matplotlib`, `seaborn`) e possui uma estrutura de markdown documentando os objetivos da análise (ex: análise demográfica, contratual e avaliação de Encoding vs Normalização).

- **`feat(docs): criação de documentação para o ambiente virtual`**
  - **O que foi feito:** Criado o arquivo `notebooks/README.md`.
  - **Detalhes:** O README detalha passo-a-passo como configurar o ambiente local focando em performance usando a ferramenta `uv`. Inclui criação do `.venv`, uso do `uv pip` para gerenciar pacotes, e configuração do `ipykernel` para integrar o ambiente virtual aos notebooks.

- **`docs(notebooks): atualização do README com métodos de execução`**
  - **O que foi feito:** Refinada a seção de execução no `README.md`.
  - **Detalhes:** Adicionadas opções claras de como rodar o ambiente:
    - **Opção A:** Integrado via extensões no VS Code (Recomendado).
    - **Opção B:** Via servidor web rodando o comando bash `jupyter notebook`.

- **`chore(deps): instalação de dependências iniciais da EDA`**
  - **O que foi feito:** Executada a primeira instalação controlada de bibliotecas no ambiente local.
  - **Detalhes:** Comandos rodados pelo terminal (`uv pip install pandas numpy matplotlib seaborn scikit-learn jupyter ipykernel`) e posterior congelamento das versões em um `requirements.txt`.

- **`feat(notebooks): adição de seção de sanidade de tipos na EDA`**
  - **O que foi feito:** Incluída a célula de Sanidade de Tipos em `notebooks/01_EDA_Telco_Churn.ipynb`.
  - **Detalhes:**
    - Conversão da coluna `TotalCharges` para numérico com coerção de erros.
    - Tratamento de NaNs em `TotalCharges` resultantes da conversão: Optou-se pela **remoção** em vez da imputação por mediana, justificando que são apenas 11 registros (clientes novos, `tenure=0`) sem histórico de cobrança, não afetando o poder de predição do modelo de forma geral.
    - Remoção da coluna `customerID`, pois a mesma é um identificador que não possui relevância estatística ou de negócio para prever o churn.

- **`feat(notebooks): análise de desbalanceamento (alvo e histórico)`**
  - **O que foi feito:** Incluída a célula de visualização de desbalanceamento em `notebooks/01_EDA_Telco_Churn.ipynb`.
  - **Detalhes:**
    - Geração de gráfico de contagem (*Count Plot*) para observar a distribuição das classes da variável alvo (`Churn`).
    - Geração de histograma para avaliar a distribuição do tempo de permanência dos clientes (`tenure`).
    - Cálculo e impressão da taxa de churn atual (%) e taxa de retenção, materializando o desbalanceamento discutido no ML Canvas.
    - **Registro de Resultados:** A análise aprofundada dos resultados desta etapa foi documentada de forma externa em: [Relatório de Análise EDA (Google Docs)](https://docs.google.com/document/d/1qXIp087bYc5XGEjAzEizzJe4EaDVfU06_7oNxYsI8uQ/edit?tab=t.0).

- **`feat(notebooks): análise bivariada (features vs target)`**
  - **O que foi feito:** Incluída a célula de análise bivariada em `notebooks/01_EDA_Telco_Churn.ipynb`.
  - **Detalhes:**
    - Geração de gráficos de barras empilhadas (*Stacked Bar Charts*) para avaliar a proporção de Churn em relação às variáveis categóricas `Contract`, `InternetService` e `PaymentMethod`.
    - Cálculo da correlação de Spearman (com respectivo *p-value* da biblioteca SciPy) entre a variável contínua `tenure` e o alvo `Churn` (mapeado para numérico), provando matematicamente a relação inversamente proporcional observada visualmente.

- **`feat(notebooks): preparação de dados via Pipeline Scikit-Learn`**
  - **O que foi feito:** Incluída a célula de preparo para os modelos baselines em `notebooks/01_EDA_Telco_Churn.ipynb`.
  - **Detalhes:**
    - Criação de um `ColumnTransformer` para tratar de forma unificada os dados estruturados.
    - Aplicação de `SimpleImputer(strategy='median')` seguido de `StandardScaler()` nas variáveis numéricas (`tenure`, `MonthlyCharges`, `TotalCharges`).
    - Aplicação de `OneHotEncoder(drop='first', handle_unknown='ignore')` nas variáveis categóricas, prevenindo multicolinearidade e garantindo que as classes minoritárias não fossem diluídas.
    - Reconstrução da matriz de saída de volta para um formato `pd.DataFrame` utilizando o método `get_feature_names_out()`, garantindo o rastreamento do nome original (e das classes de OHE) de cada coluna para a etapa de feature importance.

- **`feat(notebooks): modelo baseline de Regressão Logística integrado ao MLflow`**
  - **O que foi feito:** Incluída a célula de modelagem e experimentação inicial no `notebooks/01_EDA_Telco_Churn.ipynb`.
  - **Detalhes:**
    - Divisão dos dados em treino e teste (`train_test_split`) de forma estratificada.
    - Treinamento do modelo `LogisticRegression` com o hiperparâmetro `class_weight='balanced'` para lidar nativamente com o desbalanceamento das classes avaliado na EDA.
    - Integração completa com o pacote `mlflow`:
      - Rastreamento dos hiperparâmetros (tipo de modelo, peso de classe).
      - Extração dos coeficientes preditivos gerados e associação com as *features* criadas pelo *Pipeline*.
      - Log automático como métricas numéricas (`mlflow.log_metric()`) dos **5 atributos com maior risco** (impacto positivo no churn) e os **5 com menor risco** (impacto negativo/retenção).
      - Geração, salvamento e registro (*Artifact*) da Matriz de Confusão no MLflow para auditoria visual.
      - Log das métricas do *Classification Report* focadas na classe minoritária (F1-Score, Recall e Precision).

- **`feat(notebooks): otimização de threshold focada em custo financeiro (MLflow)`**
  - **O que foi feito:** Incluída a célula de análise financeira de decisão (Business Value) em `notebooks/01_EDA_Telco_Churn.ipynb`.
  - **Detalhes:**
    - Criação de lógica de simulação para calcular o impacto financeiro iterando o *probability threshold* do modelo Baseline de 0.1 até 0.9.
    - Incorporação dos pesos de penalidade de negócio definidos no ML Canvas: Falso Negativo (R$ 500 de LTV perdido) e Falso Positivo (R$ 50 de marketing indevido).
    - Identificação computacional do limiar exato (*Threshold Ótimo*) que minimiza o prejuízo financeiro total da operadora de telecom.
    - Criação do gráfico da Curva de Custo vs Threshold.
    - Criação de uma nova *Run* de experimento no MLflow (`Baseline_Financial_Optimization`) logando o threshold calculado, os parâmetros de custo e anexando o gráfico gerado como artefato da execução.

- **`feat(notebooks): criação de features sintéticas e exportação do dataset final`**
  - **O que foi feito:** Incluída célula final no `notebooks/01_EDA_Telco_Churn.ipynb` para engenharia de *features* e exportação dos dados estruturados.
  - **Detalhes:**
    - Criada a nova feature `Charges_per_Tenure` através da razão entre `TotalCharges` e `tenure` (utilizando função vetorial `np.where` para evitar erros de divisão por zero).
    - Geração de *Boxplot* (`seaborn.boxplot`) para avaliar visualmente o poder da nova variável em separar as classes de Churn.
    - Garantia de que a variável alvo (`Churn`) foi convertida definitivamente de categórica (`Yes/No`) para o domínio binário numérico (`1/0`).
    - Exportação física da matriz de dados completa para `data/processed/telco_final_for_mlp.csv`, estabelecendo o *checkpoint* para a próxima fase do projeto (treinamento da rede neural MLP em PyTorch).

- **`refactor(src): modularização do pipeline de pré-processamento`**
  - **O que foi feito:** Migração do pipeline desenhado no Notebook de EDA para módulos Python robustos focados em produção (`src/`).
  - **Detalhes:**
    - Criado `src/utils/seed_config.py` contendo a função `set_seeds()` (assegurando determinismo em `random`, `numpy`, SO e futuramente `torch`).
    - Criado `src/features/build_features.py` encapsulando toda a limpeza, a Feature Engineering (`Charges_per_Tenure`) e o Pipeline do Scikit-Learn. A função de preprocessamento exporta ativamente o `ColumnTransformer` via `joblib` para o arquivo `models/preprocessor.pkl`, garantindo a simetria de transformação para a API em FastAPI.
    - Criado `src/data/make_dataset.py` como script orquestrador. Ele consome os dados raw, executa o `train_test_split` (evitando Data Leakage), roda o Pipeline e exporta os dados finais em formato tabular para `data/processed/train_processed.csv` e `data/processed/test_processed.csv`.

---

## [Iteração v0.3] - Etapa 3: Engenharia, API e Qualidade - 02/05/2026

**Objetivo da Fase:** 
Transformar o projeto em um serviço produtivo e robusto, implementando contratos de dados, uma API de inferência e uma suíte de testes automatizados, conforme as exigências de "Engenharia de Machine Learning".

### Resumo de Atividades:

- **`feat(schemas): implementação de contratos de dados com Pandera e Pydantic`**
  - **O que foi feito:** Criado o arquivo `src/schemas/churn_schema.py`.
  - **Detalhes:** 
    - Definido `raw_churn_schema` (Pandera) para validar o dataset IBM Telco na entrada do pipeline.
    - Definido `processed_churn_schema` (Pandera) para garantir a integridade das features após o processamento.
    - Definido `ChurnRequest` (Pydantic) para validação de tipos e documentação automática (Swagger) na API.

- **`refactor(features): integração de validação no pipeline de features`**
  - **O que foi feito:** Atualizado o módulo `src/features/build_features.py`.
  - **Detalhes:** A função `engineer_features` agora valida os dados via Pandera tanto na entrada quanto na saída, prevenindo falhas silenciosas e garantindo que o modelo nunca processe dados fora da especificação.

- **`feat(models): criação do núcleo de inferência para PyTorch`**
  - **O que foi feito:** Criado o arquivo `src/models/predict_model.py`.
  - **Detalhes:** 
    - Implementada a classe `ChurnMLP` com arquitetura baseada nos requisitos da Etapa 2.
    - Criado o wrapper `ChurnModelWrapper` que carrega o `preprocessor.pkl` e os pesos do modelo (`.pth`).
    - Implementada a lógica de inferência end-to-end (JSON -> Features -> Tensores -> Predição).

- **`feat(api): desenvolvimento da API de Inferência com FastAPI`**
  - **O que foi feito:** Refatoração completa de `src/api/main.py`.
  - **Detalhes:** 
    - Implementados endpoints: `/predict` (POST), `/health` (GET) e `/version` (GET).
    - Configurado o evento `startup` para carregar os modelos na memória apenas uma vez.
    - Integrado o sistema de logging para rastrear latência e resultados das predições.

- **`test(quality): criação da suíte de testes automatizados com Pytest`**
  - **O que foi feito:** Criação da pasta `tests/` e arquivos de teste.
  - **Detalhes:** 
    - `tests/conftest.py`: Definição de fixtures para o `TestClient` e payloads.
    - `tests/test_api.py`: Testes de integração para validar o comportamento dos endpoints e a rejeição de payloads inválidos.
    - `tests/test_schemas.py`: Testes unitários para garantir que as regras de validação do Pandera estão funcionando.

- **`chore(quality): conformidade e linting`**
  - **O que foi feito:** Ajustes de estilo e formatação em todo o código `src/` e `tests/`.
  - **Detalhes:** Uso rigoroso do `ruff check --fix` e `ruff format` para garantir conformidade com os critérios de avaliação de "Qualidade de Código" (20% da nota).

---

## [Ajuste Emergencial] - Finalização das Pendências da Etapa 2 - 02/05/2026

**Objetivo:** Garantir a nota máxima sanando as lacunas de modelagem identificadas.

### Atividades Realizadas:

- **`feat(models): implementação do script de treinamento train_model.py`**
  - **O que foi feito:** Desenvolvido o motor de treinamento completo em PyTorch.
  - **Detalhes:** 
    - Implementado loop de treinamento com mini-batch SGD via `DataLoader`.
    - Adicionada classe `EarlyStopping` para monitorar a perda de validação.
    - Integrado ao **MLflow** para rastreamento de métricas por época e registro final do modelo.
- **`feat(automation): automação do fluxo de treinamento`**
  - **O que foi feito:** Atualizado o `Makefile` com o comando `make train`.
  - **Detalhes:** Agora o pipeline completo pode ser executado via comandos de terminal, garantindo a pontuação no critério de "Reprodutibilidade".
- **`docs(readme): documentação do ciclo de vida do modelo`**
  - **O que foi feito:** Atualizado o `README.md` principal com as seções de treinamento e visualização no MLflow.

---

## [Auditoria de Conformidade] - Alinhamento com Textbook de ML - 02/05/2026

**Objetivo:** Avaliar se o projeto atende aos padrões de excelência em documentação e governança de Machine Learning definidos em `@.plan/textbook.md`.

### Resultado da Auditoria:

- **Infraestrutura Cognitiva (Cap. 01):** ✅ **Aprovado.**
  - O projeto evita o conhecimento tácito ao centralizar planos, mudanças e auditorias na pasta `.plan/` e nesta memória. O sistema é legível e auditável por terceiros.
- **Prevenção do "Funciona na minha máquina" (Cap. 01 & 03):** ✅ **Aprovado.**
  - Implementação rigorosa de `uv` e `Makefile`. A reprodutibilidade é garantida por comandos de terminal únicos, eliminando fricção na configuração do ambiente.
- **MLflow como Diário Científico (Cap. 05):** ✅ **Aprovado.**
  - O treinamento modularizado em `src/models/train_model.py` registra hiperparâmetros e métricas por época, transformando dados brutos de execução em registro científico vivo.
- **Gatekeeping contra Falhas Silenciosas (Cap. 01):** ✅ **Aprovado.**
  - O uso de **Pandera** e **Pydantic** cria uma barreira de segurança que impede que o modelo tome decisões sobre dados corrompidos ou fora da distribuição esperada.

### Oportunidades Identificadas para a Etapa 4:
1.  **Transposição da Análise Financeira:** Integrar a análise de custo (R$ 500 FN / R$ 50 FP) no Model Card para justificar thresholds de decisão.
2.  **Identidade Visual Técnica:** Utilizar diagramas **Mermaid** para documentar o fluxo de sequência da API e o pipeline de dados no README final.
3.  **Honestidade de Modelo:** Detalhar limitações (out-of-scope) baseadas nas características do dataset Telco.

---

## [Fase de Polimento] - Elevação para Nível de Excelência - 02/05/2026

**Objetivo:** Eliminar lacunas de comparação técnica e formalizar decisões de arquitetura conforme orientações da coordenação.

### Atividades Realizadas:

- **`feat(models): implementação de benchmark de árvore (Random Forest)`**
  - **O que foi feito:** Criado o script `src/models/benchmark_tree.py`.
  - **Detalhes:** Treinada uma Random Forest com pesos balanceados, completando a tríade exigida: Linear (LogReg) vs Árvore (RF) vs Neural (MLP).
- **`feat(docs): formalização de Architecture Decision Records (ADRs)`**
  - **O que foi feito:** Criado o diretório `docs/adr/` com os registros ADR-001 e ADR-002.
  - **Detalhes:** Documentadas as decisões sobre a escolha do FastAPI e a estratégia de gatekeeping com Pandera/Pydantic.
- **`feat(docs): criação do Plano de Monitoramento`**
  - **O que foi feito:** Criado `docs/plano_monitoramento.md`.
  - **Detalhes:** Definida a estratégia de detecção de Drift (PSI) e o playbook de resposta a falhas.
- **`feat(automation): automação completa do pipeline de benchmark`**
  - **O que foi feito:** Atualizado o `Makefile` com `make benchmark`.
