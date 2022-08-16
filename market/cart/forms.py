from django import forms
from cart.models import Sell


class SellForm(forms.ModelForm):
    class Meta:
        model = Sell
        fields = ['payment', 'delivery']
        widgets = {
            'payment': forms.Select(attrs={'class': 'form-control'}),
            'delivery': forms.Select(attrs={'class': 'form-control'})
        }
