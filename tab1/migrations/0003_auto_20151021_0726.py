# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tab1', '0002_contactus_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='customer',
            field=models.ForeignKey(default=None, blank=True, to='customer.Customer', null=True, verbose_name='\u7528\u6237'),
        ),
    ]
