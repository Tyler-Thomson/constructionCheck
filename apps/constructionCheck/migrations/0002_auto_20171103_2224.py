# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-03 22:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('constructionCheck', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checklist',
            old_name='user',
            new_name='manager',
        ),
    ]