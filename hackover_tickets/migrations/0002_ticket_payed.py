# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-27 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackover_tickets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='payed',
            field=models.BooleanField(default=False),
        ),
    ]