# Generated by Django 2.2.6 on 2019-10-14 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0010_auto_20191014_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='shipping',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8, null=True),
        ),
    ]
