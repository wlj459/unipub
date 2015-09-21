# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300, verbose_name='\u6807\u9898\u540d')),
                ('is_send', models.BooleanField(default=False, verbose_name='\u662f\u5426\u663e\u793a')),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('content', models.TextField(verbose_name='\u6b63\u6587')),
                ('clicks', models.IntegerField(default=0, verbose_name='\u70b9\u51fb\u6b21\u6570')),
                ('summary', models.CharField(max_length=300, verbose_name='\u6587\u7ae0\u7b80\u4ecb')),
                ('ad', models.CharField(max_length=300, verbose_name='\u5e7f\u544a\u8fde\u63a5')),
                ('author', models.ForeignKey(verbose_name='\u4f5c\u8005', to='customer.Customer')),
            ],
            options={
                'ordering': ['-published'],
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u7c7b\u578b')),
                ('url', models.CharField(max_length=300, verbose_name='\u5e7f\u544a\u94fe\u63a5')),
            ],
            options={
                'verbose_name': '\u7c7b\u578b',
                'verbose_name_plural': '\u7c7b\u578b\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('published', models.DateTimeField(auto_now=True, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('comment', models.TextField(max_length=300, verbose_name='\u8bc4\u8bba')),
                ('article', models.ForeignKey(verbose_name='\u6587\u7ae0', to='tab2.Article')),
                ('author', models.ForeignKey(verbose_name='\u4f5c\u8005', to='customer.Customer')),
            ],
            options={
                'ordering': ['-published'],
                'verbose_name': '\u8bc4\u8bba',
                'verbose_name_plural': '\u8bc4\u8bba\u7c7b',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(verbose_name='\u7c7b\u578b', to='tab2.Category'),
        ),
    ]
