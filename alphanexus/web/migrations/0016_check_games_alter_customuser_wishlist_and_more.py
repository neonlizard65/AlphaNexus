# Generated by Django 4.2.1 on 2023-05-31 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_alter_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='check',
            name='games',
            field=models.ManyToManyField(to='web.product', verbose_name='Игры'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='wishlist',
            field=models.ManyToManyField(blank=True, default=None, related_name='wishlist', to='web.product', verbose_name='Список желаемого'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(help_text='Зажмите CTRL и нажмите на тег, чтобы выделить несколько', to='web.tag', verbose_name='Теги'),
        ),
    ]