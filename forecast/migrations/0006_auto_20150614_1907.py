# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forecast', '0005_auto_20150614_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeframe',
            name='ant_award_date',
            field=models.DateField(null=True, verbose_name='Anticipated Award Date'),
        ),
        migrations.AlterField(
            model_name='timeframe',
            name='ant_release_date',
            field=models.DateField(null=True, verbose_name='Anticipated Release Date'),
        ),
    ]
