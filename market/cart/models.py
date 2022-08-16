from django.db import models


class Politics(models.Model):
    title = models.CharField(max_length=20, verbose_name='title')
    content = models.TextField(max_length=600, verbose_name='content')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'политика'
        verbose_name_plural = 'политики'
        ordering = ['title']


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


class Sell(models.Model):
    payment = models.ForeignKey('Payment', on_delete=models.PROTECT, verbose_name='payment')
    delivery = models.ForeignKey('Delivery', on_delete=models.PROTECT, verbose_name='delivery')
