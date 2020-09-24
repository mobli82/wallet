from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class GazSupplierModel(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    vat = models.IntegerField(default=23, null=False, blank=False)
    conversion_rate = models.FloatField(default=11.506, null=False, blank=False)
    distribution_fee = models.DecimalField(default=0.04937, max_digits=1000, decimal_places=5)
    gaz_fuel = models.DecimalField(default=0.08944, max_digits=1000, decimal_places=5)
    subscription_fee = models.DecimalField(default=6.38, max_digits=1000, decimal_places=2)
    distribution_fee_constant = models.DecimalField(default=3.49, max_digits=1000, decimal_places=2)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("gaz-supplier-detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return f'{self.name} {self.vat} {self.conversion_rate} {self.distribution_fee}\
                {self.gaz_fuel} {self.subscription_fee} {self.distribution_fee_constant}'

class PowerSupplierModel(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    vat = models.IntegerField(default=23, null=False, blank=False)
    energy_fee = models.DecimalField(default=0.2902, max_digits=1000, decimal_places=4)
    subscription_fee = models.DecimalField(default=1.5800, max_digits=1000, decimal_places=4)
    network_fee_constant = models.DecimalField(default=7.4900, max_digits=1000, decimal_places=4)
    network_fee_24_7 = models.DecimalField(default=0.2380, max_digits=1000, decimal_places=4)
    quality_fee = models.DecimalField(default=0.0133, max_digits=1000, decimal_places=4)
    oze_fee = models.DecimalField(default=0.0000, max_digits=1000, decimal_places=4)
    cogeneration_fee = models.DecimalField(default=0.00139, max_digits=1000, decimal_places=5)
    transitional_fee = models.DecimalField(default=0.3300, max_digits=1000, decimal_places=4)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("power-supplier-detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return f'{self.name} {self.vat} {self.energy_fee} {self.subscription_fee}\
                {self.network_fee_constant} {self.network_fee_24_7} {self.quality_fee} {self.oze_fee} {self.cogeneration_fee}\
                {self.transitional_fee}'

