from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


inputAttrs = {
    'class': "form-control"
}

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class NewClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'client_name': forms.TextInput(attrs=inputAttrs),
            'info': forms.Textarea(attrs={"class": "form-control", "rows": 5}),

        }


class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['model_code', 'type', 'description', 'photo', 'is_available', 'MW', 'color', 'year', 'age', 'material']
        widgets = {
            'model_code': forms.TextInput(attrs=inputAttrs),
            'type': forms.TextInput(attrs=inputAttrs),
            'description': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
        }


class NewOrderForm(forms.ModelForm):
    class Meta:
        model = Order

        fields = ['model_code', 'client_name', 'price', 'quantity', 'debt']
        widgets = {
            'price': forms.NumberInput(attrs=inputAttrs),
            'quantity': forms.NumberInput(attrs=inputAttrs),
            'debt': forms.NumberInput(attrs=inputAttrs),

        }