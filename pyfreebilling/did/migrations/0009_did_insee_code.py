# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-09 18:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('did', '0008_auto_20161216_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='did',
            name='insee_code',
            field=models.PositiveIntegerField(blank=True, help_text='Postal code, INSEE code ... for routing\n          urgency number to the right urgency call center.', null=True, verbose_name='Special code for routing urgency numbers'),
        ),
    ]
