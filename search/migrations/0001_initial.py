# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CorporationNameSearch',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('entity_number', models.CharField(max_length=50)),
                ('date_filed', models.DateTimeField(verbose_name='date filed')),
                ('status', models.CharField(max_length=20)),
                ('entity_name', models.CharField(max_length=20)),
                ('agent_for_service', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
