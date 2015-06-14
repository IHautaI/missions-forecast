# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forecast', '0003_auto_20150609_1737'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('descr', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TimeFrame',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ant_award_date', models.DateField(verbose_name='Anticipated Award Date')),
                ('ant_release_date', models.DateField(verbose_name='Anticipated Release Date')),
                ('fiscal_year', models.DateField(default='1/1/16', verbose_name='Year of Action')),
            ],
        ),
        migrations.RemoveField(
            model_name='award',
            name='AA_specialist',
        ),
        migrations.RemoveField(
            model_name='award',
            name='ant_award_date',
        ),
        migrations.RemoveField(
            model_name='award',
            name='ant_release_date',
        ),
        migrations.RemoveField(
            model_name='award',
            name='award_length',
        ),
        migrations.RemoveField(
            model_name='award',
            name='fiscal_year',
        ),
        migrations.AlterField(
            model_name='award',
            name='BF_status_change',
            field=models.CharField(default='None', verbose_name='BF Status Change', max_length=255),
        ),
        migrations.AlterField(
            model_name='award',
            name='MBIO_name',
            field=models.CharField(verbose_name='M/B/IO name', max_length=255),
        ),
        migrations.AlterField(
            model_name='award',
            name='amt_range',
            field=models.CharField(verbose_name='Award Amount Range', max_length=255),
        ),
        migrations.AlterField(
            model_name='award',
            name='award_type',
            field=models.CharField(verbose_name='Award Type', max_length=255),
        ),
        migrations.AlterField(
            model_name='award',
            name='description',
            field=models.CharField(default='None', verbose_name='Description', max_length=255),
        ),
        migrations.AlterField(
            model_name='award',
            name='partner',
            field=models.CharField(default='None', verbose_name='Implementing Partner', max_length=255),
        ),
        migrations.AlterField(
            model_name='award',
            name='small_business_SA',
            field=models.CharField(default='None', verbose_name='Small Business SA', max_length=255),
        ),
        migrations.AlterField(
            model_name='award',
            name='title',
            field=models.CharField(verbose_name='Title', max_length=255),
        ),
        migrations.AddField(
            model_name='award',
            name='specialist',
            field=models.ForeignKey(to='forecast.Specialist', null=True),
        ),
        migrations.AddField(
            model_name='award',
            name='timeframe',
            field=models.OneToOneField(null=True, to='forecast.TimeFrame'),
        ),
    ]
