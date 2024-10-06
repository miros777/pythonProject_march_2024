from django.core.serializers import serialize

from rest_framework import status
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.response import Response

from apps.autoparks.models import AutoParksModel
from apps.autoparks.serializers import AutoParkSerializer
from apps.cars.serializers import CarSerializer


class AutoParkListCreateAPIView(ListCreateAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParksModel.objects.all()


class AutoParkAddCarView(CreateAPIView):
    queryset = AutoParksModel.objects.all()

    def post(self, *args, **kwargs):
        data  =self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        autopark  = self.get_object()
        serializer.save(autopark=autopark) #serializer.save(auto_park_id=auto_park.id)
        park_serializer = AutoParkSerializer(autopark)
        return Response(park_serializer.data, status=status.HTTP_201_CREATED)
