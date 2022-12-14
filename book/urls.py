from django.urls import path
from . import views

app_name = "book"

urlpatterns = [
    path("create/", views.create, name="create"),
    path("delete/<int:book_pk>", views.delete, name="delete"),
    path("book_list/<int:pk>", views.book_list, name="book_list"),
    path("update/<int:book_pk>", views.update, name="update"),
]
