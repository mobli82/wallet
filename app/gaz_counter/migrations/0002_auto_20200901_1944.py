# Generated by Django 3.1 on 2020-09-01 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gaz_counter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gazcountermodel',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, default=1.3, max_digits=1000),
        ),
        migrations.DeleteModel(
            name='GazCounterUnitPriceModel',
        ),
    ]