# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mountains', '0006_remove_mountain_number_of_climbs'),
    ]

    operations = [
        migrations.AddField(
            model_name='mountain',
            name='image',
            field=models.ImageField(null=True, upload_to='mountains'),
        ),
    ]
