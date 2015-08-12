# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cpu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cpu_speed', models.IntegerField(default=1)),
                ('processor_cpu_count', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Disk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('disk_type', models.CharField(default=b'SATA', max_length=200)),
                ('disk_size', models.IntegerField(default=1024)),
                ('disk_speed', models.IntegerField(default=5400)),
            ],
        ),
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('memory_size', models.IntegerField(default=1024)),
                ('memory_speed', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(max_length=200)),
                ('ip', models.GenericIPAddressField()),
                ('cpu_slot_count', models.IntegerField(default=1)),
                ('memory_slot_count', models.IntegerField(default=1)),
                ('cpu', models.ForeignKey(to='web_models.Cpu')),
                ('disk', models.ForeignKey(to='web_models.Disk')),
                ('memory', models.ForeignKey(to='web_models.Memory')),
            ],
        ),
    ]
