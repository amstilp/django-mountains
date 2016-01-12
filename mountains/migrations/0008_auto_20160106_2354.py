# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mountains', '0007_mountain_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mountain',
            name='mountain_range',
            field=models.ForeignKey(to='mountains.MountainRange', blank=True, related_name='mountains', null=True),
        ),
    ]
