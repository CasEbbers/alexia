# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 14:16
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0013_auto_20160412_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='certificate',
        ),
        migrations.AlterField(
            model_name='certificate',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='certificate'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='current_organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='organization.Organization', verbose_name='current organization'),
        ),
    ]
