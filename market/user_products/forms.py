from django import forms

from shop.models import Products


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'slug', 'photo', 'description', 'color', 'category', 'currency_char', 'price', 'discount']
        help_texts = {'slug': 'Эта надпись будет в ссылке на страницу товара'}
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'slug': forms.TextInput(attrs={'class': 'form-control'}),
                   'description': forms.Textarea(attrs={'class': 'form-control'}),
                   'color': forms.Select(attrs={'class': 'form-control'}),
                   'category': forms.Select(attrs={'class': 'form-control'}),
                   'price': forms.TextInput(attrs={'class': 'form-control'}),
                   'discount': forms.TextInput(attrs={'class': 'form-control'}),
                   'currency_char': forms.Select(attrs={'class': 'form-control'}),
                   'photo': forms.FileInput(attrs={'class': 'form-control'})
                   }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if user and user.is_authenticated:
            self.instance.author = user
