from rest_framework.decorators import (
    api_view,
    permission_classes
)
from rest_framework import status
from rest_framework.response import Response

from django.contrib.auth import (
    authenticate,
    login as django_login,
    logout as django_logout,
)

from accounts.serializers import UserSerializer
from .utils import is_valid_email

import re



@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        response = Response(serializer.data, status=status.HTTP_201_CREATED)
        response.data['message'] = "We just sent a confirmation link. Please check your email."
        return response
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    email = request.data.get('email', None)
    password = request.data.get('password', None)

    if not email:
        return Response({'email': 'Please enter your email address.'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        email = email.lower()
    
    if not is_valid_email(email):
        return Response({'email': 'Please enter a valid email address.'})
    
    if not password:
        return Response({'password': 'Please enter your password.'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = authenticate(request, email=email, password=password)

    if user is not None:
        django_login(request, user)
        print("Logged In")
    else:
        return Response({'error': 'Invalid Credentials'})
    
    return Response({'test': 'test'})
