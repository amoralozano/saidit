from django.shortcuts import render
from saidituser.models import SaidItUser
from authorization_app.forms import LoginForm, SignupForm
from django.shortcuts import HttpResponseRedirect, reverse
from django.contrib.auth import login, authenticate, logout


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            auth_user = SaidItUser.objects.create_user(display_name=data['display_name'], username=data['username'], password=data['password']) # noqa
            if auth_user:
                login(request, auth_user, backend='django.contrib.auth.backends.ModelBackend')
                return HttpResponseRedirect(reverse('home'))
    form = SignupForm()
    return render(request, 'generic_form.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,
                                username=data['username'],
                                password=data['password']
                                )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('home',)))

    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
