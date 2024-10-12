from typing import Final

DOMAIN = "webhook_service"
DEFAULT_NAME = "Webhook Service Integration"

from .webhook_functions import functions
WEBHOOKS_DATAS: Final = [
    {
        "service": "basic_webhook",
        "function": functions.basic_webhook
    },
    {
        "service": "discord_webhook",
        "function": functions.discord_webhook
    }
]