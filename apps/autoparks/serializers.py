from rest_framework import serializers

from apps.autoparks.models import AutoParksModel
from apps.cars.serializers import CarSerializer


class AutoParkSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)
    class Meta:
        model = AutoParksModel
        fields = ('id', 'name', 'created_at', 'update_at', 'cars')
        read_only_fields = ('id', 'created_at', 'update_at')
        # depth = 1 # скільки рівнів вглиб
