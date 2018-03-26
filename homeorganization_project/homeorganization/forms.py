from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label="Login", max_length=64)
    password = forms.CharField(label="Hasło", widget=forms.PasswordInput)
