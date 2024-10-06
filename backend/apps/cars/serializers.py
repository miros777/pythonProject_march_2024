from rest_framework import serializers

from apps.cars.models import CarModel

# class CarSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     model = serializers.CharField(max_length=50)
#     price = serializers.IntegerField()
#     year = serializers.IntegerField()
#     created_at = serializers.DateTimeField(read_only=True)
#     update_at = serializers.DateTimeField(read_only=True)
#
#     def create(self, validated_data:dict):
#         car = CarModel.objects.create(**validated_data)
#         return car
#
#     def update(self, instance, validated_data:dict):
#         for key, value in validated_data.items():
#             setattr(instance, key, value)
#         instance.save()
#         return instance

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