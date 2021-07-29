from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    pass

class Plant(models.Model):
    species = models.CharField(max_length=35)
    place = models.IntegerField(max_digits=1)
    startdate = models.DateTimeField(auto_now_add=True)
    showonlist = models.BooleanField(default=True)



#To be filled with simulator or admin control panel
class Height(models.Model):
    subject = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name="weight")
    height = models.DecimalField(max_digits=6, decimal_places=3)
    measuredate = models.DateTimeField(auto_now_add=True)

class LeafColors(models.Model):
    subject = models.ForeignKey(Plant, on_delete=models.CASCADE)
    colorpattern = models.CharField(max_length=35)  #will be url
    measuredate = models.DateTimeField(auto_now_add=True)

class DiseaseList(models.Model):
    name = models.CharField(max_length=35)
    description = models.CharField(max_length=350)

class Diseased(models.Model):
    subject = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name="disease")
    disease = models.ForeignKey(DiseaseList, on_delete=models.CASCADE)
    detectiondate = models.DateTimeField(auto_now_add=True)

#To be filled with user interface
class Harvest(models.Model):
    subject = models.ForeignKey(Plant, on_delete=models.CASCADE)
    quantity = models.IntegerField(max_digits=2)
    netweight = models.DecimalField(max_digits=5, decimal_places=3)
    date = models.DateTimeField(auto_now_add=True)

class PlantLog(models.Model):
    subject = models.ForeignKey(Plant, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    report = models.CharField(max_length=350)
    date = models.DateTimeField(auto_now_add=True)