from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from .models import SubGroup
from posts.models import Post
from saidituser.models import SaidItUser


def group_detail(request, id):
    group = SubGroup.objects.get(id=id)
    posts = Post.objects.filter(posted_in=group.id)
    member_count = SaidItUser.objects.filter(id=id).count()
    return render(request, "group_detail.html", {"group": group, "posts": posts, 'member_count':member_count}) # noqa


def join_group(request, id):
    newMember = request.user
    group = SaidItUser.objects.get(id=id)
    newMember.member.add(group)
    newMember.save()
    print('joined')
    return redirect(request.META.get('HTTP_REFERER'))
# Create your views here.
