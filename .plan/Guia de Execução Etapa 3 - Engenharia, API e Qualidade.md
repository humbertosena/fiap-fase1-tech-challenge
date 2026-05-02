# **🛠️ Guia de Execução: Etapa 3 \- Engenharia, API & Qualidade**

Este guia orienta a transformação do projeto em um serviço produtivo, focando em robustez via **FastAPI**, validação rigorosa com **Pandera** e uma suíte de testes automatizados.

## **📅 Cronograma Sugerido (Semana 3\)**

| Dia | Atividade | Entregável Técnico |
| :---- | :---- | :---- |
| **Dia 1** | Refatoração e Contratos de Dados | src/schemas/churn\_schema.py (Pandera) |
| **Dia 2** | Desenvolvimento da API Base | src/api/main.py (FastAPI) |
| **Dia 3** | Integração de Inferência (Predict) | Endpoint /predict com carregamento de artefatos |
| **Dia 4** | Suíte de Testes Automatizados | tests/test\_api.py e tests/test\_schemas.py |
| **Dia 5** | Validação de Logs e Versionamento | Middleware de logs e endpoint /version |

## **🚀 1\. Contratos de Dados com Pandera**

**O que fazer:** Criar esquemas de validação para os dados de entrada e saída.

**Por que:** Em sistemas de ML, o "silence failure" (falha silenciosa) é o maior perigo. O Pandera atua como um gatekeeper, garantindo que se o formato dos dados mudar na fonte, o pipeline quebre imediatamente com um erro claro em vez de gerar predições erradas.

### **Atividades:**

* Definir InputSchema com tipos (float, int) e intervalos (ex: Tenure \>= 0).  
* Implementar validação no pipeline de pré-processamento.

## **⚡ 2\. API de Inferência com FastAPI**

**O que fazer:** Implementar uma API assíncrona para servir o modelo MLP.

**Por que:** O FastAPI é o padrão atual de mercado por ser extremamente rápido e utilizar **Pydantic** nativamente, o que gera documentação automática (Swagger) e validação de tipos em tempo de execução.

### **Endpoints Obrigatórios:**

* GET /health: Verificação de integridade do serviço.  
* GET /version: Retorna a versão do modelo e da API (rastreabilidade).  
* POST /predict: Recebe o JSON do cliente e retorna a probabilidade de Churn.

## **🧪 3\. Suíte de Testes (Qualidade de Software)**

**O que fazer:** Implementar testes que garantam que mudanças no código não quebrem o modelo.

**Por que:** Conforme o enunciado da FIAP, a "Qualidade de Código" vale 20%. Testes automatizados são a prova de que seu código é modular e sustentável.

### **Tipos de Testes Necessários:**

1. **Smoke Tests:** Verificam se a API sobe e responde ao /health.  
2. **Schema Tests:** Garantem que dados inválidos (ex: MonthlyCharges negativo) sejam rejeitados pela API.  
3. **API Tests:** Simulam uma requisição completa de predição e verificam se o retorno é um float entre 0 e 1\.

## **📁 Estrutura de Arquivos da Etapa 3**

A árvore do projeto deve ser atualizada para refletir a modularização total:

├── src/  
│   ├── api/  
│   │   ├── \_\_init\_\_.py  
│   │   ├── main.py          \<-- App FastAPI  
│   │   └── routes/          \<-- Divisão de endpoints  
│   ├── schemas/  
│   │   ├── \_\_init\_\_.py  
│   │   └── churn\_schema.py   \<-- Contratos Pandera/Pydantic  
│   ├── features/  
│   │   └── build\_features.py \<-- Atualizado com validação  
│   └── models/  
│       └── predict\_model.py  \<-- Lógica de inferência PyTorch  
├── tests/  
│   ├── conftest.py  
│   ├── test\_api.py  
│   └── test\_schemas.py

## **✅ Checklist de Nota Máxima (Critérios FIAP)**

* \[ \] **Modularidade:** Nenhum código de treinamento ou inferência dentro de notebooks. Tudo em src/.  
* \[ \] **SOLID:** As classes de modelo e datasets estão isoladas de lógica de API.  
* \[ \] **FastAPI:** Documentação /docs funcional e sem erros.  
* \[ \] **Pandera:** Validação ativa tanto no treino quanto na inferência.  
* \[ \] **Logging:** A API deve logar as requisições recebidas e possíveis erros de inferência.