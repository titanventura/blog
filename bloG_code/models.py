from django.db import models
# from django.models import User

# Create your models here.

class Blog_code(models.Model):
    heading         = models.CharField(max_length=100)
    read_time       = models.IntegerField(default=0)
    content         = models.TextField()
    image           = models.URLField(null=True)
    description     = models.CharField(max_length=250,blank=True)
