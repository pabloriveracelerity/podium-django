# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-10-31 20:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyatl', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='footer_link',
            field=models.BooleanField(default=False),
        ),
    ]
