from django.db import models

# Create your models here.
class PostLikes(models.Model):
    likes = models.BooleanField(default=False)

# class Comments(models.Model):
