# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tab1', '0005_auto_20151027_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='getbook',
            name='remark',
            field=models.CharField(max_length=500, null=True, verbose_name='\u8ba2\u9605\u5185\u5bb9', blank=True),
        ),
    ]
