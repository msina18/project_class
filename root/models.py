from django.db import models


class service (models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)

    class meta :
        ordering=['created_at']

    def __str__(self):
        return self.title
    

class Testimonials (models.Model):
    image=models.ImageField(upload_to='property',default='imags3.jpg')
    name=models.CharField(max_length=200)
    description=models.TextField(default='#')
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.name
    


# Create your models here.
