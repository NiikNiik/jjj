from django import forms
from django.forms import ModelForm
from .models import User
from django.core.validators import RegexValidator
import re
regex=r'^\+?1?\d{9,15}$'
class SubscriberForm(ModelForm):
    class Meta():
        model = User
        fields = ('phone_number',)
        labels =  {'phone_number': ''}
        widgets = {
            'phone_number':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Phone Number'})
        }
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not re.match(r'^\+?1?\d{9,15}$', phone_number):
            raise forms.ValidationError("Enter a valid phone number")
        return phone_number