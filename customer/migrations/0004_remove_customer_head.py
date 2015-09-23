# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20150923_0829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='head',
        ),
    ]
