import logging
import requests 
import json

from .. import const

_LOGGER = logging.getLogger(__name__)

def run(hass, call, thumbnail_file=None, thumbnail_name=None, image_file=None, image_name=None):
    data = call.data.copy()
    title = data.get("title", "Embed Title")
    title_url = data.get("title_url")
    description = data.get("description", "Embed Description")
    
    author = data.get("author")
    fields = data.get("fields")
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
    if color:
        output_data["color"] = color
    if timestamp:
        output_data["timestamp"] = timestamp
    if footer:
        output_data["footer"] = footer
    

    files = {}
    if image_file and image_name:
        files["file_image"] = (image_name, image_file)
        output_data["image"] = {"url": f'attachment://{image_name}'}

        
    if thumbnail_file and thumbnail_name:
        files["file_thumbnail"] = (thumbnail_name, thumbnail_file)
        output_data["thumbnail"] = {"url": f'attachment://{thumbnail_name}'}


    embed_data = {
        "embeds": [output_data]
    }

    result = requests.post(webhook_url, data={"payload_json": json.dumps(embed_data)}, files=files)

    try:
        result.raise_for_status()
        _LOGGER.info("Embed sent successfully.")
    except:
        _LOGGER.error("Failed to send embed: %s", result.text)

def discord_webhook(hass, call):
    data = call.data.copy()
    thumbnail = data.get("thumbnail")
    image = data.get("image")


    if thumbnail:
        thumbnail_name = thumbnail.split("/")[-1]
        with open(thumbnail, "rb") as thumbnail_file:
            if image:
                image_name = image.split("/")[-1]
                with open(image, "rb") as image_file:
                    run(hass, call, thumbnail_file, thumbnail_name, image_file, image_name)
            else:
                run(hass, call, thumbnail_file, thumbnail_name)



    if not thumbnail and image:
        image_name = image.split("/")[-1]
        with open(image, "rb") as image_file:
            run(hass, call, image_file=image_file, image_name=image_name)