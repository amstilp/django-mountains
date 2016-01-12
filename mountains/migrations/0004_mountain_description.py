# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mountains', '0003_mountain_mountain_range'),
    ]

    operations = [
        migrations.AddField(
            model_name='mountain',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
