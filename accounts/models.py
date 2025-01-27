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

    class Type(models.TextChoices):
        RIDER = 'RIDER', 'Rider'
        DRIVER = 'DRIVER', 'Driver'


    type = models.CharField(max_length=6, choices=Type.choices, default=Type.RIDER)
    email = models.EmailField(_("email address"), unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
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
    





