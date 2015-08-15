# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tab1', '0002_auto_20150809_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='company_name',
            field=models.CharField(max_length=300, verbose_name='\u516c\u53f8\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='business',
            name='contact',
            field=models.CharField(max_length=300, verbose_name='\u8054\u7cfb\u65b9\u5f0f'),
        ),
        migrations.AlterField(
            model_name='business',
            name='cooperation_way',
            field=models.CharField(max_length=1000, verbose_name='\u5408\u4f5c\u65b9\u5f0f'),
        ),
        migrations.AlterField(
            model_name='business',
            name='user_name',
            field=models.CharField(max_length=300, verbose_name='\u7528\u6237'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='email',
            field=models.CharField(max_length=300, verbose_name='\u90ae\u7bb1'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='message',
            field=models.CharField(max_length=1000, verbose_name='\u7559\u8a00'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='phone_num',
            field=models.CharField(max_length=300, verbose_name='\u7535\u8bdd'),
        ),
        migrations.AlterField(
            model_name='getbook',
            name='email',
            field=models.CharField(max_length=300, verbose_name='\u90ae\u7bb1'),
        ),
        migrations.AlterField(
            model_name='getbook',
            name='phone_num',
            field=models.CharField(max_length=300, verbose_name='\u7535\u8bdd'),
        ),
    ]
