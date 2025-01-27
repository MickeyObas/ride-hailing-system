from rest_framework import status
from rest_framework.decorators import (
    api_view,
    parser_classes
)
from rest_framework.response import Response
from rest_framework.parsers import (
    MultiPartParser,
    JSONParser
)

from .serializers import (
    RiderSerializer,
    DriverSerializer,
    DocumentSerializer
)
from .models import (
    Rider,
    Driver
)

# RIDER ENDPOINTS
@api_view(['GET'])
def riders_list(request):
    riders = Rider.objects.all()
    serializer = RiderSerializer(riders, many=True)
    return Response(serializer.data)


# DRIVER ENDPOINTS
@api_view(['GET'])
def drivers_list(request):
    drivers = Driver.objects.all()
    serializer = DriverSerializer(drivers, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@parser_classes([MultiPartParser])
def document_upload(request):
    serializer = DocumentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)