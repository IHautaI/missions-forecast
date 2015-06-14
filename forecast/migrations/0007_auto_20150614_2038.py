# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forecast', '0006_auto_20150614_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='NAICS_code',
            field=models.CharField(max_length=255, verbose_name='NAICS Code'),
        ),
        migrations.AlterField(
            model_name='details',
            name='solicitation_number',
            field=models.CharField(max_length=255, verbose_name='Solicitation Number'),
        ),
        migrations.AlterField(
            model_name='timeframe',
            name='fiscal_year',
            field=models.DateField(default='01/01/2000', verbose_name='Year of Action'),
        ),
    ]
