# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hashmap', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField()),
                ('latitude', models.DecimalField(max_length=20, max_digits=29, decimal_places=9)),
                ('longitude', models.DecimalField(max_length=20, max_digits=29, decimal_places=9)),
                ('address', models.CharField(max_length=150, blank=True)),
                ('name', models.CharField(max_length=200)),
                ('number', models.IntegerField()),
                ('category', models.CharField(max_length=300, blank=True)),
                ('description', models.CharField(max_length=500, blank=True)),
                ('website', models.URLField(blank=True)),
                ('tag', models.CharField(max_length=250, blank=True)),
                ('place_id', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='tags',
            field=models.CharField(max_length=250, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.IntegerField(default=0, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='imei',
            field=models.BigIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='latitude',
            field=models.DecimalField(max_length=20, max_digits=29, decimal_places=9, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='longitude',
            field=models.DecimalField(max_length=20, max_digits=29, decimal_places=9, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='number',
            field=models.BigIntegerField(unique=True),
        ),
    ]
