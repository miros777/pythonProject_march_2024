from datetime import datetime

from django.core import validators as V
from django.db import models

from apps.cars.managers import CarManager
from core.models import BaseModel

from apps.autoparks.models import AutoParksModel
from apps.cars.choices import BodyTypeChoice
from apps.cars.regex import CarRegex


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'
    # model = models.CharField(max_length=50, validators=[V.RegexValidator(CarRegex.MODEL.pattern, CarRegex.MODEL.msg)])
    #або
    model = models.CharField(max_length=50, validators=[V.RegexValidator(*CarRegex.MODEL.value)])
    body_type = models.CharField(max_length=9, choices=BodyTypeChoice.choices)
    price = models.IntegerField(validators=[V.MinValueValidator(1), V.MaxValueValidator(1000000)])
    year = models.IntegerField(validators=[V.MinValueValidator(1999), V.MaxValueValidator(datetime.now().year)])
    autopark = models.ForeignKey(AutoParksModel, on_delete=models.CASCADE, related_name='cars')

    objects = CarManager()


