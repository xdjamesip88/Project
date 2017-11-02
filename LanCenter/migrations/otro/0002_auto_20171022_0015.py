# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 05:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LanCenter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='stockdetalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('vendidos', models.IntegerField()),
                ('restante', models.IntegerField()),
                ('total', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='stock',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='producto',
        ),
        migrations.AddField(
            model_name='stock',
            name='fecha',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='stock',
            name='usuario',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='stockdetalle',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LanCenter.stock'),
        ),
    ]
