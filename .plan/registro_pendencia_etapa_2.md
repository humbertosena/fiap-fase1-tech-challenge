# Registro de Pendências e Impacto - Etapa 2

Este documento descreve o plano para sanar as lacunas identificadas na modelagem da Rede Neural (PyTorch) e avalia o risco para a nota final do projeto.

---

## ⚠️ 1. Avaliação de Risco para a Nota

De acordo com o enunciado, o critério **"Rede Neural (PyTorch)" possui peso de 25%** na avaliação final. A pontuação máxima neste critério exige:
1.  **MLP Funcional:** O modelo deve estar treinado e apto a fazer predições reais.
2.  **Early Stopping e Batching:** Uso de boas práticas de treinamento de Deep Learning.
3.  **Comparação:** Confronto de performance entre a MLP e os baselines (LogReg).

**Impacto:** A ausência do script de treinamento (`train_model.py`) e da comparação formal no `src/` pode resultar em uma **perda de até 20 a 25 pontos percentuais** na nota final, desqualificando o projeto para o selo de "Excelência MLOps".

---

## 📋 2. Plano de Implementação das Pendências

### Fase 1: Código de Treinamento
*   **Arquivo:** `src/models/train_model.py`
*   **Funcionalidades:**
    *   Carga dos dados processados (`train_processed.csv` e `test_processed.csv`).
    *   Uso de `DataLoader` e `TensorDataset` para batching (Mini-batch SGD).
    *   Implementação de classe `EarlyStopping` para prevenir overfitting.
    *   Loop de treinamento com log de Loss e Acurácia por época no **MLflow**.
    *   Exportação automática do melhor estado do modelo para `models/model.pth`.

### Fase 2: Automação e Documentação
*   **Makefile:** Adicionar comando `make train` para orquestrar o treinamento.
*   **README.md:** Adicionar seção "Treinamento do Modelo" com instruções de execução e visualização de métricas no MLflow.

### Fase 3: Comparação e Model Card
*   **Ação:** Gerar um log final no MLflow comparando AUC-ROC, F1-Score e Recall entre LogReg e MLP.
*   **Documentação:** Preparar os dados para o Model Card (Etapa 4).

---

## 🛠️ 3. Mudanças Previstas em Arquivos

| Arquivo | Tipo | Mudança Planejada |
| :--- | :--- | :--- |
| `src/models/train_model.py` | Novo | Script principal de treinamento PyTorch. |
| `Makefile` | Alteração | Inclusão do target `train` (`uv run python -m src.models.train_model`). |
| `README.md` | Alteração | Documentação do fluxo de treino e reprodutibilidade do modelo. |
| `models/model.pth` | Artefato | Geração do arquivo de pesos reais após o treino bem-sucedido. |

---
**Data:** 02 de maio de 2026  
**Status:** ✅ Concluído com Sucesso
