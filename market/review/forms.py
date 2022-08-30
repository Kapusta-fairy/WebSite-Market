from django import forms

from review.models import Review


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
