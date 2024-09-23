
from apps.cars.models import CarModel
from rest_framework.generics import get_object_or_404, GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.cars.serializers import CarSerializer

class CarsListCreateView(GenericAPIView):
    # serializer_class = CarSerializer
    # queryset = CarModel.objects.all() # для get

    serializer_class = CarSerializer
    queryset = CarModel.objects.all() # для get




class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()



