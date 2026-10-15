import logging
import os

import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def enviar_webhook_para_github():
    logger.info("Preparando envio de Webhook para o GitHub Actions...")

    # Para interagir com a API do GitHub como uma automação externa
    # o padrão corporativo exige um Personal Access Token (PAT).
    token = os.environ.get("GITHUB_PAT")
    owner = "landidaniel"
    repo = "Integracao-ci-cd"

    # Endpoint oficial do GitHub para disparos de repositório
    url = f"https://api.github.com/repos/{owner}/{repo}/dispatches"

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }

    # O event_type deve ser igual ao configurado no workflow
    payload = {
        "event_type": "anomalia-detectada-retreinar",
        "client_payload": {
            "motivo": "Concept Drift crítico identificado na última hora.",
            "acuracia": "72%",
        },
    }

    resposta = requests.post(url, json=payload, headers=headers )

    if resposta.status_code == 204:
        logger.info(
            "✅ WEBHOOK ENVIADO: A requisição foi autenticada "
            "e a esteira de treinamento foi acordada!"
        )
    else:
        logger.error(
            "❌ FALHA DE AUTENTICAÇÃO: HTTP %s - %s",
            resposta.status_code,
            resposta.text,
        )


if __name__ == "__main__":
    enviar_webhook_para_github()