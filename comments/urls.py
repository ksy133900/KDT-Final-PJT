from django.urls import path
from . import views

app_name = "comments"

urlpatterns = [
    path("<int:pk>/",views.comments, name="comments"),
    path("write/<int:pk>", views.comments_write, name="comments_write"),
    path("delete/<int:pk>", views.comments_delete, name="comments_delete"),
]
