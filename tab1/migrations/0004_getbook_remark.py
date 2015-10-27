# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tab1', '0003_auto_20151021_0726'),
    ]

    operations = [
        migrations.AddField(
            model_name='getbook',
            name='remark',
            field=models.CharField(max_length=500, null=True, verbose_name='\u520a\u7269', blank=True),
        ),
    ]
