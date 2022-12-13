from django.urls import path, re_path
from django.contrib import admin
from chat.views import index
from . import views

app_name='chat'

urlpatterns = [
    path("", index, name="index"),
    path("<int:pk>/", views.room, name="room"),

]