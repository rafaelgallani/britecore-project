from django.db import models

class RiskType(models.Model):
    name = models.TextField()
    description = models.TextField()
