from functools import partial
from django.db import models
from django.utils import timezone
from saidituser.models import SaidItUser
from posts.models import Post
from mptt.models import MPTTModel, TreeForeignKey


class Reply(MPTTModel):
    reply_text = models.TextField()
    date_replied = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(SaidItUser,default= timezone.now, on_delete=models.CASCADE)
    replied_to = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="replies")
    parent = TreeForeignKey("self", on_delete=models.CASCADE,null=True, blank=True, related_name='children')
    like_dislike = models.BooleanField(default=False, choices=((True, 'like'), (False, 'dislike'))
    )
    # like/dislike?


    class MPTTMeta:
        order_insertion_by = ["date_replied"]
    def __str__(self):
        return str(self.reply_text)