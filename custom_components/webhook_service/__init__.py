import logging
import requests 
import json

DOMAIN = "webhook_service"
_LOGGER = logging.getLogger(__name__)


SERVICE_SEND = "basic_webhook"

def setup(hass, config):
    def send_basic_webhook(call):
        data = call.data.copy()
        if "json" in data:
            jsondata = json.loads(data["json"])
        else:
            jsondata = {}
        result = requests.post(data["webhook"], json = jsondata)
        _LOGGER.warn('Received data', data["webhook"])

    hass.services.register(DOMAIN, SERVICE_SEND, send_basic_webhook)

    return True
