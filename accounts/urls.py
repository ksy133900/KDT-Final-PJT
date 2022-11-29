from django.urls import path
from . import views


app_name = "accounts"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    # path("<int:pk>/", views.detail, name="detail"),
    path("profile/", views.profile, name="profile"),# 이후에 <int:pk>넣어 주세요~
    path("update/", views.update, name="update"),# 이후에 <int:pk>넣어 주세요~
]
