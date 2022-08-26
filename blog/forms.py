from dataclasses import fields
from socket import fromshare
from django import forms
from .models import Comment


class ContactForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'description']
    