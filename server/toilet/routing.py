from channels.routing import route
from .consumers import ws_connect

channel_routing = [
    route("websocket.connect", ws_connect),
]
