from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=20, verbose_name='name')
    slug = models.SlugField(max_length=20, unique=True, db_index=True, verbose_name="slug")
    color = models.ForeignKey('Color', on_delete=models.PROTECT, verbose_name='color')
    category = models.ForeignKey('Categories', on_delete=models.PROTECT, verbose_name='category')
    article = models.CharField(max_length=20, verbose_name='article')
    price = models.IntegerField(verbose_name='price')
    discount = models.IntegerField(verbose_name='discount')
    total_purchased = models.CharField(max_length=20, verbose_name='total purchased')

    def __str__(self):
        return f'{self.name}art{self.article}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ['name']


class Categories(models.Model):
    name = models.CharField(max_length=20, verbose_name='name')
    slug = models.SlugField(max_length=20, unique=True, db_index=True, verbose_name="slug")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name']


class Reviews(models.Model):
    product = models.ForeignKey('products', on_delete=models.PROTECT, verbose_name='product')
    author = models.CharField(max_length=20, verbose_name='name')
    text_content = models.CharField(max_length=20, verbose_name='text content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created at')

    def __str__(self):
        return f'{self.author}{self.product}'

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'
        ordering = ['author']


class Politics(models.Model):
    title = models.CharField(max_length=20, verbose_name='title')
    content = models.CharField(max_length=20, verbose_name='content')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'политика'
        verbose_name_plural = 'политики'
        ordering = ['title']


class Basket(models.Model):
    product = models.ForeignKey('products', on_delete=models.PROTECT, verbose_name='product')

    def __str__(self):
        return self.product

    class Meta:
        verbose_name = 'корзина'
        verbose_name_plural = 'корзины'
        ordering = ['product_name']


class Color(models.Model):
    name = models.CharField(max_length=20, verbose_name='name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'цвет'
        verbose_name_plural = 'цвета'
        ordering = ['name']


class Delivery(models.Model):
    title = models.CharField(max_length=20, verbose_name='title')
    description = models.CharField(max_length=20, verbose_name='description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'доставка'
        verbose_name_plural = 'способы доставки'
        ordering = ['title']


class Payment(models.Model):
    title = models.CharField(max_length=20, verbose_name='title')
    description = models.CharField(max_length=20, verbose_name='description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'оплата'
        verbose_name_plural = 'способы оплаты'
        ordering = ['title']


class Search(models.Model):
    pass


class Detail(models.Model):
    pass
