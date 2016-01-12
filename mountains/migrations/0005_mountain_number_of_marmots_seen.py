# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mountains', '0004_mountain_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='mountain',
            name='number_of_marmots_seen',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
