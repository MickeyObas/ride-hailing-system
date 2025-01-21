from django.db import models


class Ride(models.Model):
    class RideStatus(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        ACCEPTED = 'ACCEPTED', 'Accepted'
        IN_PROGRESS = 'IN_PROGRESS', 'In Progress'
        COMPLETED = 'COMPLETED', 'Completed'
        CANCELLED = 'CANCELLED', 'Cancelled'
        
    rider = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='rider')
    driver = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='driver')
    pickup_location = models.CharField(max_length=140)
    dropoff_location = models.CharField(max_length=140)
    status = models.CharField(max_length=10)
    ride_type = models.CharField(max_length=140)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField()
    pickup_time = models.DateTimeField()
    actual_pickup_time = models.DateTimeField(null=True, blank=True)
    completion_time = models.DateTimeField(null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)
    rating_count = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class RideHistory(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    ride = models.ForeignKey('rides.Ride', on_delete=models.CASCADE)
    role = models.CharField(max_length=140)
    status = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    


