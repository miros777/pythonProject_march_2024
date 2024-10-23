
from django.urls import path

from .views import CarRetrieveUpdateDestroyView, CarsListView, CarAddPhotoView

urlpatterns = [
    path('', CarsListView.as_view(), name='cars_list'),
    path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view(), name='cars_retrieve_update_destroy'),
    path('/<int:pk>/photos', CarAddPhotoView.as_view(), name='cars_add_photo'),
]
