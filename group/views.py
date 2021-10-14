from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from .models import SubGroup
from posts.models import Post
from saidituser.models import SaidItUser
from django.views.generic import View


def group_detail(request, id):
    group = SubGroup.objects.get(id=id)
    posts = Post.objects.filter(posted_in=group.id)
    member_count = SaidItUser.objects.filter(id=id).count()
    return render(request, "group_detail.html", {"group": group, "posts": posts, 'member_count':member_count}) # noqa

@login_required
def join_group(request, id):
    newMember = request.user
    group = SubGroup.objects.get(id=id)
    group.member.add(newMember)
    group.save()
    print('joined')
    return redirect(request.META.get('HTTP_REFERER'))


def leave_group(request, id):
    newMember = request.user
    group = SubGroup.objects.get(id=id)
    group.member.remove(newMember)
    group.save()
    print('joined')
    return redirect(request.META.get('HTTP_REFERER'))


class GroupListView(View):
    def get(self, request):
        groups = SubGroup.objects.all()
        return render(request, "group_list.html", {"groups": groups})
