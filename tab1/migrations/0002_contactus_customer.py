# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_auto_20151012_1449'),
        ('tab1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='customer',
            field=models.ForeignKey(default=None, verbose_name='\u7528\u6237', blank=True, to='customer.Customer'),
        ),
    ]
