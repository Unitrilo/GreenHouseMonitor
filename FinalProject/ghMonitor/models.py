from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    pass

class Plant(models.Model):
    species = models.CharField(max_length=35)

class Weight(models.Model):
    subject = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name="weight")
    mass = models.DecimalField(max_digits=5, decimal_places=3)
    date = models.DateField()

class Fruits(models.Model):
    subject = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name="weight")
    date = models.DateField()