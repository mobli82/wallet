from django.contrib.auth.models import User
from django.db import models
from django.db.models.aggregates import Max
from django.utils import timezone
from django.urls import reverse

from .utils import calculate_montlhy_power_cost

class PowerCounterModel(models.Model):
    value = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    unit_price = models.DecimalField(default=1.30, max_digits=1000, decimal_places=2)
    monthly_cost = models.DecimalField(default=0, max_digits=1000, decimal_places=2)
    monthly_usage = models.IntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.value} {self.date} {self.monthly_usage} {self.monthly_cost}'
    
    def get_absolute_url(self):
        return reverse("power-detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        record_max = PowerCounterModel.objects.filter(owner=self.owner).aggregate(Max('value'))
        if record_max['value__max'] is None:
            record_max['value__max'] = 0
        self.monthly_usage = self.value - record_max['value__max']

        self.monthly_cost = calculate_montlhy_power_cost(usage=self.monthly_usage, user=self.owner)
        
        super(PowerCounterModel, self).save(*args, **kwargs)