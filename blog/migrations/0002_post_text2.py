# Generated by Django 2.2.24 on 2021-10-27 05:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text2',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
