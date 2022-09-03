from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Review(models.Model):
    product = models.ForeignKey('shop.products', on_delete=models.CASCADE, verbose_name='product')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text_content = models.CharField(max_length=20, verbose_name='Текст вашего отзыва')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created at')

    def __str__(self):
        return f'{self.author}: {self.product}'

    def get_absolute_url(self):
        return reverse('reviews', kwargs={'slug': self.product.slug})

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'
        ordering = ['-created_at']
