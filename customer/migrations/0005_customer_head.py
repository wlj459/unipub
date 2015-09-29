# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_remove_customer_head'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='head',
            field=models.ForeignKey(default=None, verbose_name='\u5934\u50cf', to='customer.Head'),
        ),
    ]
