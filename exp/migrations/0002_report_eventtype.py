# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='eventType',
            field=models.CharField(default='none', max_length=100),
            preserve_default=False,
        ),
    ]
