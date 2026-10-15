# Integração com CI/CD para Machine Learning

Projeto desenvolvido durante a Pós-Tech em Machine Learning Engineering da FIAP.

O objetivo foi aplicar conceitos de CI/CD e MLOps em um projeto de Machine Learning utilizando GitHub Actions.

## Conteúdo estudado

- Aula 1 – Conceitos de CI/CD aplicados a ML
- Aula 2 – Integração Contínua para Data Science com GitHub Actions
- Aula 3 – Pipeline CI/CD com GitHub Actions
- Aula 4 – Testes Automatizados no Pipeline de ML
- Aula 5 – Automatizando o Deploy de Modelos — Containerização
- Aula 6 – Automatizando o Deploy de Modelos — Entrega Contínua
- Aula 7 – Boas Práticas de CI/CD em ML — MLOps
- Aula 8 – Aprendizado Contínuo e Monitoramento de Modelos

## Tecnologias utilizadas

- Python
- Poetry
- Pandas
- Scikit-Learn
- FastAPI
- Pytest
- Ruff
- Docker
- GitHub Actions
- GitHub Container Registry
- AWS IAM com OIDC
- Kubernetes

## O que foi implementado

- Validação automática do ambiente;
- Análise de código com Ruff;
- Testes automatizados com Pytest;
- Preparação de dados;
- Treinamento de modelo;
- Comparação entre modelo Champion e Challenger;
- Geração de artefatos;
- Criação automática de Pull Request;
- Workflows reutilizáveis;
- GitHub Action personalizada;
- Pipeline de CI/CD;
- Build e publicação de imagem Docker;
- Integração segura com a AWS utilizando OIDC;
- Monitoramento agendado;
- Simulação de retreinamento por evento `repository_dispatch`.

## Estrutura do projeto

    .github/workflows/
    ├── ci.yaml
    ├── ci-workflow-call.yaml
    ├── cd.yaml
    ├── ml-pipeline.yaml
    └── monitoramento-diario.yaml

    k8s/
    scripts/
    src/models/
    tests/
    api.py
    Dockerfile
    pyproject.toml
    poetry.lock

## Observação

Este projeto foi desenvolvido para fins educacionais como parte das aulas de Integração com CI/CD da Pós-Tech em Machine Learning Engineering da FIAP.

Algumas etapas de infraestrutura e deploy são simuladas para demonstrar o funcionamento do fluxo de MLOps.