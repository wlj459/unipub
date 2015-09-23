# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20150921_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300, verbose_name='\u5b66\u6821\u540d\u79f0')),
            ],
            options={
                'verbose_name': '\u5b66\u6821\u540d\u79f0',
                'verbose_name_plural': '\u5b66\u6821',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='School',
            field=models.ForeignKey(default=None, blank=True, to='customer.School', null=True, verbose_name='\u5b66\u6821\u540d\u79f0'),
        ),
    ]
