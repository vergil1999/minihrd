# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-09 07:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('karyawan', '0002_auto_20180407_0854'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kehadiran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis_kehadiran', models.CharField(choices=[('izin', 'Izin'), ('cuti', 'Cuti'), ('alpa', 'Tanpa Alasan'), ('hadir', 'Hadir')], max_length=20)),
                ('waktu', models.DateField()),
                ('karyawan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='karyawan.Karyawan')),
            ],
        ),
    ]
