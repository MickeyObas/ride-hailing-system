from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import (
    RiderSerializer,
    DriverSerializer
)
from .models import (
    Rider,
    Driver
)


@api_view(['GET'])
def riders_list(request):
    riders = Rider.objects.all()
    serializer = RiderSerializer(riders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def drivers_list(request):
    drivers = Driver.objects.all()
    serializer = DriverSerializer(drivers, many=True)
    return Response(serializer.data)