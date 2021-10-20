from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from .models import Reply
from django.views.generic import View
from .forms import ReplyForm
from posts.models import Post
# Create your views here.




class ReplyDetailView(View):
    def get(self, request, reply_id):
        template_name = "reply_detail.html"
        reply = Reply.objects.get(id=reply_id)
        init_reply = reply
        replies = reply.get_descendants(include_self=False)
        context = {
                    "init_reply": init_reply,
                    "replies": replies
                    }
        return render(request, template_name, context)


def toggle_like(request, id):
    like = Reply.objects.get(id=id)
    like.like_dislike = not like.like_dislike
    like.save()
    return HttpResponseRedirect(reverse('reply-detail', args=[id]))


@login_required
def create_reply(request, reply_id):
    reply = Reply.objects.get(id=reply_id)
    if request.method == "POST":
        form = ReplyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Reply.objects.create(
                reply_text=data['reply_text'],
                created_by=request.user,
                replied_to=reply.replied_to,
                parent=reply)
            return redirect("post", reply.replied_to.id)
    form = ReplyForm()
    return render(request, "generic_form.html", {"form": form})

@login_required
def initiate_reply(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        form = ReplyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Reply.objects.create(
                reply_text=data['reply_text'],
                created_by=request.user,
                replied_to=post,)
            return redirect("post", post.id)
    form = ReplyForm()
    return render(request, "generic_form.html", {"form": form})  

