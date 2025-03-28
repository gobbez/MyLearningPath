from django.urls import path
from .consumers import WebchatConsumer

websocket_urlpatterns = [path("", WebchatConsumer.as_asgi())]