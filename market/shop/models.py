from django.db import models
from django.urls import reverse


class Products(models.Model):
    name = models.CharField(max_length=20, verbose_name='name')
    slug = models.SlugField(max_length=20, unique=True, db_index=True, verbose_name="slug")
    description = models.TextField(max_length=600, verbose_name='description')
    photo = models.ImageField(upload_to='products/', verbose_name='photo')
    color = models.ForeignKey('Color', on_delete=models.PROTECT, verbose_name='color')
    category = models.ForeignKey('Categories', on_delete=models.PROTECT, verbose_name='category')
    article = models.CharField(max_length=20, verbose_name='article')
    price = models.IntegerField(verbose_name='price')
    discount = models.IntegerField(verbose_name='discount', blank=True, null=True)
    currency_char = models.ForeignKey('Currency', on_delete=models.PROTECT, verbose_name='currency')
    total_purchased = models.IntegerField(verbose_name='total purchased', default=0)

    def __str__(self):
        return f'{self.name}art{self.article}'

    def get_absolute_url(self):
        return reverse('promout', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ['name']


class Currency(models.Model):
    char = models.CharField(max_length=1, verbose_name='currency char')

    def __str__(self):
        return self.char

    class Meta:
        verbose_name = 'валюта'
        verbose_name_plural = 'валюты'
        ordering = ['char']


class Categories(models.Model):
    objects = None
    title = models.CharField(max_length=20, verbose_name='title')
    slug = models.SlugField(max_length=20, unique=True, db_index=True, verbose_name="slug")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['title']


class Color(models.Model):
    title = models.CharField(max_length=20, verbose_name='name')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'цвет'
        verbose_name_plural = 'цвета'
        ordering = ['title']
