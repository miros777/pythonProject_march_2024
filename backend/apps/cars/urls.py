
from django.urls import path

from .views import CarRetrieveUpdateDestroyView, CarsListView

urlpatterns = [
    path('', CarsListView.as_view(), name='cars_list'),
    path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view(), name='cars_retreive_update_destroy'),
]
