# Generated by Django 3.1.7 on 2021-03-28 21:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, max_length=100, null=True, verbose_name='text')),
                ('create_date', models.DateTimeField(default=datetime.datetime(2021, 3, 28, 21, 3, 5, 973474))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.user', verbose_name='author')),
            ],
        ),
    ]
