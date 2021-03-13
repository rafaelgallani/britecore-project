from django.db import models
from .risk_type import RiskType

class Risk(models.Model):
    name = models.TextField()
    description = models.TextField()
    risk_type = models.ForeignKey(RiskType, on_delete=models.CASCADE)
