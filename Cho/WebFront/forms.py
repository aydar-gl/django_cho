from django import forms
from .models import Order, Station

class Adding(forms.Form):
    pass

class BuyForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('client_name', 'client_number', 'client_mail', 'station')
