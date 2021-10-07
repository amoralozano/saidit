from django.http.response import HttpResponseRedirect
from django.shortcuts import render, reverse
from posts.forms import AddPostForm
from posts.models import Post
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def addPost(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                user=request.user,
                body=data['body'],
                # time_created=data['time_created']
            )
        return HttpResponseRedirect(reverse('home'))
    form = AddPostForm()
    return render(request, 'generic_form.html', {'form': form})