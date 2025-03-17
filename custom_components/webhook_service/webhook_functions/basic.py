import logging
import requests 
import json

_LOGGER = logging.getLogger(__name__)

def basic_webhook(call):
    data = call.data.copy()
    if "json" in data:
        jsondata = json.loads(data["json"])
    elif "jsonObj" in data:
        jsondata = data["jsonObj"]
    else:
        jsondata = {}

    auth = None
    if "username" in data and "password" in data:
        auth = (data["username"], data["password"])
    result = requests.post(data["webhook"], json = jsondata, auth = auth)
    
    _LOGGER.warning('Sending %s to %s. STATUS:%s', jsondata, data["webhook"], result.status_code)