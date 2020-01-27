# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EMPLOYEE',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('emp_name', models.CharField(max_length=50)),
                ('emp_qualification', models.CharField(max_length=20)),
                ('id_number', models.CharField(max_length=12)),
            ],
        ),
    ]
