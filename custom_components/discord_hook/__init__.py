import logging
import requests 

DOMAIN = "discord_hook"
_LOGGER = logging.getLogger(__name__)


def setup(hass, config):
    def send_message(call):
        #result = requests.post(url, json = data)
        _LOGGER.info('Received data', call.data)

    hass.services.register(DOMAIN, 'Send_on_Webhook', send_message)

    return True

"""
#for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
data = {
  "content": null,
  "embeds": [
    {
      "title": "Server Status",
      "color": 37370,
      "fields": [
        {
          "name": "Survival Server is OFFLINE",
          "value": "This is likely a problem"
        }
      ]
    }
  ],
  "username": "Server Notifications",
  "avatar_url": "https://servers.eldrest.com/assets/img/Favicon2-small.png"
}

result = requests.post(url, json = data)"""
