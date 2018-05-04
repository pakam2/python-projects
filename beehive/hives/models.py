from django.db import models
from datetime import datetime


# Create your models here.

class HiveModel(models.Model):
    numberOfHive = models.IntegerField(null=False)
    firstFrame = models.DecimalFiled(max_digits=3, decimal_places=2, null=False)
    secondFrame = models.DecimalField(max_digits=3, decimal_places=2, null=False)
    thirdFrame = models.DecimalField(max_digits=3, decimal_places=2, null=False)
    motherBee = models.BooleanField(default=False, null=False)
    date = models.DateTimeField(default=datetime.now, blank=True)
    comments = models.CharField(max_length=500)
