# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u540d\u79f0')),
                ('email', models.CharField(max_length=100, verbose_name='\u90ae\u7bb1')),
                ('num', models.CharField(default=b'', max_length=100, verbose_name='\u5de5\u5546\u53f7')),
                ('qq', models.CharField(default=b'', max_length=100, null=True, verbose_name='\u8054\u7cfb\u65b9\u5f0f', blank=True)),
                ('introduction', models.TextField(default=b'', max_length=500, null=True, verbose_name='\u7b80\u4ecb', blank=True)),
                ('permission', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5ba1\u6838')),
                ('type', models.BooleanField(default=False, verbose_name='\u662f\u5426\u662f\u4f01\u4e1a\u7528\u6237')),
                ('open_id', models.CharField(max_length=100, verbose_name='OpenID')),
                ('integral', models.IntegerField(default=50, verbose_name='\u79ef\u5206')),
            ],
            options={
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237',
            },
        ),
    ]
