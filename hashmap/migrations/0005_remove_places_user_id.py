# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hashmap', '0004_remove_user_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='places',
            name='user_id',
        ),
    ]
