# Generated by Django 3.1 on 2020-09-23 09:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('suppliers', '0003_auto_20200910_0900'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GazSupplier',
            new_name='GazSupplierModel',
        ),
        migrations.CreateModel(
            name='PowerSupplierModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('vat', models.IntegerField(default=23)),
                ('energy_fee', models.DecimalField(decimal_places=4, default=0.2902, max_digits=1000)),
                ('subscription_fee', models.DecimalField(decimal_places=4, default=1.58, max_digits=1000)),
                ('network_fee_constant', models.DecimalField(decimal_places=4, default=7.49, max_digits=1000)),
                ('network_fee_24_7', models.DecimalField(decimal_places=4, default=0.238, max_digits=1000)),
                ('quality_fee', models.DecimalField(decimal_places=4, default=0.0133, max_digits=1000)),
                ('oze_fee', models.DecimalField(decimal_places=4, default=0.0, max_digits=1000)),
                ('cogeneration_fee', models.DecimalField(decimal_places=5, default=0.00139, max_digits=1000)),
                ('transitional_fee', models.DecimalField(decimal_places=4, default=0.33, max_digits=1000)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]