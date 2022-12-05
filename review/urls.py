from django.urls import path
from . import views

app_name = "review"

urlpatterns = [
    path("", views.pro_index, name="pro_index"),
    path("index/", views.index, name="index"),
    path("genre/", views.genre, name="genre"),
    path("create/", views.create, name="create"),
    path("detail/", views.detail, name="detail"),
    path("matching/", views.matching, name="matching"),
    path("like_users/", views.like_users, name="like_users"),
]
