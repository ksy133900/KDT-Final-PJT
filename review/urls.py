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
    # 글 수정
    path("update/<int:pk>", views.update, name="update"),
    # 글 삭제
    path("delete/<int:pk>", views.delete, name="delete"),
    # 리뷰카드 좋아/싫어 버튼
    # path("like_users/", views.like_users, name="like_users"),
    path("like/<int:pk>", views.like, name="like"),
]
