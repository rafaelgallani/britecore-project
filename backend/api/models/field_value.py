from django.db import models
from .field import Field

class FieldValue(models.Model):
    label = models.TextField()
    value = models.TextField()
    field = models.ForeignKey(Field, on_delete=models.CASCADE)

