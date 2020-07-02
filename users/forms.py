from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class StoreCustomerForm(UserCreationForm):
    username = forms.CharField(max_length=20,
                               widget=forms.TextInput(
                                     attrs={
                                         'class': 'form-control mb-2',
                                         'placeholder': 'Username'
                                     }
                                 ))

    first_name = forms.CharField(max_length=20,
                                 widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control mb-2',
                                        'placeholder': 'John'
                                    }
                                 ))

    last_name = forms.CharField(max_length=20,
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control mb-2',
                                        'placeholder': 'Doe'
                                    }
                                ))

    email = forms.EmailField(widget=forms.EmailInput(
                                 attrs={
                                     'class': 'form-control mb-2',
                                     'placeholder': 'myemailaddress@gmail.com'
                                 }
                                ))
    password1 = forms.CharField(help_text=
                                '''<b>Your password can’t be too similar to your other personal information.
                                   Your password must contain at least 8 characters.
                                   Your password can’t be a commonly used password.
                                   Your password can’t be entirely numeric.</b>''',

                                widget=forms.PasswordInput(
                                    attrs={
                                        'class': 'form-control mb-2',
                                        'placeholder': 'Enter your password'
                                    }))

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Enter your password again for confirmation'
            }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
