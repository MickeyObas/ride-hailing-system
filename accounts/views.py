from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import User
from .serializers import UserSerializer

from profiles.models import (
    Rider,
    Driver
)
from profiles.serializers import (
    RiderSerializer,
    DriverSerializer
)

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode



@api_view(['GET'])
def users_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['PATCH'])
def user_update(request, pk):
    pass


@api_view(['GET'])
def confirm_email(request, uid, token):
    try:
        user_id = urlsafe_base64_decode(uid).decode()
        user = User.objects.get(id=user_id)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        return Response({'error': 'This link is invalid.'})
    
    if PasswordResetTokenGenerator().check_token(user, token):
        user.is_verified = True
        user.save()
        return Response({"message": "Email confirmed!"})
    
    return Response({"error": "Invalid or expired link"}, status=400)
    
