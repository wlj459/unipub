# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tab1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='others',
            field=models.CharField(max_length=300, null=True, verbose_name='\u5907\u6ce8', blank=True),
        ),
    ]
