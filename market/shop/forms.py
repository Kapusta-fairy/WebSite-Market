from django import forms
from shop.models import Products, Review
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


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=[(i, str(i)) for i in range(1, PRODUCT_QUANTITY_CHOICES + 1)],
                                      coerce=int,
                                      widget=forms.Select(attrs={'class': 'form-control'}),
                                      label='Количество')
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text_content']
        widgets = {'text_content': forms.Textarea(attrs={'class': 'form-control'})}

    def __init__(self, user, product, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.product = product
        if user and user.is_authenticated:
            self.instance.author = user
