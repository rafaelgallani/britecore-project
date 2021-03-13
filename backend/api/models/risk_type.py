from django.db import models
from .field import Field

class RiskType(models.Model):
    name = models.TextField()
    description = models.TextField()

    fields = models.ManyToManyField(Field, through='RiskTypeDefaultField')
