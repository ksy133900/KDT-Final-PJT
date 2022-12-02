from django import forms
from .models import *
from django.forms import ClearableFileInput
from .widgets import starWidget


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "title",
            "content",
            "genre",
            "rating"
            # 날짜??? 넣어야하려나..,
        ]
        labels = {
            "title": "제목",
            "content": "내용",
            "genre": "장르",
            "rating": "별점을 남겨주세요",
        }
        widgets = {
            "rating": starWidget,
        }


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
