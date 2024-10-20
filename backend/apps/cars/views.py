
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from apps.cars.serializers import CarSerializer
from apps.cars.filters import CarFilter
from apps.cars.models import CarModel



class CarsListView(ListAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    # pagination_class = None #відключаємо пагінацію
    filterset_class = CarFilter


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()



