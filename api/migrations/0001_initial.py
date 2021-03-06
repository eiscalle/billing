# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 12:44
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BillingUser',
            fields=[
                ('user_id', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='User ID')),
                ('is_trial_activated', models.BooleanField(default=False, verbose_name='Is trial activated')),
                ('payed_till', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Payed till')),
                ('balance', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Balance')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Price')),
                ('payed_from', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Payed from')),
                ('payed_till', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Payed till')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
                ('status', models.CharField(default='', max_length=255, verbose_name='Status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='api.BillingUser', verbose_name='User')),
            ],
        ),
    ]
