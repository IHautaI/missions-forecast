# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forecast', '0007_auto_20150614_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='award',
            name='relevance',
            field=models.NullBooleanField(),
        ),
    ]
