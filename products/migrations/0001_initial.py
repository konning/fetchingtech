# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-12 20:46
from __future__ import unicode_literals

import django.contrib.postgres.search
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.CharField(max_length=255, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=products.models.PathAndRename('categories/'))),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='products.Category')),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=255, unique=True)),
                ('rank', models.PositiveIntegerField(blank=True, null=True)),
                ('discount', models.FloatField(blank=True, null=True)),
                ('search', django.contrib.postgres.search.SearchVectorField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Category')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Manufacturer')),
            ],
            options={
                'ordering': ['manufacturer', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
                ('model', models.CharField(blank=True, max_length=50)),
                ('upc', models.CharField(blank=True, max_length=12)),
                ('ean', models.CharField(blank=True, max_length=13)),
                ('msrp', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('image', models.URLField(blank=True, max_length=255, null=True)),
                ('rank', models.PositiveIntegerField(blank=True, null=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
            options={
                'ordering': ['parent', 'name'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='variant',
            unique_together=set([('parent', 'name')]),
        ),
    ]
