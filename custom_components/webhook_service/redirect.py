from homeassistant.components.http import HomeAssistantView
from homeassistant.config_entries import ConfigEntry
from aiohttp import web, ClientSession
import mimetypes
import requests

from .const import DOMAIN

class ImagesRedirect(HomeAssistantView):
    requires_auth = False

    def __init__(self, config_entry: ConfigEntry | dict):
        super().__init__()
        self.name = DOMAIN
        self.url = f'/{DOMAIN}'
        self.image_mime_types = ["image/jpeg", "image/png", "image/gif", "image/webp", "image/bmp", "image/tiff"]

    async def get(self, request):
        path = request.query.get("path", "")

        if not path:
            return web.HTTPBadRequest(text="Path is required.")

        mime_type, _ = mimetypes.guess_type(path)
        if mime_type not in self.image_mime_types:
            return web.HTTPBadRequest(text=f'The requested file is not an image. File path: {path}')

        try:
            with open(path, "rb") as f:
                content = f.read()
            return web.Response(body=content, content_type=mime_type)
        except Exception as e:
            return web.HTTPInternalServerError(text=f"Error reading the file: {str(e)}")
