from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render, reverse
from django.views.generic.base import View
from group.models import SubGroup
from saidituser.forms import EditProfileForm
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
    following_count = user.following.count()
    followers_count = user.followers.count()
    groups = SubGroup.objects.filter(member=id)
    return render(request, "user_detail.html", {"user": user,
                                                "posts": posts,
                                                "followers": followers, 
                                                "following": following,
                                                "following_count": following_count,
                                                "followers_count": followers_count,
                                                "groups": groups})

def edit_userview(request, id):
    user = SaidItUser.objects.get(id=id)
    
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            user.display_name = data['display_name']
            user.age = data['age']
            user.bio = data['bio']
            user.image = data['image']
            user.save()
            return HttpResponseRedirect(reverse('user-detail', args=(id,)))

    form = EditProfileForm(initial={
        'display_name': user.display_name,
        'age': user.age,
        'bio': user.bio,
        'image': user.image
    })
    return render(request, 'generic_form.html', {'form':form})

class FollowingList(View):
    def get(self, request, id):
        following = SaidItUser.objects.filter(followers=id)
        return render(request, 'following_list.html', {'following':following})

class FollowerList(View):
    def get(self, request, id):
        followers = SaidItUser.objects.filter(following=id)
        
        return render(request, 'followers_list.html', {'followers':followers})


def handle_not_found(request, exception):
    data = {}
    return render(request, 'not-found.html', data )

def error_500(request):
    data = {}
    return render(request,'500.html', data)
