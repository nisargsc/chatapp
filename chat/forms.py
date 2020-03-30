from django import forms
from .models import Message


class ChatInputForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content', 'to_whom', 'from_whom']