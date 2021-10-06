from django.db import models
from saidituser.models import SaidItUser
from django.utils import timezone


class Post(models.Model):
    user = models.ForeignKey(SaidItUser, on_delete=models.CASCADE, default=1)
    # group = models.ForeignKey()
    body = models.CharField(max_length=150)
    time_created = models.DateTimeField(default=timezone.now)
    # notification

    def __str__(self):
        return self.body


class The_Groups(models.Model):
    group_name = models.CharField(max_length=30)
    group_description = models.TextField(null=True, blank=False)
    time_created = models.DateTimeField(default=timezone.now)
    users = models.ForeignKey(SaidItUser, on_delete=models.CASCADE, default=1)  # noqa # need to look at this one
    posts = models.ForeignKey(Post, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.group_name
