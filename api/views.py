from rest_framework.decorators import (
    api_view,
    permission_classes
)
from rest_framework import status
from rest_framework.response import Response

from accounts.serializers import UserSerializer


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    pass
