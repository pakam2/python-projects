from django import forms

class AddHiveForm(forms.Form):
    numberOfHive = forms.IntegerField()
    firstFrame = forms.DecimalField(max_digits=3, decimal_places=2)
    secondFrame = forms.DecimalField(max_digits=3, decimal_places=2)
    thirdFrame = forms.DecimalField(max_digits=3, decimal_places=2)
    motherBee = forms.BooleanField()
    comments = forms.CharField(max_length=500)
