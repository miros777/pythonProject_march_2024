from django.core.serializers import serialize
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.cars.models import CarModel
from rest_framework.generics import get_object_or_404, GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.cars.serializers import CarSerializer
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin, DestroyModelMixin

# class CarsListCreateView(GenericAPIView):
#     serializer_class = CarSerializer
#
#     def get(self, *args, **kwargs):
#         cars = CarModel.objects.all()
#         serializer = self.get_serializer(cars, many=True)
#         # cars = [model_to_dict(car) for car in cars]
#         # cars = serializer.data
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         # Валідуємо за допомогою Serializer
#         serializer = self.get_serializer(data=data)
#         # if not serializer.is_valid():
#         #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         # car = CarModel.objects.create(**serializer.data)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)


# class CarRetrieveUpdateDestroyView(GenericAPIView):
#     queryset = CarModel.objects.all()
#
#     def get(self, *args, **kwargs):
#         # pk = kwargs['pk']
#
#         # try:
#         #     car = CarModel.objects.get(pk=pk)
#         # except:
#         #     return Response(status=status.HTTP_200_OK)
#
#
#         # car = get_object_or_404(CarModel, pk=pk)
#         car = self.get_object()
#         serializer = CarSerializer(car)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
#     def put(self, *args, **kwargs):
#         # pk = kwargs['pk']
#         data = self.request.data
#
#         # try:
#         #     car = CarModel.objects.get(pk=pk)
#         # except:
#         #     return Response(status=status.HTTP_200_OK)
#         car = self.get_object()
#         serializer = CarSerializer(car, data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         # без S
#         # car.model = data['model']
#         # car.price = data['price']
#         # car.year = data['year']
#         # car.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
#     def patch(self, *args, **kwargs):
#         # pk = kwargs['pk']
#         data = self.request.data
#
#         # try:
#         #     car = CarModel.objects.get(pk=pk)
#         # except:
#         #     return Response(status=status.HTTP_200_OK)
#         # partial=True не буде вимагати всі поля, буде валідувати ті що є
#         car = self.get_object()
#         serializer = CarSerializer(car, data, partial=True)
#
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
#     def delete(self, *args, **kwargs):
#         # pk = kwargs['pk']
#         #
#         # try:
#         #     CarModel.objects.get(pk=pk).delete()
#         # except:
#         #     return Response(status=status.HTTP_404_NOT_FOUND)
#         self.get_object().delete()
#
#         return Response(status=status.HTTP_204_NO_CONTENT)

# mixins
# class CarsListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
#     serializer_class = CarSerializer
#     queryset = CarModel.objects.all() # для get
#
#     def post(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)
#
#     def get(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
#
#
# class CarRetrieveUpdateDestroyView(GenericAPIView, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
#     serializer_class = CarSerializer
#     queryset = CarModel.objects.all()
#
#     def put(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)
#
#     def get(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return super().partial_update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)


class CarsListCreateView(ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all() # для get



class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()



