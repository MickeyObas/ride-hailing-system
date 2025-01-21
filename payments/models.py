from django.db import models


class Payment(models.Model):
    ride = models.ForeignKey('rides.Ride', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=140)
    status = models.CharField(max_length=140)
    date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=140)
    gateway = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

