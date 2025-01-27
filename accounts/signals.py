from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User

from profiles.models import (
    Rider,
    Driver
)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.type == 'RIDER':
            Rider.objects.create(
                user=instance
            )
        elif instance.type == "DRIVER":
            Driver.objects.create(
                user=instance
            )