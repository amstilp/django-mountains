# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mountains', '0009_auto_20160106_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mountain',
            name='image',
            field=models.ImageField(default='/static/images/mountain.jpg', upload_to='mountains', blank=True),
        ),
    ]
