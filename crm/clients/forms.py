from django import forms
from .models import Client

# What this means is that i am using normal form.Form


class ClientForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)

# Here I want to inherit the fields from my model that I have created


class ClientModelForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = (
            'first_name',
            'last_name',
            'age',
            'agent'
        )