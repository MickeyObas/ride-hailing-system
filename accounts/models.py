from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.conf import settings

from .managers import (
    CustomUserManager,
    ActiveUserManager
)
from api.models import BaseModel

class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Status(models.TextChoices):
        ACTIVE = 'ACTIVE', 'Active'
        BANNED = 'BANNED', 'Banned'

    email = models.EmailField(_("email address"), unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True, unique=True)
    first_name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=140)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVE)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_seen = models.DateTimeField(null=True, blank=True)
    is_first_login = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    active = ActiveUserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email
    

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



