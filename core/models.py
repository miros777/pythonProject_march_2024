from django.db import models

class BaseModel(models.Model):
    class Meta:
        abstract  = True

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
