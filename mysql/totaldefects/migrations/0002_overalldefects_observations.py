# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('totaldefects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='overalldefects',
            name='observations',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
