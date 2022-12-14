from .models import *
from django import forms


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ("to_id", "title", "content")
        labels = {
            "to_id": "받는 사람",
            "title": "제목",
            "content": "내용",
        }
