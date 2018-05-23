from django.db import models

# Create your models here.

# A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.

from django.contrib.auth.models import User


class Cat(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    age = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
