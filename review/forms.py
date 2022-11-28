from django import forms
from .models import *
from django.forms import ClearableFileInput


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "title",
            "content",
            "genre"
            # 날짜??? 넣어야하려나..,
        ]


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ("image",)
        widgets = {
            "image": ClearableFileInput(attrs={"multiple": True}),
        }


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "댓글을 작성해주세요.",
            }
        ),
    )

    class Meta:
        model = Comment
        fields = [
            "content",
        ]
