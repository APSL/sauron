import os
import channels.asgi

os.environ.setdefault('DJANGO_CONFIGURATION', 'Base')
channel_layer = channels.asgi.get_channel_layer()
