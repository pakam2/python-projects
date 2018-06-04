from django.db import models
from datetime import datetime
from django.contrib.auth.models import User, AbstractUser


# Create your models here.

class HiveModel(models.Model):
    numberOfHive = models.IntegerField(null=False, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    additional_info = models.CharField(max_length=500)

class HiveDataModel(models.Model):
    firstFrame = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    secondFrame = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    thirdFrame = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    motherBee = models.BooleanField(default=False)
    addInformationDate = models.DateField(auto_now_add=True)

    hive = models.ForeignKey(HiveModel, on_delete=models.CASCADE)



    
