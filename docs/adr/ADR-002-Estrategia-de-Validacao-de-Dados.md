# ADR-002: Estratégia de Validação de Dados e Qualidade de Entrada

## Status
Aceito

## Data
02/05/2026

## Contexto
Em sistemas de ML, falhas silenciosas de dados ("Silent Data Corruption") podem levar a predições erradas sem que o sistema dispare erros de código. Precisamos de uma camada técnica de proteção na entrada do pipeline e da API para garantir que apenas dados corretos sejam processados.

## Decisão
Implementar a biblioteca **Pandera** para validação de DataFrames e **Pydantic** para validação de payloads JSON.

## Consequências
- **Robustez:** O pipeline de features (`build_features.py`) agora valida o schema antes e depois do processamento.
- **Previsibilidade:** Garantimos que colunas como `tenure` e `MonthlyCharges` nunca sejam negativas.
- **Simetria:** O mesmo contrato de dados definido no treinamento é aplicado na inferência da API.
