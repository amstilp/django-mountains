# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mountains', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MountainRange',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('region', models.CharField(max_length=200, default='Pacific Northwest')),
            ],
        ),
    ]
