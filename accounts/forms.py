from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "nickname", "age", "password1", "password2"]
        labels = {"nickname": "닉네임", "age": "나이"}

    # OperationalError at /accounts/signup/
    # no such column: accounts_user.nickname
    def signup(self, request, user):
        # form에 기입된 데이터를 가져오기 위해 cleaned_data 사용
        user.nickname = self.cleaned_data["nickname"]
        user.age = self.cleaned_data["age"]
        user.save()


class ProfileForm(ModelForm):
    class Meta:
        model = Profile()
        fields = ["intro", "image"]


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ["nickname"]
        labels = {
            "nickname": "닉네임",
        }
