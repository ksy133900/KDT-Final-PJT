from django.urls import path, re_path
from django.contrib import admin
from chat.views import index
from . import views

app_name='chat'

urlpatterns = [
    path("", index, name="index"),
    path("<int:pk>/", views.room, name="room"),
    # re_path(r'^(?P<room_name>[^/]+)/$', room, name='room'),
    # path("<int:room_name>/", views.room, name="room"),
    # path("<int:pk>/find_room/", views.find_room, name="find_room"),
    # path("<int:pk>/init_room/", views.init_room, name="init_room"),
    # path("message/", views.message, name="message"),
    # path("empty/", views.message, name="message"),
    # path("", views.chatroom, name="chatroom")


]