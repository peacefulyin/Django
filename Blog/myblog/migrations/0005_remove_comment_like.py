# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 08:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='like',
        ),
    ]