# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='cpu',
            field=models.ForeignKey(to='web_models.Cpu', null=True),
        ),
        migrations.AlterField(
            model_name='server',
            name='disk',
            field=models.ForeignKey(to='web_models.Disk', null=True),
        ),
        migrations.AlterField(
            model_name='server',
            name='memory',
            field=models.ForeignKey(to='web_models.Memory', null=True),
        ),
    ]
