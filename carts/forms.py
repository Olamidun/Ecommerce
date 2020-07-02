from carts.models import BillingAddress, Payment
from django import forms


class BillingAddressForm(forms.ModelForm):

    address = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'needs-validation',
            'placeholder': '1234 Main St'
        }
    ))
    apartment_address = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class': 'needs-validation',
            'placeholder': 'Apartment or suite'
        }
    ))
    country = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'needs-validation',
            'placeholder': 'e.g: Nigeria'
        }
    ))
    state = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'needs-validation',
            'placeholder': 'e.g: Oyo'
        }
    ))

    class Meta:
        model = BillingAddress
        fields = ('address', 'apartment_address', 'country', 'state')


class PaymentForm(forms.Form):
    email = forms.EmailField()