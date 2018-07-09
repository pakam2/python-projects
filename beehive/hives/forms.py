from django import forms
from django.forms import ModelForm
from hives.models import HiveModel, HiveDataModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class AddHiveForm(ModelForm):
    class Meta:
        model = HiveModel
        fields = '__all__'

    #Making the 'max' value of the field equal to 1
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
        first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
        last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
        email = forms.EmailField(max_length=254)
        password1 = forms.CharField(widget=forms.PasswordInput(), help_text='')
        class Meta:
            model = User
            fields = ('username', 'last_name', 'password1', 'password2', )
