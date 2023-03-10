from django.db import models
from django.urls import reverse


# Create your models here.
class Days(models.Model):
    day = models.CharField(max_length=40)

    def __str__(self):
       return self.day
class Post(models.Model):
    days = models.ForeignKey(Days,on_delete=models.CASCADE)
    text = models.CharField(max_length=400)
    def __str__(self):
       return self.text
    def get_absoult_url(self):
        return reverse ('day',qwarks = {'day' : self.day })
