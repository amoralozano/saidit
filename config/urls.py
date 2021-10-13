"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin, auth
from django.urls import path, include
from posts import views as post_view
from group import views
from saidituser import views as user_view
from authorization_app import views as auth_view
from reply import views as reply_view


urlpatterns = [
    path('addpost/', post_view.addPost),
    path('', post_view.index, name='home'),
    path('admin/', admin.site.urls),
    path('addgroup/', post_view.addSubgroup),
    path('groupdetail/<int:id>/', views.group_detail, name='detail'),
    path('login/', auth_view.login_view, name='login'),
    path('logout/', auth_view.logout_view, name='logout'),
<<<<<<< HEAD
    path('signup/', auth_view.signup_view, name='signup'),
    path('accounts/', include('allauth.urls')),

=======
    path("replydetail/<int:reply_id>/", reply_view.ReplyDetailView.as_view(), name="reply-detail"),
    path("post/<int:post_id>/", post_view.PostView.as_view(), name="post"),

    path('signup/', auth_view.signup_view, name='signup'),
    path('follow/<int:id>/', user_view.follow, name="follow"),
<<<<<<< HEAD
    path('unfollow/<int:id>/', user_view.unfollow, name="unfollow")
=======
    path('unfollow/<int:id>/', user_view.unfollow, name="follow")
>>>>>>> main
>>>>>>> 1d84dae303d12d0b59d385f2d675a0f9d5f9d943
]

handler404 = "saidituser.views.handle_not_found"
