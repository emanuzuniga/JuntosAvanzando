# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='last_name',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Apellido del Cliente'),
        ),
    ]
