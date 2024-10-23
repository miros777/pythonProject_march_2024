from django.core.serializers import serialize

from rest_framework import status
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.response import Response

from apps.auto_parks.models import AutoParkModel
from apps.auto_parks.serializers import AutoParkSerializer
from apps.cars.serializers import CarSerializer


class AutoParkListCreateAPIView(ListCreateAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParkModel.objects.all()

class AutoParkAddCarView(CreateAPIView):
    queryset = AutoParkModel.objects.all()

    def post(self, *args, **kwargs):
        data  =self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        auto_park  = self.get_object()
        serializer.save(autopark=auto_park) #serializer.save(auto_park_id=auto_park.id)
        park_serializer = AutoParkSerializer(auto_park)
        return Response(park_serializer.data, status=status.HTTP_201_CREATED)
