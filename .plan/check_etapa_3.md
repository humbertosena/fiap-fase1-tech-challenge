# Checklist de Avaliação Técnica - Etapa 3

Este documento apresenta uma avaliação crítica do progresso do projeto frente aos requisitos do **Tech Challenge (Fase 1)** da FIAP.

## 📊 1. Conformidade com as Etapas

| Etapa | Requisito | Status | Observação |
| :--- | :--- | :---: | :--- |
| **Etapa 1** | ML Canvas preenchido | ✅ | Disponível em `docs/ml_canvas.md`. |
| **Etapa 1** | EDA Completa | ✅ | Implementada em `notebooks/01_eda_churn.ipynb`. |
| **Etapa 1** | Baselines (Dummy/LogReg) | ✅ | Registrados no MLflow via notebook. |
| **Etapa 2** | Arquitetura MLP (PyTorch) | ✅ | Definida em `src/models/predict_model.py`. |
| **Etapa 2** | Loop de Treino & Early Stopping | ⚠️ | **Pendente**: O loop de treino modularizado ainda não foi implementado no `src/`. |
| **Etapa 2** | Comparação MLP vs Baselines | ⚠️ | **Pendente**: Necessário após a execução do treino da MLP. |
| **Etapa 3** | Estrutura de Pastas | ✅ | Seguindo o padrão `src/`, `data/`, `models/`, etc. |
| **Etapa 3** | Pipeline Reprodutível | ✅ | `make_dataset.py` e `build_features.py` funcionais. |
| **Etapa 3** | Validação Pandera | ✅ | Integrada no pipeline de features e schemas. |
| **Etapa 3** | API FastAPI (Predict/Health) | ✅ | Implementada com Pydantic e Logging. |
| **Etapa 3** | Testes Automatizados | ✅ | 7 testes (API, Schema, Smoke) passando via Pytest. |
| **Etapa 3** | Qualidade de Código (Ruff) | ✅ | Linter validado e sem erros. |

---

## 🛠️ 2. Avaliação Crítica

### Pontos Fortes:
*   **Engenharia de Software:** O projeto apresenta um nível de maturidade elevado em termos de modularidade e separação de preocupações (SOLID).
*   **Robustez:** A inclusão do Pandera protege o modelo contra "Data Drift" e "Schema Violation" logo na ingestão.
*   **API Profissional:** O uso de FastAPI com eventos de startup e logging estruturado facilita a operação em produção.

### Lacunas Identificadas:
*   **Treinamento da MLP:** Embora a arquitetura e a inferência estejam prontas, o script de **treinamento formal** (Etapa 2) no diretório `src/` ainda não foi consolidado. O modelo na API está rodando com pesos aleatórios ou aviso de ausência de pesos.
*   **Comparação Formal:** Falta o artefato (Model Card ou Log no MLflow) comparando explicitamente a MLP contra a Regressão Logística em pelo menos 4 métricas.

---

## 🚀 3. Reprodutibilidade e CI/CD

O projeto é **altamente reprodutível** devido ao uso do `uv` e do `Makefile`. No entanto, para ser considerado "Pronto para CI/CD" no GitHub:

1.  **Workflow de Testes:** É necessário criar um arquivo `.github/workflows/ci.yml` que execute `make lint` e `make test` automaticamente em cada Pull Request.
2.  **Gestão de Artefatos:** Atualmente, artefatos como `preprocessor.pkl` e `model.pth` são locais. Em uma CI/CD real, estes deveriam ser baixados do MLflow Model Registry ou salvos via Git LFS.
3.  **Ambiente:** O uso do `uv sync` no Makefile garante que o ambiente de CI seja idêntico ao de desenvolvimento.

---

## 🏁 4. Veredito e Próximos Passos

O projeto cumpre **~85% dos requisitos técnicos** da Etapa 3. O foco imediato deve ser a **finalização da Etapa 2 (Treino da MLP)** para que a API sirva um modelo real e validado.

**Próxima Ação Sugerida:** Implementar `src/models/train_model.py` com o loop de treino PyTorch e Early Stopping.
