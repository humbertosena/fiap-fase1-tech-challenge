# Machine Learning Canvas

**Projeto**: Previsão de Churn - Operadora de Telecom (FIAP Tech Challenge)<br/>
**Responsável**: Humberto Sena Santos<br/>
**Data**: 21/04/2026<br/>
**Iteração**: v0.1 - Design e Definição de Problema<br/>

## 1. Propostas de Valor (Value Propositions)

Reduzir a taxa de cancelamento (Churn) da operadora através da identificação proativa de clientes em risco. O objetivo é permitir que a equipe de retenção atue antes do cancelamento efetivo, preservando a receita recorrente (MRR) e aumentando o Life Time Value (LTV) do cliente.

## 2. Tarefa de ML (ML Task)

Classificação Binária.

- **Input**: Dados demográficos, serviços assinados, informações contratuais e histórico de cobrança.
- **Output**: Classe "Churn" (Sim/Não).

## 3. Fontes de Dados (Data Sources)

**Fonte**: Dataset Telco Customer Churn (IBM).<br/>
**Features**: Dados demográficos, serviços assinados (Internet, Stream, Phone), informações de contrato (Mensalidade, Tempo de Casa, Tipo de Contrato).<br/>
**Volume Sugerido**: ~7.000 registros com mais de 10 atributos.<br/>
**Link**: https://www.kaggle.com/datasets/blastchar/telco-customer-churn<br/>

## 4. Coleta de Dados (Collecting Data)

Os dados são extraídos de sistemas de CRM e Billing da operadora uma única vez, 06 de janeiro de 2019, consolidados em um arquivo tabular para processamento em batch.

## 5. Atributos (Features)

- **Demográficos**: Gênero, Senior Citizen, Parceiros.
- **Serviços**: Tipo de Internet, Segurança Online, Streaming.
- **Contratuais**: Tipo de contrato (mensal/anual), Paperless billing, Método de pagamento.

## 6. Construção de Modelos (Building Models)

Retreino mensal (Batch) utilizando PyTorch (MLP) para capturar mudanças no comportamento do consumidor. Rastreamento de experimentos via MLflow.

## 7. Decisões (Decisions)

**Ação**: Clientes com probabilidade de Churn acima de um threshold 0,70 são enviados para a régua de relacionamento de retenção (oferta de upgrades, descontos ou contato direto do CS).<br/>
**Intervenção**: Acionamento via e-mail marketing ou ligação do gerente de conta.

## 8. Realização de Predições (Making Predictions)

Predição em lote (Batch) executada mensalmente para toda a base ativa. Baixa restrição de latência (processamento overnight).

## 9. Avaliação Offline (Offline Evaluation)

**Métricas Técnicas**:

- AUC-ROC: Para avaliar a capacidade de separação das classes.
- F1-Score: Crucial devido ao desbalanceamento das classes (Churn costuma ser a classe minoritária).
- PR-AUC: Para focar na precisão/recall da classe positiva (quem cancela).
- **Baselines**: Comparação de performance contra Dummy Classifier (estratificado) e Regressão Logística para justificar a complexidade da MLP.

**Métricas de Negócio**:

- Taxa de Churn Evitado: % de clientes que foram classificados como risco e não cancelaram após intervenção.
- ROI da Campanha: (Receita Salva - Custo da Retenção) / Custo da Retenção.
- **Análise de Custo Financeiro**: Matriz de custo ponderando o impacto financeiro de Falsos Negativos (perda do LTV) vs. Falsos Positivos (custo de marketing/desconto desnecessário).

## 10. Avaliação em Tempo Real e Monitoramento (Live Evaluation and Monitoring)

Queda percentual na taxa de Churn real vs. grupo de controle (Hold-out). Monitoramento de Data Drift via MLflow/FastAPI logs.
