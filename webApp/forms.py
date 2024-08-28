from django import forms
from .models import Applicant
from django.forms import ModelForm

class MyForm(ModelForm):
    class Meta:
        model = Applicant
        fields = '__all__'

class ApplicantForm(forms.Form):
    first_name = forms.CharField(
        max_length=20,
        label='First Name',
        widget=forms.TextInput(
            attrs={'class': 'form-control',}
        )
    )
    last_name = forms.CharField(
        max_length=20,
        label='Last Name',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    age = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control'}
        ),
        min_value = 0
    )
