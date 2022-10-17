from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class AHT20(models.Model):
    temperature = models.fields.FloatField(default=0.0)
    humidite = models.fields.FloatField(default=0.0)
