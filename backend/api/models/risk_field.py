from django.db import models

from .risk import Risk
from .field import Field

class RiskField(models.Model):
    risk = models.ForeignKey(Risk, on_delete=models.CASCADE, related_name="fields")
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    value = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['risk', 'field'], name = 'risk_field_primary_constraint')
        ]

