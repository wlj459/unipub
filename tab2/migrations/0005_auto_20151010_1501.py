# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tab2', '0004_category_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='ad',
        ),
        migrations.AddField(
            model_name='article',
            name='ad_1',
            field=models.CharField(default=b'http://7xl7bo.com1.z0.glb.clouddn.com/logo.png', max_length=300, verbose_name='\u4e0a\u90e8\u5e7f\u544a\u8fde\u63a5'),
        ),
        migrations.AddField(
            model_name='article',
            name='ad_2',
            field=models.CharField(default=b'http://7xl7bo.com1.z0.glb.clouddn.com/logo.png', max_length=300, verbose_name='\u4e0b\u90e8\u5e7f\u544a\u8fde\u63a5'),
        ),
    ]
