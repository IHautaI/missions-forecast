# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forecast', '0004_auto_20150614_1559'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('description', models.CharField(default='None', verbose_name='Description', max_length=255)),
                ('NAICS_code', models.IntegerField(default=-1, verbose_name='NAICS Code')),
                ('partner', models.CharField(default='None', verbose_name='Implementing Partner', max_length=255)),
                ('small_business_SA', models.CharField(default='None', verbose_name='Small Business SA', max_length=255)),
                ('solicitation_number', models.IntegerField(default=-1, verbose_name='Solicitation Number')),
                ('BF_status_change', models.CharField(default='None', verbose_name='BF Status Change', max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='award',
            name='BF_status_change',
        ),
        migrations.RemoveField(
            model_name='award',
            name='NAICS_code',
        ),
        migrations.RemoveField(
            model_name='award',
            name='description',
        ),
        migrations.RemoveField(
            model_name='award',
            name='partner',
        ),
        migrations.RemoveField(
            model_name='award',
            name='small_business_SA',
        ),
        migrations.RemoveField(
            model_name='award',
            name='solicitation_number',
        ),
        migrations.AddField(
            model_name='award',
            name='details',
            field=models.OneToOneField(null=True, to='forecast.Details'),
        ),
    ]
