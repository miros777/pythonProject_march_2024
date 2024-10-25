from datetime import datetime

from django.core import validators as V
from django.db import models

from core.models import BaseModel

from apps.auto_parks.models import AutoParkModel
from apps.cars.choices import BodyTypeChoice
from apps.cars.managers import CarManager
from apps.cars.regex import CarRegex
from apps.cars.services import upload_car_photo


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'
    # model = models.CharField(max_length=50, validators=[V.RegexValidator(CarRegex.MODEL.pattern, CarRegex.MODEL.msg)])
    #або
    model = models.CharField(max_length=50, validators=[V.RegexValidator(*CarRegex.MODEL.value)])
    body_type = models.CharField(max_length=9, choices=BodyTypeChoice.choices)
    price = models.IntegerField(validators=[V.MinValueValidator(1), V.MaxValueValidator(1000000)])
    year = models.IntegerField(validators=[V.MinValueValidator(1999), V.MaxValueValidator(datetime.now().year)])
    auto_parks = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')

    objects = CarManager()

class CarPhotoModel(BaseModel):
    class Meta:
        db_table = 'car_photos'
    photo = models.ImageField(upload_to=upload_car_photo, blank=True)
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='photos')


