# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forecast', '0009_auto_20150615_0051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='award',
            old_name='relevance',
            new_name='relevant',
        ),
    ]
