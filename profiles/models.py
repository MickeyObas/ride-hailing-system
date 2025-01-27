from django.db import models
from django.conf import settings


class Driver(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='driver_profile')
    is_approved = models.BooleanField(default=False)
    license_number = models.CharField(max_length=140)
    current_location = models.CharField(max_length=140)
    is_available = models.BooleanField(default=True)
    rating = models.FloatField(default=0.0)
    number_of_rides = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Vehicle(models.Model):
    driver = models.OneToOneField('profiles.Driver', on_delete=models.CASCADE)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    registration_number = models.CharField(max_length=50)
    insurance_number = models.CharField(max_length=50)
    insurance_expiry_date = models.DateField()


class Document(models.Model):
    class Type(models.TextChoices):
        DRIVER_LICENSE = 'DL', "Driver's License"
        INSURANCE = 'INS', "Insurance"
        ID_CARD = 'ID', "Identification Card"

    driver = models.ForeignKey('profiles.Driver', on_delete=models.CASCADE)
    type = models.CharField(max_length=100, choices=Type.choices, default=Type.DRIVER_LICENSE)
    is_verified = models.BooleanField(default=False)
    file = models.FileField(upload_to="driver_documents/")


class BackgroundCheck(models.Model):
    driver = models.ForeignKey('profiles.Driver', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=(
        ('APRV', 'Approved'), 
        ('RJCT', 'Rejected')
    ))
    check_date = models.DateTimeField(auto_now_add=True)


class Rider(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rider_profile')
    rating = models.FloatField(default=0.0)
    preferred_vehicle_type = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email