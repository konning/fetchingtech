# Generated by Django 2.2.6 on 2019-10-14 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='search',
            field=models.TextField(blank=True, null=True),
        ),
    ]
