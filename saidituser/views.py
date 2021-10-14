from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from saidituser.models import SaidItUser
from django.contrib.auth.models import User
from posts.models import Post

# for the user profile view add user, followers and following for it to be able to function # noqa
@login_required
def follow(request, id):
    self = request.user
    target = SaidItUser.objects.get(id=id)
    self.following.add(target)
    self.save()
    print("followed")
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def unfollow(request, id):
    self = request.user
    target = SaidItUser.objects.get(id=id)
    self.following.remove(target)
    self.save()
    print("unfollowed")
    return redirect(request.META.get('HTTP_REFERER'))

def userview(request, id):
    user = SaidItUser.objects.get(id=id)
    posts = Post.objects.filter(user=user)
    followers = user.followers.all()
    following = user.following.all()
    return render(request, "user_detail.html", {"user": user,
                                                "posts": posts,
                                                "followers": followers, 
                                                "following": following })


def handle_not_found(request, exception):
    return render(request, 'not-found.html')
