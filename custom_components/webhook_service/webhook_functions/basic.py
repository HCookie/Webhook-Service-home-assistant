import logging
import requests 
import json

_LOGGER = logging.getLogger(__name__)

def basic_webhook(call):
    data = call.data.copy()
    if "json" in data:
        jsondata = json.loads(data["json"])
    else:
        jsondata = {}
    result = requests.post(data["webhook"], json = jsondata)
    _LOGGER.warn('Received data', data["webhook"])