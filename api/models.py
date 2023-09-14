from django.db import models
from django.urls import reverse

# Create your models here.
class Persons(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(null= True, blank=True)
    nationality = models.CharField(max_length=200)
    state_of_origin = models.CharField(max_length=200)
    occupation = models.CharField(max_length=200)

    
    # def get_absolute_url(self, *args, **kwargs):
    #     return reverse('')