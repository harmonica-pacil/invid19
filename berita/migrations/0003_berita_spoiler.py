# Generated by Django 3.2.8 on 2021-10-29 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('berita', '0002_auto_20211028_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='berita',
            name='spoiler',
            field=models.CharField(default=123456, max_length=20),
            preserve_default=False,
        ),
    ]
