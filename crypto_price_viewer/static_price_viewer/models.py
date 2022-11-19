from django.db import models
from datetime import time
# Create your models here.


class Price(models.Model):
    ## Defining Schema ##
    currentTime=models.TimeField(default=time(9))
    currency = models.CharField(max_length=200)
    price = models.FloatField()

