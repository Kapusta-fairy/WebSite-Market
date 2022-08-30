# Generated by Django 4.0.6 on 2022-08-30 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='title')),
                ('description', models.CharField(max_length=20, verbose_name='description')),
            ],
            options={
                'verbose_name': 'доставка',
                'verbose_name_plural': 'способы доставки',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='title')),
                ('description', models.CharField(max_length=20, verbose_name='description')),
            ],
            options={
                'verbose_name': 'оплата',
                'verbose_name_plural': 'способы оплаты',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Politics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='title')),
                ('content', models.TextField(max_length=600, verbose_name='content')),
            ],
            options={
                'verbose_name': 'политика',
                'verbose_name_plural': 'политики',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cart.delivery',
                                               verbose_name='Доставка')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cart.payment',
                                              verbose_name='Оплата')),
            ],
        ),
    ]
