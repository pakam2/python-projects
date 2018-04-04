from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


WHO = (
    ('P', 'Paweł'),
    ('K', 'Kasia'),
)


class LoginForm(forms.Form):
    username = forms.CharField(label="Login", max_length=64)
    password = forms.CharField(label="Hasło", widget=forms.PasswordInput)

"""
class RepeatableExpensesForm(forms.Form):
    amount = forms.DecimalField(label="Kwota", initial="Wpisz kwotę", max_digits=6, decimal_places=2)
    type_of_expense = forms.ChoiceField(label="Rodzaj wydatku", choices = RepetableEx, required=True)
"""
class ToDoForm(forms.Form):
    text_field = forms.CharField(label="Opis zadania", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '4'}))
    whos_task = forms.ChoiceField(label="Osoba", choices=WHO, widget=forms.Select(attrs={'class':'form-control'}))
