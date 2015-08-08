# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=100, verbose_name='\u7528\u6237')),
                ('contact', models.CharField(max_length=100, verbose_name='\u8054\u7cfb\u65b9\u5f0f')),
                ('company_name', models.CharField(max_length=100, verbose_name='\u516c\u53f8\u540d\u79f0')),
                ('cooperation_way', models.CharField(max_length=300, verbose_name='\u5408\u4f5c\u65b9\u5f0f')),
                ('others', models.CharField(max_length=300, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '\u5408\u4f5c',
                'verbose_name_plural': '\u5408\u4f5c',
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_num', models.CharField(max_length=100, verbose_name='\u7535\u8bdd')),
                ('email', models.CharField(max_length=100, verbose_name='\u90ae\u7bb1')),
                ('message', models.CharField(max_length=300, verbose_name='\u7559\u8a00')),
            ],
            options={
                'verbose_name': '\u6765\u4fe1',
                'verbose_name_plural': '\u6765\u4fe1',
            },
        ),
        migrations.CreateModel(
            name='GetBook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=100, verbose_name='\u90ae\u7bb1')),
                ('phone_num', models.CharField(max_length=100, verbose_name='\u7535\u8bdd')),
            ],
            options={
                'verbose_name': '\u8ba2\u9605',
                'verbose_name_plural': '\u8ba2\u9605',
            },
        ),
    ]
