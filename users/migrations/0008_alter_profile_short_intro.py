# Generated by Django 3.2.8 on 2021-10-18 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_profile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='short_intro',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
