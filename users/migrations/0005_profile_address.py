# Generated by Django 3.2.8 on 2021-10-18 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_short_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]