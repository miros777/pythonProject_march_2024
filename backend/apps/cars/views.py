
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from apps.cars.filters import CarFilter
from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser,IsAuthenticatedOrReadOnly


class CarsListView(ListAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.less_than_year(2001).only_audi()
    pagination_class = None #відключаємо пагінацію
    filterset_class = CarFilter
    permission_classes = (IsAuthenticated,)

class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()



