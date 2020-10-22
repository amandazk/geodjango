# Generated by Django 3.1.2 on 2020-10-22 20:19

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0002_auto_20201022_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidences',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326),
        ),
        migrations.AlterField(
            model_name='incidences',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
