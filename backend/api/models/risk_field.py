from django.db import models

from .risk import Risk
from .field import Field

class RiskField(models.Model):
    risk = models.ForeignKey(Risk, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['risk', 'field'], name = 'risk_field_primary_constraint')
        ]

