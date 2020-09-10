from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class GazSupplier(models.Model):
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

