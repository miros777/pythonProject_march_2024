from django.core.serializers import serialize
from django.template.defaulttags import querystring
from rest_framework.response import Response

from apps.cars.filters import car_filter_queryset
from apps.cars.models import CarModel
from rest_framework.generics import get_object_or_404, GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

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
class CarsListCreateView(ListCreateAPIView):

    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        return car_filter_queryset(self.request.query_params)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()



