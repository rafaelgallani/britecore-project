from django.db import models

class RiskType(models.Model):
    name = models.TextField()
    description = models.TextField()

class Field(models.Model):

    class FieldType(models.TextChoices):
        TEXT = 'TEXT', 'Text'
        NUMBER = 'NUMBER', 'Number'
        DATE = 'DATE', 'Date'
        ENUM = 'ENUM', 'Enum'

    name = models.TextField()
    field_type = models.TextField(choices=FieldType.choices)

class FieldValue(models.Model):
    label = models.TextField()
    value = models.TextField()
    field = models.ForeignKey(Field, on_delete=models.CASCADE)

class Risk(models.Model):
    name = models.TextField()
    description = models.TextField()
    risk_type = models.ForeignKey(RiskType, on_delete=models.CASCADE)

class RiskField(models.Model):
    risk = models.ForeignKey(Risk, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['risk', 'field'], name = 'risk_field_primary_constraint')
        ]

class RiskTypeDefaultField(models.Model):
    risk_type = models.ForeignKey(RiskType, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['risk_type', 'field'], name = 'risk_type_default_field_primary_constraint')
        ]