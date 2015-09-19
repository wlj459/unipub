# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '__first__'),
    ]
    operations = [
        migrations.AlterField(
            model_name='article',
            name='ad',
            field=models.CharField(max_length=300, verbose_name='\u5e7f\u544a\u8fde\u63a5'),
        ),
        migrations.AlterField(
            model_name='category',
            name='url',
            field=models.CharField(max_length=300, verbose_name='\u5e7f\u544a\u94fe\u63a5'),

        ),
    ]
