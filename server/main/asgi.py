import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
os.environ.setdefault('DJANGO_CONFIGURATION', 'Base')

from asgi_redis import RedisChannelLayer

channel_layer = RedisChannelLayer(
    hosts=[("redis://redis:6379/10")],
)
