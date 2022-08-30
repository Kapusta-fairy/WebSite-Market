from django import forms
from market.settings import PRODUCT_QUANTITY_CHOICES


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=[(i, str(i)) for i in range(1, PRODUCT_QUANTITY_CHOICES + 1)],
                                      coerce=int,
                                      widget=forms.Select(attrs={'class': 'form-control'}),
                                      label='Количество')
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
