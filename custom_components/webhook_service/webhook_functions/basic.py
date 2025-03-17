import logging
import requests 
import json

_LOGGER = logging.getLogger(__name__)

def basic_webhook(hass, call):
    data = call.data.copy()
    if "json" in data:
        jsondata = json.loads(data["json"])
    elif "jsonObj" in data:
        jsondata = data["jsonObj"]
    else:
        jsondata = {}
    result = requests.post(data["webhook"], json = jsondata)
    _LOGGER.warn('Received data', data["webhook"])