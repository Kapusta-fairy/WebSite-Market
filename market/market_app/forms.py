from django import forms
from market_app.models import Products, Payment, Delivery


class SaleForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'color', 'category', 'price', 'discount']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'discount': forms.TextInput(attrs={'class': 'form-control'})
        }


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['title']
        widgets = {
            'title': forms.Select(attrs={'class': 'form-control'})
        }


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['title']
        widgets = {
            'title': forms.Select(attrs={'class': 'form-control'})
        }
