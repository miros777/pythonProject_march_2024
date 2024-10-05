from django.db import models

from core.models import BaseModel

from apps.autoparks.models import AutoParksModel


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    price = models.IntegerField()

    autopark = models.ForeignKey(AutoParksModel, on_delete=models.CASCADE, related_name='cars')


