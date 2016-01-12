# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mountains', '0005_mountain_number_of_marmots_seen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mountain',
            name='number_of_climbs',
        ),
    ]
