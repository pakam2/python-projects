from django import forms
from django.forms import ModelForm
from hives.models import HiveModel, HiveDataModel

class AddHiveForm(ModelForm):
    class Meta:
        model = HiveModel
        fields = '__all__'

class HiveDataForm(forms.Form):
    
    first_frame = forms.IntegerField(label='Pierwsza ramka', widget=forms.NumberInput(attrs={'step': 0.01, 'min':0.01, 'max':1}))
    second_frame = forms.IntegerField(label='Druga ramka', widget=forms.NumberInput(attrs={'step': 0.01, 'min':0.01, 'max':1}))
    third_frame = forms.IntegerField(label='Trzecia ramka', widget=forms.NumberInput(attrs={'step': 0.01, 'min':0.01, 'max': 1}))
    motherBee = forms.BooleanField(label='Matka pszczoła')
