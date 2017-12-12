# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-12 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('summary', models.TextField(max_length=500)),
                ('text', models.TextField(max_length=5000)),
                ('datePosted', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Newspaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('articles', models.ManyToManyField(to='main.Article')),
            ],
        ),
    ]
