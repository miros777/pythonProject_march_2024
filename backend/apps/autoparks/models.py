from django.db import models

from core.models import BaseModel


class AutoParksModel(BaseModel):
    class Meta:
        db_table = 'autoparks'

    name = models.CharField(max_length=20)


