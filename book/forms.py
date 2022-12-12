from django import forms
from .models import *
from django.forms import ClearableFileInput


class bookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "genre",
            "price",
            "summary",
            "matching_count",
        ]
        labels = {
            "title": "책 제목",
            "genre": "장르",
            "price": "가격",
            "summary": "줄거리",
            "matching_count": "매칭 수",
        }


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["image"]

        # widgets = {"image": forms.ClearableFileInput(attrs={"multiple": True})}
