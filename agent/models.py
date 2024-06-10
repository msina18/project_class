from django.db import models
from django.contrib.auth.models import User


class Agent(models.Model):
      user=models.ForeignKey(User,on_delete=models.CASCADE)
      image=models.ImageField(upload_to='property',default='1.jpg') 
      descriptions=models.TextField(default='#')
      phon=models.IntegerField(default='0918')
      email=models.EmailField(default='.com')
      facebook=models.CharField(max_length=220,default='#')
      instegram=models.CharField(max_length=220,default='#')
      linkdin=models.CharField(max_length=220,default='#')
      X=models.CharField(max_length=220,default='#')

      def __str__(self):
          return self.user.username
      
# Create your models her


