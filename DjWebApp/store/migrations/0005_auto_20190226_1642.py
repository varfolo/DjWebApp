# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-02-26 13:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_profile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='Ufile',
        ),
    ]