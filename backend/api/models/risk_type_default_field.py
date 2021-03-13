from django.db import models

from .risk_type import RiskType
from .field import Field

class RiskTypeDefaultField(models.Model):
    risk_type = models.ForeignKey(RiskType, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['risk_type', 'field'], name = 'risk_type_default_field_primary_constraint')
        ]