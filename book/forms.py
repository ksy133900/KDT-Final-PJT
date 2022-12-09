from django import forms
from .models import *
from django.forms import ClearableFileInput


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "price",
            "summary",
            "matching_count",
        ]


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["image"]
        widgets = {"image": forms.ClearableFileInput(attrs={"multiple": True})}
