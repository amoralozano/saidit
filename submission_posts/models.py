from django.db import models

# Create your models here.
class Posts(models.Model):
    likes = models.BooleanField(default=False)

# class Comments(models.Model):
