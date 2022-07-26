# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-16 18:28
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0013_auto_20160419_1133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='temporaryproduct',
            options={'verbose_name': 'temporary product', 'verbose_name_plural': 'temporary products'},
        ),
        migrations.RenameField(
            model_name='purchase',
            old_name='product',
            new_name='product_id',
        ),
        migrations.AddField(
            model_name='purchase',
            name='product',
            field=models.CharField(max_length=32, null=True, verbose_name='product'),
        ),
        migrations.RunSQL('UPDATE billing_purchase INNER JOIN billing_product ON billing_purchase.product_id_id = billing_product.id SET billing_purchase.product = billing_product.name'),
        migrations.RemoveField(
            model_name='purchase',
            name='product_id',
        ),
        migrations.AlterField(
            model_name='purchase',
            name='product',
            field=models.CharField(max_length=32, verbose_name='product'),
        ),
    ]
