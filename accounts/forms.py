from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import Profile, User
from .models import Profile
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "password1",
            "password2",
            "address",
        ]
        def clean_username(self):
            username = self.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError('아이디가 이미 사용중입니다')
            return username
    # OperationalError at /accounts/signup/
    # no such column: accounts_user.nickname

    # form에 기입된 데이터를 가져오기 위해 cleaned_data 사용


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile()
        fields = [
            "intro",
            "nickname",
            "genre",
            "age",
            "ages",
            "day",
            "time",
            "image",
        ]
        labels = {
            "intro": "소개글",
            "nickname": "닉네임",
            "genre": "장르",
            "age": "나이",
            "ages": "선호 나이",
            "day": "선호 요일",
            "time": "선호 시간",
            "image": "프로필 사진",
        }
