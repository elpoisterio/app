# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=30)),
                ('number', models.BigIntegerField(default=b'', unique=True)),
                ('imei', models.BigIntegerField(default=b'')),
                ('email', models.EmailField(default=b'', unique=True, max_length=100)),
                ('latitude', models.DecimalField(default=b'', max_length=20, max_digits=29, decimal_places=9)),
                ('longitude', models.DecimalField(default=b'', max_length=20, max_digits=29, decimal_places=9)),
                ('address', models.CharField(default=b'', max_length=150)),
            ],
        ),
    ]
