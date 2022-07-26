# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-06 13:38
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scheduling', '0011_auto_20161206_1438'),
        ('consumption', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsumptionForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed_at', models.DateTimeField(null=True, verbose_name='completed at ')),
                ('comments', models.TextField(null=True, verbose_name='comments')),
                ('completed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='completed by')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='scheduling.Event', verbose_name='event')),
            ],
            options={
                'verbose_name': 'consumption form',
                'verbose_name_plural': 'consumption forms',
            },
        ),
        migrations.AlterField(
            model_name='weightconsumptionproduct',
            name='has_flowmeter',
            field=models.BooleanField(default=False, help_text='Designates wheter apart from weight, this product also uses a flowmeter.', verbose_name='has flowmeter'),
        ),
    ]
