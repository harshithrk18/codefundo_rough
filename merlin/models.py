from django.db import models

# Create your models here.
class Ngo(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=5000)
    website = models.URLField(max_length=200)
    email = models.EmailField(max_length=200)
    contact = models.PositiveIntegerField()


class ReliefCamp(models.Model):
    title = models.CharField(max_length=200)
    lat = models.FloatField()
    long = models.FloatField()
    image = models.ImageField()
