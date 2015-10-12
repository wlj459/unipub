# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_auto_20150930_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='integral',
            field=models.IntegerField(default=200, verbose_name='\u79ef\u5206'),
        ),
    ]
