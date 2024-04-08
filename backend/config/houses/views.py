from rest_framework import viewsets
from rest_framework import status

from rest_framework.response import Response

from .models import Checker
from .models import House
from .serializers import HouseSerializer

class HouseViewSet(viewsets.ViewSet):
    def list(self, request):
        houses = House.objects.all()
        houses_serializer = HouseSerializer(houses, many=True)
        return Response(houses_serializer.data)

    def create(self, request):
        house_serializer = HouseSerializer(data=request.data)
        house_serializer.is_valid(raise_exception=True)
        house_serializer.save()
        return Response(house_serializer.data, status=status.HTTP_201_CREATED)
    
    
