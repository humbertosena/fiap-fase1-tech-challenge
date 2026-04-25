# Notebooks de Experimentação

Este diretório contém os notebooks utilizados para a etapa de EDA (Exploratory Data Analysis) e experimentação dos modelos do projeto de Previsão de Churn.

## Configuração do Ambiente

Para garantir a reprodutibilidade, isolamento das dependências e velocidade de instalação, recomendamos o uso do `uv` para o gerenciamento do ambiente virtual e pacotes.

### 1. Pré-requisitos

Certifique-se de ter o `uv` instalado em sua máquina. Caso não tenha, instale-o via pip (ou de acordo com as [instruções oficiais](https://github.com/astral-sh/uv)):

```bash
pip install uv
```

### 2. Criação do Ambiente Virtual

Crie um ambiente virtual na raiz do projeto utilizando o `uv`:

```bash
uv venv
```

Ative o ambiente virtual:

- **Windows**:
  ```bash
  .venv\Scripts\activate
  ```
- **Linux/macOS**:
  ```bash
  source .venv/bin/activate
  ```

### 3. Instalação Controlada das Dependências

Para a etapa de experimentação, instale os pacotes necessários utilizando o `uv pip`. Isso garante uma resolução de dependências robusta.

Se houver um arquivo `requirements.txt` ou `pyproject.toml`, execute:

```bash
uv pip install -r requirements.txt
```

_(Caso não exista, instale os pacotes base manualmente e gere o controle das dependências:)_

```bash
uv pip install pandas numpy matplotlib seaborn scikit-learn jupyter ipykernel
uv pip freeze > requirements.txt
```

### 4. Configuração do Jupyter e IPykernel

Para que o Jupyter Notebook reconheça o ambiente virtual recém-criado, é necessário registrar o kernel associado a este ambiente.

Instale o `ipykernel` (se não foi instalado no passo anterior):

```bash
uv pip install ipykernel
```

Registre o ambiente virtual como um kernel do Jupyter:

```bash
python -m ipykernel install --user --name=fiap-churn-env --display-name "Python (fiap-churn-env)"
```

### 5. Executando o Notebook

Você pode executar os notebooks de duas maneiras diferentes, dependendo da sua preferência:

#### Opção A: Via Editor (VS Code) - Recomendado

A maneira mais prática é utilizar as extensões do Jupyter diretamente no seu editor de código, aproveitando o ambiente virtual recém-criado.

1. Abra a pasta raiz do projeto (`fiap-fase1-tech-challenge`) no seu editor.
2. Certifique-se de que a extensão **Jupyter** está instalada.
3. Abra o notebook desejado, por exemplo: `notebooks/01_EDA_Telco_Churn.ipynb`.
4. No canto superior direito da aba do notebook, clique no botão de seleção de Kernel (geralmente indica **"Select Kernel"**).
5. Escolha **Python Environments** e selecione o ambiente virtual `.venv` que você criou (ou o kernel nomeado como `Python (fiap-churn-env)`).
6. Você já pode executar as células de forma integrada!

#### Opção B: Via Servidor Web (Linha de Comando)

Se você prefere a interface clássica do Jupyter diretamente no navegador:

1. No terminal, com o ambiente virtual ativado, inicie o servidor:
   ```bash
   jupyter notebook
   ```
2. O navegador abrirá automaticamente. Navegue até a pasta `notebooks/` e abra o arquivo `01_EDA_Telco_Churn.ipynb`.
3. Certifique-se de selecionar o kernel **"Python (fiap-churn-env)"** no canto superior direito (ou através do menu _Kernel > Change kernel_).

---

## 📊 Model Tracking & Git LFS

Este projeto utiliza o **MLflow** para rastreamento de experimentos. O banco de dados de metadados (`mlflow.db`) está localizado na raiz do projeto para centralização.

Para visualizar os experimentos através da interface web do MLflow, execute o seguinte comando **a partir da raiz do projeto**:

```bash
uv run mlflow ui --backend-store-uri sqlite:///mlflow.db
```

### 💾 Armazenamento do Banco de Dados (Git LFS)

O arquivo `mlflow.db` (na raiz) está configurado para ser rastreado via **Git LFS (Large File Storage)**. 

*   **Objetivo:** Preservar a integridade e o tamanho do histórico do Git, evitando que binários de bancos de dados SQLite sobrecarreguem o repositório principal.
*   **Limites do GitHub:** A conta gratuita oferece **1 GB** de armazenamento LFS, suficiente para os experimentos desta fase.

> **⚠️ Nota de Escalabilidade:** Para cenários reais de produção ou volumes de dados superiores a 1 GB, recomenda-se a migração para instâncias gerenciadas do MLflow (como no Databricks) ou a configuração de um banco de dados externo (Postgres/MySQL) e storage remoto (S3/GCS/Azure Blob).
