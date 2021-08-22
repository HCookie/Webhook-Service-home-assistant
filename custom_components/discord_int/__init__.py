DOMAIN = "discord_int"
ATTR_NAME = "name"

DEFAULT_NAME = "Discord Webhook"

def setup(hass, config):    
    """Set up is called when Home Assistant is loading our component."""
    def handle_hello(call):        
        """Handle the service call."""        
        name = call.data.get(ATTR_NAME, DEFAULT_NAME)
        hass.states.set("discord_int.hello", name)
    
    hass.services.register(DOMAIN, "hello", handle_hello)
    
    # Return boolean to indicate that initialization was successfully.    
    return True