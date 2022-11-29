from django.urls import path
from . import views


app_name = "accounts"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("<int:pk>/", views.profile, name="profile"),
    path("open_profile/", views.open_profile, name="open_profile"),# 이후에 <int:pk>넣어 주세요~
    path("<int:pk>/follow/", views.follow, name="follow"),
    path("<int:pk>/update/", views.update, name="update"),
    path("delete/", views.delete, name="delete"),  # 회원탈퇴
]
