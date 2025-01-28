from rest_framework import serializers

from .models import (
    Rider,
    Driver,
    Vehicle,
    Document
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
            'id',
            'user',
            'rating',
            'is_available'
        ]

class DocumentSerializer(serializers.ModelSerializer):
    driver = serializers.PrimaryKeyRelatedField(queryset=Driver.objects.all())

    class Meta:
        model = Document
        fields = [
            'driver',
            'type',
            'is_verified',
            'file'
        ]
        extra_kwargs = {
            'file': {'write_only': True}
        }

    def create(self, validated_data):
        # Extra attributes
        document = Document.objects.create(**validated_data)
        return document