from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blogpost(models.Model):
    month = models.CharField(max_length=20)
    date = models.IntegerField()
    year = models.IntegerField()
    comment_no = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    full_decription = models.TextField()




  
