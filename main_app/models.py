from django.db import models
from django.contrib.auth.models import User

# Create your models here.

MAINTENANCE = (
    ('P', 'Played and Cleaned'),
    ('C', 'Played and not Cleaned'),
    ('D', 'Record Got Damaged')
)

class CleaningBrush(models.Model):
  brand = models.CharField(max_length=50)
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

class Record(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField( max_length=100)
    format = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    genre = models.CharField(max_length=100)
    released = models.CharField(max_length=100)
    # Adding M:M to association
    cleaning_brush = models.ManyToManyField(CleaningBrush, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Played(models.Model):
  date = models.DateField('Date Record Was Played')
  maintenance = models.CharField(max_length=1,
    choices=MAINTENANCE,
    default=MAINTENANCE[0][0]
    )
  record = models.ForeignKey(Record, on_delete=models.CASCADE)

  def __str__(self):
      return f"{self.get_maintenance_display()} on {self.date}"
      
  class Meta:
    ordering = ['-date'] 
