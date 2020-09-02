from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse

class GazCounterModel(models.Model):
    value = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    unit_price = models.DecimalField(default=1.30, max_digits=1000, decimal_places=2)
    monthly_cost = models.DecimalField(default=0, max_digits=1000, decimal_places=2)
    monthly_usage = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    total_cost = models.DecimalField(default=0, max_digits=1000, decimal_places=2)

    def __str__(self):
        return f'{self.value} {self.date} {self.unit_price.price} {self.monthly_usage} {self.monthly_cost} {self.total_cost}'
    
    def get_absolute_url(self):
        return reverse("gaz-detail", kwargs={"pk": self.pk})
    