from django.db import models
from django.utils import timezone
from saidituser.models import SaidItUser

# Create your models here.


class Reply(models.Model):
    reply_text = models.TextField()
    date_replied = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(SaidItUser, on_delete=models.CASCADE)
    # post replied to fk


    def __str__(self):
        return str(self.reply_text)