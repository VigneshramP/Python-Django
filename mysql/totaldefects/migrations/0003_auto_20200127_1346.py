# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('totaldefects', '0002_overalldefects_observations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='overalldefects',
            name='vehicle_id',
        ),
        migrations.AlterField(
            model_name='overalldefects',
            name='id',
            field=models.CharField(max_length=15, serialize=False, primary_key=True),
        ),
    ]
