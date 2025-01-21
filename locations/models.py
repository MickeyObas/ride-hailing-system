from django.db import models


class Location(models.Model):
    driver = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    location = models.CharField(max_length=140)
    timestamp = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)