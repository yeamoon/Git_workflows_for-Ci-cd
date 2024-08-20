from django.db import models
from datetime import datetime

class Productowner(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    top_seller = models.BooleanField(default=False)
    

    def __str__(self):
        return self.name