# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mountains', '0010_auto_20160107_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mountain',
            name='image',
            field=models.ImageField(null=True, blank=True, upload_to='mountains'),
        ),
    ]
