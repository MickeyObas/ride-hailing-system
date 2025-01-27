from rest_framework import serializers

from django.core import exceptions
from django.conf import settings
from django.contrib.auth.password_validation import (
    validate_password
)
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from .models import User

from api.utils import send_confirmation_email


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    phone_number = serializers.CharField(max_length=15)
    type = serializers.CharField(max_length=6)

    class Meta:
        model = User
        fields = [
            'id',
            'type',
            'email',
            'phone_number',
            'first_name',
            'last_name',
            'password',
            'status',
            'is_verified'
        ]

        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, attrs):
        user = User(**attrs)
        password = attrs.get('password')
        errors = dict()

        try:
            validate_password(user=user, password=password)
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return super().validate(attrs)
    
    def validate_type(self, value):
        if value not in ['RIDER', 'DRIVER']:
            return serializers.ValidationError("Type must be either 'RIDER' or 'DRIVER'.")
        return value
    
    def validate_first_name(self, value):
        if not value.strip().isalpha():
            raise serializers.ValidationError("Please enter a valid name. Names can only contain letters.")
        return value.strip()
    
    def validate_last_name(self, value):
        if not value.strip().isalpha():
            raise serializers.ValidationError("Please enter a valid name. Names can only contain letters.")
        return value.strip()

    def validate_email(self, value):
        email = value.strip().lower()
        if User.objects.filter(
            email__iexact=email
        ).exists():
            raise serializers.ValidationError(f"An account with this email address already exists. Please use another one.")
        else:
            return email
        
    def validate_phone_number(self, value):
        phone_number = value.strip()

        for char in phone_number:
            if char not in "0123456789":
                raise serializers.ValidationError("Please enter a valid phone number.")

        if User.objects.filter(
            phone_number=phone_number
        ).exists():
            raise serializers.ValidationError(f"An account with this phone number already exists. Please use another one.")
        else:
            return phone_number

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        #TODO: Create Temp User? 
        token = PasswordResetTokenGenerator().make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        link = f"{settings.BACKEND_HOST}confirm-email/{uid}/{token}/"
        
        # Send link to email
        send_confirmation_email(user, token, uid)

        return user
    

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'phone_number',
            'first_name',
            'last_name',
        ]
    
    def validate_email(self, value):
        email = value.strip().lower()
        if User.objects.filter(
            email__iexact=email
        ).exists():
            raise serializers.ValidationError(f"An account with this email address already exists. Please use another one.")
        else:
            return email
        
    def validate_phone_number(self, value):
        phone_number = value.strip()

        for char in phone_number:
            if char not in "0123456789":
                raise serializers.ValidationError("Please enter a valid phone number.")

        if User.objects.filter(
            phone_number=phone_number
        ).exists():
            raise serializers.ValidationError(f"An account with this phone number already exists. Please use another one.")
        else:
            return phone_number
        
    def validate_first_name(self, value):
        if not value.strip().isalpha():
            raise serializers.ValidationError("Please enter a valid name. Names can only contain letters.")
        return value.strip()
    
    def validate_last_name(self, value):
        if not value.strip().isalpha():
            raise serializers.ValidationError("Please enter a valid name. Names can only contain letters.")
        return value.strip()