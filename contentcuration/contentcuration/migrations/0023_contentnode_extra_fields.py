# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-20 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentcuration', '0022_auto_20160920_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentnode',
            name='extra_fields',
            field=models.TextField(blank=True, null=True),
        ),
    ]
