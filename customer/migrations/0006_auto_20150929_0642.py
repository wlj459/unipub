# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_customer_head'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='School',
            new_name='school',
        ),
    ]
