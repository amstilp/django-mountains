# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mountains', '0008_auto_20160106_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mountain',
            name='image',
            field=models.ImageField(null=True, blank=True, upload_to='mountains'),
        ),
        migrations.AlterField(
            model_name='mountain',
            name='mountain_range',
            field=models.ForeignKey(null=True, related_name='mountains', to='mountains.MountainRange'),
        ),
    ]
