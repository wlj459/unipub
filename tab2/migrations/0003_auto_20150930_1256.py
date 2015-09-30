# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tab2', '0002_auto_20150929_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='ad',
            field=models.CharField(default=b'http://7xl7bo.com1.z0.glb.clouddn.com/logo.png', max_length=300, verbose_name='\u5e7f\u544a\u8fde\u63a5'),
        ),
    ]
