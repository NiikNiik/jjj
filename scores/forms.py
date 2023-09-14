from django import forms
from django.forms import ModelForm
from .models import User
from django.core.validators import RegexValidator
import re

class SubscriberForm(ModelForm):
    class Meta():
        model = User
        fields = ('phone_number',)
        labels =  {'phone_number': ''}
        widgets = {
            'phone_number':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Cell-Phone number'})
        }
        validators=[RegexValidator(
            regex=r'^\+?1?\d{9,15}$',  # Customize the regex pattern
            message='Enter a valid phone number.',
        )]
    
    # def clean_phone_number(self):
    #     phone_number = self.cleaned_data.get('phone_number')
    #     if phone_number