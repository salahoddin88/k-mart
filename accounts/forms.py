from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserAuthenticationForm(AuthenticationForm):
    class Meta:
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input-class'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
        }

