# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forecast', '0008_award_relevance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='relevance',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
