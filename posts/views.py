from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from posts.forms import AddPostForm
from posts.models import Post
from saidituser.models import SaidItUser
from group.forms import AddSubGroup
from group.models import SubGroup
from django.views.generic import View

from reply.models import Reply


def index(request):
    posts = Post.objects.all()
    groups = SubGroup.objects.all()
    return render(request, 'index.html', {'posts': posts, "groups": groups})


@login_required
def addPost(request, id):
    group = SubGroup.objects.get(id=id)
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                user=request.user,
                body=data['body'],
                posted_in=group
            )
        return redirect("group-detail", group.id)
    form = AddPostForm()
    return render(request, 'addpost.html', {'form': form, 'group': group})


class PostView(View):
    def get(self, request, post_id):
        template_name = "post_detail.html"
        post = Post.objects.get(id=post_id)
        replies = Reply.objects.filter(replied_to=post_id)
        context = {"post": post, "replies": replies}
        return render(request, template_name, context)
