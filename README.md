# Webhook Service Provider for Home Assistant (abandoned 2023)
## As of 03/2023 this project is abandoned
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)
![Icon](Images/Icon.png)

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

## Usage
Use the `webhook_service:basic_webhook` service in automations to post json data to a webhook
