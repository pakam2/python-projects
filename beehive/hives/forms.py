from django import forms
from django.forms import ModelForm
from hives.models import HiveModel

class AddHiveForm(ModelForm):
    class Meta:
        model = HiveModel
        fields = '__all__'
