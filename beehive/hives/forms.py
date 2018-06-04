from django import forms
from django.forms import ModelForm
from hives.models import HiveModel, HiveDataModel

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

    login = forms.CharField(label="Login")
    password = forms.CharField(label="Hasło" ,widget=forms.PasswordInput())


