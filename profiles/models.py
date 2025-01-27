from django.db import models
from django.conf import settings


class Driver(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='driver_profile')
    vehicle_type = models.CharField(max_length=140)
    vehicle_model = models.CharField(max_length=140)
    vehicle_year = models.CharField(max_length=4)
    license_number = models.CharField(max_length=140)
    current_location = models.CharField(max_length=140)
    is_available = models.BooleanField(default=True)
    rating = models.FloatField(default=0.0)
    number_of_rides = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Rider(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rider_profile')
    rating = models.FloatField(default=0.0)
    preferred_vehicle_type = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email