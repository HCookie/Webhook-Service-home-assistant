# Webhook Service Provider for Home Assistant 
### Looking for contributions 

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs) <br/>
<img src="Images/Icon.png" alt="Icon" style="width:200px;" />

Service provider that allows Home Assistant to utilise Webhooks in automations or service calls, initially designed for use with Discord Webhooks

## Setup
### HACS

The repository folder structure is compatible with [HACS](https://hacs.xyz)

Install HACS via: https://hacs.xyz/docs/installation/manual.
Once installed, select custom repositories, and copy in the address to this `https://github.com/HCookie/Webhook-Service-home-assistant`

### Manual Setup
Copy all the files in `custom_components\webhook_service` to `custom_components\webhook_service` in your HomeAssistant.

## Configuration
Simply add `webhook_service:` to your configuration.yaml file

### Or

To add the **Webhook Service** integration to your Home Assistant, use this My button:

<a href="https://my.home-assistant.io/redirect/config_flow_start?domain=webhook_service" class="my badge" target="_blank"><img src="https://my.home-assistant.io/badges/config_flow_start.svg"></a>

<details><summary style="list-style: none"><h3><b style="cursor: pointer">Manual configuration steps</b></h3></summary>

If the above My button doesn’t work, you can also perform the following steps manually:

- Browse to your Home Assistant instance.

- Go to [Settings > Devices & Services](https://my.home-assistant.io/redirect/integrations/).

- In the bottom right corner, select the [Add Integration button.](https://my.home-assistant.io/redirect/config_flow_start?domain=webhook_service)

- From the list, select **Webhook Service**.

- Follow the instructions on screen to complete the setup.

</details>

## Usage
Use the `webhook_service:basic_webhook` service in automations to post json data to a webhook
