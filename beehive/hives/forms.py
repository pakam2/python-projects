from django import forms
from django.forms import ModelForm
from hives.models import HiveModel, HiveDataModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class AddHiveForm(ModelForm):
    class Meta:
        model = HiveModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AddHiveForm,self).__init__(*args, **kwargs)
        self.fields['numberOfHive'].widget = forms.NumberInput(attrs={'step':1, 'min':1})

class HiveDataForm(ModelForm):

    class Meta:
        model = HiveDataModel
        exclude = ['hive']


    #Making the 'max' value of the fileds equal to 1
    def __init__(self, *args, **kwargs):
        super(HiveDataForm, self).__init__(*args, **kwargs)
        self.fields['firstFrame'].widget = forms.NumberInput(attrs={'step': 0.01, 'min': 0.01, 'max': 1})
        self.fields['secondFrame'].widget = forms.NumberInput(attrs={'step': 0.01, 'min': 0.01, 'max': 1})
        self.fields['thirdFrame'].widget = forms.NumberInput(attrs={'step': 0.01, 'min': 0.01, 'max': 1})


class SignInForm(forms.Form):

    login = forms.CharField(label="Login" ,widget=forms.TextInput(attrs={'class' : 'inputField', 'placeholder' : 'Twój login', 'autocomplete' : 'nope'}))
    password = forms.CharField(label="Hasło" ,widget=forms.PasswordInput(attrs={'class': 'inputField', 'placeholder' : 'Twoje hasło', 'autocomplete' : 'nope'}))

class MySignUpForm(UserCreationForm):
        
        username = forms.CharField(max_length=150, required=True, label='Username', widget=forms.TextInput(attrs={'class' : 'inputField', 'placeholder' : 'Required'}))
        first_name = forms.CharField(max_length=30, required=False, label='First Name', widget=forms.TextInput(attrs={'class' : 'inputField', 'placeholder' : 'Optional'}))
        last_name = forms.CharField(max_length=30, required=False, label="Last Name", widget=forms.TextInput(attrs={'class' : 'inputField', 'placeholder' : 'Optional'}))
        email = forms.EmailField(max_length=254, required=True, label='Email', widget=forms.EmailInput(attrs={'class' : 'inputField', 'placeholder' : 'Required'}))
        password1 = forms.CharField(label='Password', required=True, widget=forms.PasswordInput(attrs={'class' : 'inputField', 'placeholder' : 'At least 8 chars, number & special'}), help_text='')
        password2 = forms.CharField(label='Confirm', required=True, widget=forms.PasswordInput(attrs={'class' : 'inputField', 'placeholder' : 'Confirm your password'}), help_text='')
        class Meta:
            model = User
            fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
