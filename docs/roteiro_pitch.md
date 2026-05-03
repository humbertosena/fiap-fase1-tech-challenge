# Roteiro do Pitch (Método STAR) — Tech Challenge Fase 1

**Objetivo:** Apresentação executiva e técnica da solução de Churn Prediction.
**Tempo Estimado:** 5 minutos.
**Atores:** Humberto Sena Santos & João Victor Faustino Piga Lopes.

---

## 🚀 [S] Situation (Situação) — 0:00 a 0:45
*   **Contexto:** Setor de Telecomunicações altamente competitivo.
*   **A Dor:** Churn elevado impactando a receita. Cada cliente perdido custa R$ 500 em LTV.
*   **Impacto:** R$ 35.850,00 estimados em perdas potenciais identificadas no dataset de estudo.
*   **Narrativa:** "Olá, somos Humberto e João Victor. Nossa missão neste desafio foi estancar a perda de receita de uma operadora de Telecom através de uma solução preditiva end-to-end..."

## 🎯 [T] Task (Tarefa) — 0:45 a 1:15
*   **Desafio:** Desenvolver não apenas um modelo, mas um **sistema industrial de ML**.
*   **Requisitos:** Rede Neural MLP (PyTorch), Rastreabilidade (MLflow), API funcional (FastAPI) e Robustez (Testes/Validação).

## 🛠️ [A] Action (Ação) — 1:15 a 3:45
*   **Arquitetura:** Modularização em \`src/\`, separando dados, features e modelos.
*   **Segurança de Dados:** Implementação de camadas de proteção com **Pandera** e **Pydantic** para barrar falhas silenciosas de dados.
*   **Modelagem:** Construção da \`ChurnMLP\` com camadas ReLU, Dropout e **Early Stopping**.
*   **Governança:** Comparação da tríade (Linear vs Árvore vs Neural) registrada no **MLflow**.
*   **Diferencial:** "Nossa API não é apenas um servidor; é um serviço resiliente que valida contratos de dados antes de qualquer inferência."

## 🏆 [R] Result (Resultado) — 3:45 a 5:00
*   **Performance:** Atingimos **0.912 de AUC-ROC**, superando baselines lineares e de árvore.
*   **Entregáveis:** Repositório auditável, Model Card transparente e Plano de Monitoramento preventivo.
*   **Conclusão:** "Entregamos uma solução que não apenas prevê o churn, mas garante a continuidade do negócio com governança e qualidade de engenharia."

---
## 💡 Dicas de Gravação:
1.  **Visual:** Mostre o diagrama de arquitetura (Mermaid) e o Dashboard do MLflow.
2.  **Demo:** Faça uma requisição rápida via Swagger (/docs) para mostrar a validação em tempo real.
3.  **Tom:** Mantenha um equilíbrio entre o executivo (valor de negócio) e o técnico (decisões de engenharia).
