# Generated by Django 3.2.8 on 2021-10-29 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaksinasi', '0004_auto_20211029_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendaftar',
            name='NIK',
            field=models.CharField(max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='vaksin',
            name='kode',
            field=models.CharField(max_length=3, unique=True),
        ),
    ]
