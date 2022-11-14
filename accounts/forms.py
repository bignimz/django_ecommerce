from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Enter Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Confirm Password'}))
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'password')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Enter Email'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Enter Phone Number'}),
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('email', 'password')
        # widgets = {
        #     'email': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        # }