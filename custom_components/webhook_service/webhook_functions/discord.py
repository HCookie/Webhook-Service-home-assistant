import logging
import requests 
import json

_LOGGER = logging.getLogger(__name__)

def discord_webhook(call):
    data = call.data.copy()
    title = data.get("title", "Embed Title")
    title_url = data.get("title_url")
    description = data.get("description", "Embed Description")
    thumbnail = data.get("thumbnail")
    author = data.get("author")
    fields = data.get("fields")
    image = data.get("image")
    color = data.get("color")
    timestamp = data.get("timestamp")
    footer = data.get("footer")
    webhook_url = data.get("webhook")
    if not webhook_url:
        _LOGGER.error("No webhook URL provided.")
        return

    output_data = {
        "title": title,
        "description": description
    }

    if title_url:
        output_data["url"] = title_url
    if thumbnail:
        output_data["thumbnail"] = thumbnail
    if author:
        try:
            output_data["author"] = json.loads(str(author))
        except Exception as e:
            _LOGGER.error(e)
    if fields:
        try:
            output_data["fields"] = json.loads(str(fields))[:25]
        except Exception as e:
            _LOGGER.error(e)
    if image:
        output_data["image"] = image
    if color:
        output_data["color"] = color
    if timestamp:
        output_data["timestamp"] = timestamp
    if footer:
        output_data["footer"] = footer

    embed_data = {
        "embeds": [output_data]
    }

    result = requests.post(webhook_url, json=embed_data)
    if result.status_code == 200:
        _LOGGER.info("Embed sent successfully.")
    else:
        _LOGGER.error("Failed to send embed: %s", result.text)