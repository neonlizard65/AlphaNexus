# Generated by Django 4.2.1 on 2023-05-28 20:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_remove_country_flag_remove_country_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cdkey',
            name='is_redeemed',
            field=models.BooleanField(default=False, verbose_name='Исчерпан'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='background',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='', verbose_name='Фон'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='bio',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Доп. информация'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='cart',
            field=models.ManyToManyField(blank=True, default=None, related_name='cart', to='web.product', verbose_name='Корзина'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='wishlist',
            field=models.ManyToManyField(blank=True, default=None, related_name='wishlist', to='web.product', verbose_name='Список желаемых'),
        ),
        migrations.AlterField(
            model_name='developer',
            name='bio',
            field=models.TextField(blank=True, null=True, verbose_name='Доп. информация'),
        ),
        migrations.AlterField(
            model_name='developer',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Логотип'),
        ),
        migrations.AlterField(
            model_name='developer',
            name='name',
            field=models.CharField(unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='post',
            name='media',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='release',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата выхода'),
        ),
    ]
