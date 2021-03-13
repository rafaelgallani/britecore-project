from django.db import models

class Field(models.Model):

    class FieldType(models.TextChoices):
        TEXT = 'TEXT', 'Text'
        NUMBER = 'NUMBER', 'Number'
        DATE = 'DATE', 'Date'
        ENUM = 'ENUM', 'Enum'

    name = models.TextField()
    field_type = models.TextField(choices=FieldType.choices)

