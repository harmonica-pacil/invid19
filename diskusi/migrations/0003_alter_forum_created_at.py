# Generated by Django 3.2.8 on 2021-10-29 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diskusi', '0002_auto_20211025_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='created_at',
            field=models.CharField(max_length=50),
        ),
    ]