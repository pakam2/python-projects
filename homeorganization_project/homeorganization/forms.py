from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=64)
    password = forms.CharField(widget=forms.PasswordInput)
