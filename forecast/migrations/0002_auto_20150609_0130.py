# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forecast', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='ant_award_date',
            field=models.DateField(verbose_name='Anticipated Award Date'),
        ),
        migrations.AlterField(
            model_name='award',
            name='ant_release_date',
            field=models.DateField(verbose_name='Anticipated Release Date'),
        ),
        migrations.AlterField(
            model_name='award',
            name='fiscal_year',
            field=models.DateField(verbose_name='Year of Action'),
        ),
    ]
