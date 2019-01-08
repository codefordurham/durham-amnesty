from django import forms
from django.core.validators import RegexValidator

class StatusForm(forms.Form):
	name = forms.CharField(label='Name', max_length=100)
	date_of_birth = forms.DateField(label='Date of Birth')
	email = forms.EmailField(label='Email')
	driver_license_number=forms.CharField(label='Driver license number',max_length=10)
	