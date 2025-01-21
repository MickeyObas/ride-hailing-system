from django.db import models


class Rating(models.Model):
    ride = models.ForeignKey('rides.Ride', on_delete=models.CASCADE)
    rider = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='rider_ratings')
    driver = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='driver_ratings')
    rating = models.IntegerField() 
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
