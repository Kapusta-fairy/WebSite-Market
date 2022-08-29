from django import forms
from shop.models import Products
from market.settings import PRODUCT_QUANTITY_CHOICES


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'slug', 'description', 'color', 'category', 'price', 'discount', 'photo', 'currency_char',
                  'article']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'slug': forms.TextInput(attrs={'class': 'form-control'}),
                   'description': forms.Textarea(attrs={'class': 'form-control'}),
                   'color': forms.Select(attrs={'class': 'form-control'}),
                   'category': forms.Select(attrs={'class': 'form-control'}),
                   'price': forms.TextInput(attrs={'class': 'form-control'}),
                   'discount': forms.TextInput(attrs={'class': 'form-control'}),
                   'currency_char': forms.Select(attrs={'class': 'form-control'}),
                   'article': forms.TextInput(attrs={'class': 'form-control'}),
                   'photo': forms.FileInput(attrs={'class': 'form-control'})
                   }


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=[(i, str(i)) for i in range(1, PRODUCT_QUANTITY_CHOICES + 1)],
                                      coerce=int,
                                      widget=forms.Select(attrs={'class': 'form-control'}),
                                      label='Количество')
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
