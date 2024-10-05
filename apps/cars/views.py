
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.cars.filters import car_filter_queryset
from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer


# class CarsListCreateView(GenericAPIView):
#
#     def get(self, *args, **kwargs):
#         query  = self.request.query_params
#         cars = car_filter_queryset(query)
#         serializer = CarSerializer(cars, many=True)
#
#         return Response(serializer.data)
#     або
class CarsListView(CreateAPIView):
    serializer_class = CarSerializer


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()



