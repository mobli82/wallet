from django.contrib.auth.models import User
from django.db import models
from django.db.models.aggregates import Max
from django.utils import timezone
from django.urls import reverse
from django.db.models.signals import pre_save

class GazCounterModel(models.Model):
    value = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    unit_price = models.DecimalField(default=1.30, max_digits=1000, decimal_places=2)
    monthly_cost = models.DecimalField(default=0, max_digits=1000, decimal_places=2)
    monthly_usage = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.value} {self.date} {self.unit_price} {self.monthly_usage} {self.monthly_cost} {self.total_cost}'
    
    def get_absolute_url(self):
        return reverse("gaz-detail", kwargs={"pk": self.pk})

# signal to calculate all costs and counter's usage
def calc_monthly_usage_monthly_cost_total_cost(sender, instance, **kwargs):
    max_gaz_value = GazCounterModel.objects.filter(owner=instance.owner).aggregate(Max('value'))

    if max_gaz_value['value__max'] is None:
        max_gaz_value['value__max'] = 0
        max_gaz_value['total_cost__max'] = 0
    
    instance.monthly_usage = instance.value - max_gaz_value['value__max']
    instance.monthly_cost  = instance.monthly_usage * float(instance.unit_price)

    return instance

pre_save.connect(calc_monthly_usage_monthly_cost_total_cost, GazCounterModel)