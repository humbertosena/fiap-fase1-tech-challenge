# Registro de Mudanças Técnicas - Etapa 3

Este documento detalha todas as alterações realizadas no código e na estrutura de arquivos para cumprir os requisitos de **Engenharia, API e Qualidade**.

---

## 🏗️ 1. Arquivos Criados

| Arquivo | Descrição |
| :--- | :--- |
| `src/schemas/churn_schema.py` | Definição de contratos de dados usando **Pandera** (DataFrameSchema) e **Pydantic** (BaseModel). |
| `src/models/predict_model.py` | Implementação da arquitetura da rede neural (**MLP**) e do wrapper de inferência (**ChurnModelWrapper**). |
| `tests/conftest.py` | Configuração de fixtures do Pytest, incluindo o cliente de teste FastAPI e payloads válidos. |
| `tests/test_api.py` | Testes de integração para validar endpoints (`/predict`, `/health`, `/version`) e respostas HTTP. |
| `tests/test_schemas.py` | Testes unitários para validar as regras de negócio nos schemas Pandera. |
| `.plan/check_etapa_3.md` | Relatório de avaliação crítica e conformidade com o enunciado do Tech Challenge. |

---

## 🛠️ 2. Arquivos Modificados

### `src/features/build_features.py`
*   **Adição:** Importação dos schemas `raw_churn_schema` e `processed_churn_schema`.
*   **Adição:** Chamada do método `.validate()` no início e no fim da função `engineer_features`.
*   **Melhoria:** Tratamento de valores nulos em `TotalCharges` via `.fillna(0)` para garantir estabilidade.

### `src/api/main.py`
*   **Refatoração:** Substituição do esqueleto básico por uma API funcional.
*   **Integração:** Adição do evento `@app.on_event("startup")` para carregar o modelo PyTorch na memória.
*   **Funcionalidade:** Implementação real dos endpoints `/predict`, `/health` e `/version`.
*   **Logging:** Inclusão de logs estruturados para monitoramento de latência e resultados.

### `README.md`
*   **Atualização:** Instruções detalhadas de instalação (`make install`), teste (`make test`) e execução (`make run-api`).
*   **Documentação:** Adição de links para a documentação Swagger e detalhes sobre o pipeline Pandera.

### `docs/memoria_desenvolvimento.md`
*   **Registro:** Adição da seção **[Iteração v0.3]**, documentando cronologicamente as atividades da Etapa 3.

### `src/schemas/churn_schema.py` (Ajuste Pós-Teste)
*   **Correção:** Alteração da coluna `Churn` no `processed_churn_schema` para `required=False`.
*   **Motivo:** Permitir que o mesmo schema valide dados durante a inferência (onde o rótulo Churn não existe).

---

## 🧹 3. Qualidade e Formatação
*   **Ruff:** Aplicação de `ruff check --fix` e `ruff format` em todos os arquivos modificados.
*   **Conformidade:** Ajuste de docstrings e remoção de imports não utilizados para atingir a nota máxima em "Qualidade de Código".

---
**Data do Registro:** 02 de maio de 2026  
**Responsável:** Senior ML Engineer
