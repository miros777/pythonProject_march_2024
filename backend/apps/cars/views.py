
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from apps.cars.serializers import CarSerializer
from apps.cars.filters import CarFilter
from apps.cars.models import CarModel
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly



class CarsListView(ListAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    # pagination_class = None #відключаємо пагінацію
    filterset_class = CarFilter
    permission_classes = (IsAuthenticated, )


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()



