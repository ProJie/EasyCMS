# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-16 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMScore', '0004_auto_20170116_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='intro',
            field=models.TextField(default=b'', null=True, verbose_name=b'\xe6\xa0\x8f\xe7\x9b\xae\xe7\xae\x80\xe4\xbb\x8b'),
        ),
    ]
