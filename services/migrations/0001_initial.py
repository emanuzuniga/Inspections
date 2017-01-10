# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-10 01:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=0, max_length=7, unique=True, verbose_name='C\xf3digo')),
                ('consecutive', models.DecimalField(decimal_places=0, default=0, max_digits=3, verbose_name='Consecutivo')),
                ('description', models.CharField(default='', max_length=255, verbose_name='Descripci\xf3n del producto')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Precio \u20a1')),
                ('unit', models.CharField(default='Unidad', max_length=255, verbose_name='Unidad')),
                ('usetaxes', models.BooleanField(default=False, verbose_name='Usa Impuestos?')),
                ('taxes', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Impuestos %')),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Descuento %')),
            ],
            options={
                'ordering': ['code'],
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
            },
        ),
        migrations.CreateModel(
            name='ServiceDepartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Nombre de la Familia')),
                ('code', models.CharField(max_length=2, unique=True, verbose_name='Identificador de Familia')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='ServiceSubDepartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Nombre de la Sub-Familia')),
                ('code', models.CharField(max_length=2, verbose_name='Identificador de Sub-Familia')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.ServiceDepartment', verbose_name='Familia')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Sub-Categoria',
                'verbose_name_plural': 'Sub-Categorias',
            },
        ),
        migrations.AddField(
            model_name='service',
            name='department',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='services.ServiceDepartment', verbose_name='Familia'),
        ),
        migrations.AddField(
            model_name='service',
            name='subdepartment',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='services.ServiceSubDepartment', verbose_name='Sub-Familia'),
        ),
    ]
