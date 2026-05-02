# ADR-001: Escolha do Framework para a API de Inferência

## Status
Aceito

## Data
02/05/2026

## Contexto
O projeto exige a criação de um serviço de inferência robusto e produtivo para servir o modelo de predição de churn. Precisamos escolher entre os principais frameworks Python para APIs (Flask vs FastAPI).

## Decisão
Escolhemos o **FastAPI** como framework principal.

## Consequências
- **Performance:** O FastAPI é assíncrono por natureza, oferecendo latência superior ao Flask.
- **Validação:** Integração nativa com **Pydantic**, garantindo validação de tipos em tempo de execução sem código boilerplate extra.
- **Documentação:** Geração automática do Swagger UI (`/docs`), facilitando o teste e a integração por outros times.
- **Ecossistema:** Alinhamento com as tendências modernas de MLOps e Engenharia de Software.
