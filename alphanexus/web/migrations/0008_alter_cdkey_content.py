# Generated by Django 4.2.1 on 2023-05-29 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_alter_cdkey_is_redeemed_alter_customuser_avatar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cdkey',
            name='content',
            field=models.CharField(unique=True, verbose_name='Ключ'),
        ),
    ]
