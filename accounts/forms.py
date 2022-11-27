from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "nickname", "password1", "password2"]
        labels = {
            "nickname": "닉네임",
        }
