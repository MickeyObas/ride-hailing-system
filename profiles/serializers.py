from rest_framework import serializers

from .models import (
    Rider,
    Driver
)


class RiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rider
        fields = [
            'user',
            'rating',
            'preferred_vehicle_type'
        ]

class RiderProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rider
        fields = [
            'rating'
        ]
        

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = [
            'user',
            'rating',
            'is_available'
        ]