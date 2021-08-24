from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class NewClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'client_name': forms.TextInput(attrs={"class": "form-input"}),
            'info': forms.Textarea(attrs={"class": "form-control", "rows": 5}),

        }


class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['model_code', 'type', 'description', 'photo', 'is_available', 'MW', 'color', 'year', 'age', 'material']
        widgets = {
            'model_code': forms.TextInput(attrs={"class": "form-input"}),
            'type': forms.TextInput(attrs={"class": "form-input"}),
            'description': forms.Textarea(attrs={"class": "form-control", "rows": 5}),

        }