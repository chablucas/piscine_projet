from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=90)
    author = models.CharField(max_length=90)
    content = models.TextField(null=True)
    date = models.DateField(null=True)
    active = models.BooleanField(default=True)
    

    def __str__(self):
        return self.title