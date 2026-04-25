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

- **`docs(plan): criação do guia de execução para a etapa 1`**
  - **O que foi feito:** Criado o arquivo `.plan/Guia de Execução Etapa 1 - EDA & Baseline.md`.
  - **Detalhes:** O documento serve como roteiro técnico para a reprodução dos resultados da Etapa 1 e prepara o terreno para a Fase 2 (Deep Learning).

---

## [Iteração v0.3] - Modelagem MLP & MLOps - 25/04/2026

**Objetivo da Fase:** 
Implementar uma rede neural MLP em PyTorch para previsão de churn, integrando o fluxo de treinamento com o MLflow para rastreabilidade e governança.

### Resumo de Atividades:

- **`chore(mlops): centralização do backend store do MLflow`**
  - **O que foi feito:** Movimentação do arquivo `mlflow.db` da pasta `notebooks/` para a raiz do projeto.
  - **Detalhes:** 
    - A mudança visa centralizar a governança de experimentos, permitindo que tanto notebooks quanto scripts de treino (`src/models/`) compartilhem a mesma base de dados via URI `sqlite:///mlflow.db`.
    - Atualização do controle de versão para rastrear o banco de dados na nova localização.
    - Encerrados processos zumbis que travavam o arquivo durante a migração.

- **`feat(models): implementação da classe ChurnDataset (PyTorch)`**
  - **O que foi feito:** Criado o arquivo `src/models/dataset.py`.
  - **Detalhes:** 
    - Implementada a classe `ChurnDataset` herdando de `torch.utils.data.Dataset`.
    - Garantida a conversão automática dos dados processados (31 features) para tensores de ponto flutuante.
    - Adicionada função auxiliar `get_dataloader` para abstrair o gerenciamento de batches e embaralhamento (shuffle).
    - Validação técnica realizada com sucesso, confirmando o carregamento de 5.625 amostras de treino.

- **`feat(models): definição da arquitetura ChurnMLP (PyTorch)`**
  - **O que foi feito:** Criado o arquivo `src/models/network.py`.
  - **Detalhes:** 
    - Implementada rede neural MLP com 3 camadas lineares.
    - Configuração: 31 neurônios de entrada, camadas ocultas de 16 e 8 (ReLU) e camada de saída única.
    - Dropout de 0.2 aplicado entre camadas ocultas para mitigar overfitting, conforme boas práticas de Deep Learning.
    - Estrutura preparada para uso com a função de perda `BCEWithLogitsLoss`.

