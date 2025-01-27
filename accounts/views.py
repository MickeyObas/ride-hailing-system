from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import User
from .serializers import (
    UserSerializer, 
    UserUpdateSerializer
)



from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode


# USER ENDPOINTS
@api_view(['GET'])
def users_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['PATCH'])
def user_update(request, pk):
    try:
        user = User.objects.get(id=pk)
        serializer = UserUpdateSerializer(user, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response({'error': f'There is no user with ID: {pk}'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)})

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
    