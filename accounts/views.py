from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import User

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode


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
    
