from django import forms
from shop.models import Products, Payment, Delivery
from market.settings import PRODUCT_QUANTITY_CHOICES


class SaleForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'color', 'category', 'price', 'discount']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'color': forms.Select(attrs={'class': 'form-control'}),
                   'category': forms.Select(attrs={'class': 'form-control'}),
                   'price': forms.TextInput(attrs={'class': 'form-control'}),
                   'discount': forms.TextInput(attrs={'class': 'form-control'})}


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['title']
        widgets = {'title': forms.Select(attrs={'class': 'form-control'})}


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['title']
        widgets = {'title': forms.Select(attrs={'class': 'form-control'})}


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=[(i, str(i)) for i in range(1, PRODUCT_QUANTITY_CHOICES)], coerce=int,
                                      widget=forms.Select(attrs={'class': 'form-control'}))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
