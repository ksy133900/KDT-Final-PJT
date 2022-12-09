from django.urls import path
from . import views

app_name = "book"

urlpatterns = [
    path("create/", views.create, name="create"),
    # path("book_list", views.book_list, name="book_list"),
]
