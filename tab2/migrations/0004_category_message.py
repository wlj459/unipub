# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tab2', '0003_auto_20150930_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='message',
            field=models.CharField(default=b'', max_length=500, verbose_name='\u516c\u544a'),
        ),
    ]
