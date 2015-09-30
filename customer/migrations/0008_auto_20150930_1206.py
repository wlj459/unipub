# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_auto_20150929_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='head',
            field=models.ForeignKey(default=None, blank=True, to='customer.Head', null=True, verbose_name='\u5934\u50cf'),
        ),
    ]
