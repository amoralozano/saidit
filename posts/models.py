from django.db import models
from saidituser.models import SaidItUser
from django.utils import timezone
from group.models import SubGroup


class Post(models.Model):
    user = models.ForeignKey(SaidItUser, on_delete=models.CASCADE)
    posted_in = models.ForeignKey(SubGroup, on_delete=models.CASCADE)
    body = models.CharField(max_length=150)
    time_created = models.DateTimeField(default=timezone.now)
    # notification

    def __str__(self):
        return self.body



