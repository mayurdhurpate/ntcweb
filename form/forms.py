from django import forms
from django.forms import ModelForm
from form.models import *

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class InstituteForm(ModelForm):
    class Meta:
        model = Institute
        fields = ['name', 'address', 'city', 'district', 'state',\
        'course', 'talk', 'venue', 'other']
        
