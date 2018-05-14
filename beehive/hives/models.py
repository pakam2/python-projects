from django.db import models
from datetime import datetime


# Create your models here.

class HiveModel(models.Model):
    numberOfHive = models.IntegerField(null=False, unique=True)
    firstFrame = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    secondFrame = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    thirdFrame = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    motherBee = models.BooleanField(default=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    comments = models.CharField(max_length=500)
