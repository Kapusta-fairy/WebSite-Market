# Generated by Django 4.0.6 on 2022-09-04 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='currency_char',
        ),
        migrations.AddField(
            model_name='products',
            name='contacts',
            field=models.CharField(default='aboba', max_length=40, verbose_name='Контакты'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.categories',
                                    verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='products',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.color', verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.TextField(max_length=600, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='products',
            name='discount',
            field=models.IntegerField(blank=True, null=True, verbose_name='Скидка'),
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='products',
            name='photo',
            field=models.ImageField(upload_to='products/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.IntegerField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='products',
            name='slug',
            field=models.SlugField(max_length=20, unique=True, verbose_name='Слаг'),
        ),
        migrations.AlterField(
            model_name='products',
            name='total_purchased',
            field=models.IntegerField(default=0, verbose_name='Всего куплено'),
        ),
    ]
