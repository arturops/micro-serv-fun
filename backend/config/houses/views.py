import random

from rest_framework import viewsets
from rest_framework import status
from rest_framework import APIView
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
    
    def retrieve(self, request, pk=None):
        house = House.objects.get(id=pk)
        house_serializer = HouseSerializer(house)
        return Response(house_serializer.data)
    
    def update(self, request, pk=None):
        house = House.objects.get(id=pk)
        house_serializer = HouseSerializer(instance=house, data=request.data)
        house_serializer.is_valid(raise_exception=True)
        house_serializer.save()
        return Response(house_serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        house = House.objects.get(id=pk)
        house.delete()
        return Response(status=status.HTTP_404_NO_CONTENT)

class CheckerAPIView(APIView):
    def get(self, request):
        checkers = Checker.objects.all()
        checker = random.choice(checkers)
        return Response({"id": checker.id})
