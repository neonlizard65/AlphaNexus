# Generated by Django 4.2.1 on 2023-05-29 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_alter_cdkey_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='banner',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Изображение'),
        ),
    ]
