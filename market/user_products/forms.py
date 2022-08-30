from django import forms

from shop.models import Products


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
