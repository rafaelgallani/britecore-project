from django.db import models
from .risk_type import RiskType
from .field import Field

class Risk(models.Model):
    name = models.TextField()
    description = models.TextField()
    risk_type = models.ForeignKey(RiskType, on_delete=models.CASCADE)

    fields = models.ManyToManyField(Field, through='RiskField')