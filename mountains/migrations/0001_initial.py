# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mountain',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('height', models.PositiveIntegerField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('number_of_summits', models.PositiveIntegerField(default=1)),
                ('snow_level', models.PositiveIntegerField(default=0)),
                ('number_of_climbs', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
