# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-10 01:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Apellidos')),
                ('code', models.CharField(max_length=10, null=True, verbose_name='C\xf3digo')),
                ('id_type', models.CharField(choices=[('per', 'C\xe9dula F\xedsica'), ('jur', 'C\xe9dula Jur\xeddica'), ('pas', 'Pasaporte')], default='per', max_length=3, verbose_name='Tipo de Identificaci\xf3n')),
                ('id_num', models.CharField(blank=True, max_length=255, null=True, verbose_name='Num Identificaci\xf3n')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Direcci\xf3n')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Tel\xe9fono')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]
