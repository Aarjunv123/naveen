from django.db import models
from .customer import Customer



class Cancel_order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_id = models.IntegerField()
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    reason = models.CharField(max_length=30)

    def __str__(self):
        return self.name




