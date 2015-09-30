# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_auto_20150929_0642'),
    ]

    operations = [
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300, verbose_name='\u7701\u4efd\u540d\u79f0')),
            ],
            options={
                'verbose_name': '\u7701\u4efd',
                'verbose_name_plural': '\u7701\u4efd',
            },
        ),
        migrations.AddField(
            model_name='school',
            name='province',
            field=models.ForeignKey(default=None, verbose_name='\u7701\u4efd', to='customer.Province', blank=True, null= True),
        ),
    ]
