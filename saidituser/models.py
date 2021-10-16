from django.db import models
from django.contrib.auth.models import AbstractUser




class SaidItUser(AbstractUser):
    display_name = models.CharField(max_length=30)
    age = models.IntegerField(null=True, blank=True)
    bio = models.TextField(null=True, blank=False)
    
    following = models.ManyToManyField("self", blank =True, related_name="followers", symmetrical=False) # noqa
    # notifications
    # display picture
    # friends or followers
    # followers / friends count
    # favorites

    def __str__(self):
        return self.username