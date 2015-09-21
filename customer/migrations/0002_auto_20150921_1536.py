# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Head',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u5934\u50cf\u540d\u79f0')),
                ('url', models.CharField(max_length=300, verbose_name='\u56fe\u7247\u94fe\u63a5')),
            ],
            options={
                'verbose_name': '\u5934\u50cf',
                'verbose_name_plural': '\u5934\u50cf',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='head',
            field=models.ForeignKey(default=None, verbose_name='\u5934\u50cf', to='customer.Head'),
        ),
    ]
