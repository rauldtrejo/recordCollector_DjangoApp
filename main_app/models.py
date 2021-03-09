from django.db import models

# Create your models here.

class Record(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField( max_length=100)
    format = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    genre = models.CharField(max_length=100)
    released = models.CharField(max_length=100)

