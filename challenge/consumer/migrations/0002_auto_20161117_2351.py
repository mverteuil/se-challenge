# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 23:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(help_text='First and last name are expected.', max_length=255, unique=True, verbose_name='Full Name'),
        ),
    ]
