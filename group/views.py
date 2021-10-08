from django.shortcuts import render
from .models import SubGroup
from posts.models import Post


def group_detail(request, id):
    group = SubGroup.objects.get(id=id)
    posts = Post.objects.filter(posted_in=group.id)
    return render(request, "group_detail.html", {"group": group, "posts": posts}) # noqa
# Create your views here.
