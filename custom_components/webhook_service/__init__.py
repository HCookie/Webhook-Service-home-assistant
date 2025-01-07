from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN, WEBHOOKS_DATAS
from .redirect import ImagesRedirect

import logging
_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the integration."""

    hass.http.register_view(ImagesRedirect(config))
    if DOMAIN not in hass.data:
        hass.data[DOMAIN] = {}
        await _setup_webhooks(hass, config)
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up the platform."""

    hass.http.register_view(ImagesRedirect(entry))
    if DOMAIN not in hass.data:
        hass.data[DOMAIN] = {}
        await _setup_webhooks(hass, entry)
    return True


async def _setup_webhooks(hass: HomeAssistant, data: dict | ConfigEntry):
    for webhook_data in WEBHOOKS_DATAS:
        if "service" in webhook_data and "function" in webhook_data:
            hass.services.async_register(DOMAIN, webhook_data["service"], lambda call: webhook_data["function"](hass, call))
            _LOGGER.info(f'{webhook_data["service"]} set up')