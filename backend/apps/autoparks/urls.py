from django.urls import path

from .views import AutoParkAddCarView, AutoParkListCreateAPIView

urlpatterns = [
    path('', AutoParkListCreateAPIView.as_view(), name='autopark_list_create'),
    path('/<int:pk>/cars', AutoParkAddCarView.as_view(), name='autopark_add_car'),
]