# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('MBIO_name', models.CharField(max_length=200)),
                ('AA_specialist', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('NAICS_code', models.IntegerField()),
                ('amt_range', models.CharField(max_length=20)),
                ('partner', models.CharField(max_length=20)),
                ('award_type', models.CharField(max_length=20)),
                ('small_business_SA', models.CharField(max_length=20)),
                ('fiscal_year', models.DateTimeField(verbose_name='Year of Action')),
                ('ant_award_date', models.DateTimeField(verbose_name='Anticipated Award Date')),
                ('ant_release_date', models.DateTimeField(verbose_name='Anticipated Release Date')),
                ('award_length', models.CharField(max_length=20)),
                ('solicitation_number', models.IntegerField()),
                ('BF_status_change', models.CharField(max_length=200)),
            ],
        ),
    ]
