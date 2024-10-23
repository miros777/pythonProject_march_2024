from rest_framework import serializers

from apps.cars.models import CarModel

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        # fields = '__all__'
        fields = ('id', 'model', 'body_type', 'price', 'year', 'created_at', 'update_at')

    def validate(self, car):
        if car['model'] == 'KIA':
            raise serializers.ValidationError("KIA is not available")
        return car

    def validate_price(self, price):
        if price < 100:
            raise serializers.ValidationError("Price must be more 100")
        return price

class CarPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('photo',)
        extra_kwargs = {'photo': {'required': True}}