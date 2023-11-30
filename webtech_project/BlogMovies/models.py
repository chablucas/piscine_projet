from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 90)
    content = models.TextField(null = True)
    #activate = models.BooleanField(default = True)
    date = models.DateField(null = True)
    active = models.BooleanField(default = True)
    author = models.CharField(max_length=90)
    
    def __str__(self):
        return self.title
    


   