from django.urls import re_path, path

from . import consumers

websocket_urlpatterns = [
    re_path(r"wss/chat/(?P<room>\w+)/$", consumers.ChatConsumer.as_asgi()),
    # path('ws/chat/<int:room>/', consumers.ChatConsumer.as_asgi())
]