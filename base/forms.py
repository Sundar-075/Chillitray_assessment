from django import forms
from django.forms import fields

from .models import User


class UserRegForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'passowrd')
