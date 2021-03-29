# Generated by Django 3.1.7 on 2021-03-28 21:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='author',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='message',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 28, 21, 15, 10, 190200)),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]