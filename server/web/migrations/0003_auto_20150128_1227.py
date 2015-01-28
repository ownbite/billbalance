# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20150126_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='category',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='person',
        ),
    ]
