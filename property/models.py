from django.db import models
from django.contrib.auth.models import User

class category(models.Model):
    title=models.CharField(max_length=200)
    statuse=models.BooleanField(default=True)

    def __str__(self):
        return self.title

class property(models.Model):
    image=models.ImageField(upload_to='property',default='default1.jpg')  
    title=models.CharField(max_length=200)
    category=models.ManyToManyField(category)
    rent = models.IntegerField(default=0)
    area = models.IntegerField(default=0)
    beds = models.IntegerField(default=0)
    baths = models.IntegerField(default=0)
    garages = models.IntegerField(default=0)
    view = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.title
     
    
# Create your models here.
