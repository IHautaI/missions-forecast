# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forecast', '0002_auto_20150609_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='AA_specialist',
            field=models.CharField(max_length=50, verbose_name='A&A Specialist'),
        ),
        migrations.AlterField(
            model_name='award',
            name='BF_status_change',
            field=models.CharField(max_length=200, default='None', verbose_name='BF Status Change'),
        ),
        migrations.AlterField(
            model_name='award',
            name='MBIO_name',
            field=models.CharField(max_length=200, verbose_name='M/B/IO name'),
        ),
        migrations.AlterField(
            model_name='award',
            name='NAICS_code',
            field=models.IntegerField(default=-1, verbose_name='NAICS Code'),
        ),
        migrations.AlterField(
            model_name='award',
            name='amt_range',
            field=models.CharField(max_length=20, verbose_name='Award Amount Range'),
        ),
        migrations.AlterField(
            model_name='award',
            name='award_length',
            field=models.CharField(max_length=20, verbose_name='Award Length'),
        ),
        migrations.AlterField(
            model_name='award',
            name='award_type',
            field=models.CharField(max_length=20, verbose_name='Award Type'),
        ),
        migrations.AlterField(
            model_name='award',
            name='description',
            field=models.CharField(max_length=200, default='None', verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='award',
            name='fiscal_year',
            field=models.DateField(default='1/1/16', verbose_name='Year of Action'),
        ),
        migrations.AlterField(
            model_name='award',
            name='partner',
            field=models.CharField(max_length=20, default='None', verbose_name='Implementing Partner'),
        ),
        migrations.AlterField(
            model_name='award',
            name='small_business_SA',
            field=models.CharField(max_length=20, default='None', verbose_name='Small Business SA'),
        ),
        migrations.AlterField(
            model_name='award',
            name='solicitation_number',
            field=models.IntegerField(default=-1, verbose_name='Solicitation Number'),
        ),
        migrations.AlterField(
            model_name='award',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
    ]
