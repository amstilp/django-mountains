# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mountains', '0002_mountainrange'),
    ]

    operations = [
        migrations.AddField(
            model_name='mountain',
            name='mountain_range',
            field=models.ForeignKey(to='mountains.MountainRange', related_name='mountains', null=True),
        ),
    ]
