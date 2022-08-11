# Generated by Django 4.0.6 on 2022-08-09 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='name')),
                ('slug', models.SlugField(max_length=20, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='name')),
            ],
            options={
                'verbose_name': 'цвет',
                'verbose_name_plural': 'цвета',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char', models.CharField(max_length=1, verbose_name='currency char')),
            ],
            options={
                'verbose_name': 'валюта',
                'verbose_name_plural': 'валюты',
                'ordering': ['char'],
            },
        ),
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
                ('content', models.CharField(max_length=20, verbose_name='content')),
            ],
            options={
                'verbose_name': 'политика',
                'verbose_name_plural': 'политики',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='name')),
                ('slug', models.SlugField(max_length=20, unique=True, verbose_name='slug')),
                ('description', models.TextField(max_length=600, verbose_name='description')),
                ('photo', models.ImageField(upload_to='products/', verbose_name='photo')),
                ('article', models.CharField(max_length=20, verbose_name='article')),
                ('price', models.IntegerField(verbose_name='price')),
                ('discount', models.IntegerField(blank=True, null=True, verbose_name='discount')),
                ('total_purchased', models.CharField(max_length=20, verbose_name='total purchased')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.categories', verbose_name='category')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.color', verbose_name='color')),
                ('currency_char', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.currency', verbose_name='currency')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=20, verbose_name='name')),
                ('text_content', models.CharField(max_length=20, verbose_name='text content')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.products', verbose_name='product')),
            ],
            options={
                'verbose_name': 'отзыв',
                'verbose_name_plural': 'отзывы',
                'ordering': ['author'],
            },
        ),
    ]
