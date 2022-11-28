from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.pro_index, name="pro_index"),
    path("index/", views.index, name="index"),
    # path("create/", views.create, name="create"),
    # path("detail/", views.detail, name="detail"),
]
