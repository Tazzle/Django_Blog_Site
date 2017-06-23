from django.db import models

# Create your models here.

class BlogPost(models.Model):
    body = models.TextField()
    title = models.CharField(max_length=500, default='')
    timestamp = models.CharField(max_length=50, default='')
    tags = models.CharField(max_length=200, default='')

    class Admin:
        pass



