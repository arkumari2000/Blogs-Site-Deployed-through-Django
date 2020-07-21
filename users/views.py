from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
from .forms import *
from .decorators import *


@decorator
def register(request):
    form = UserCreateForm()
    if request.method == 'POST':
        form = UserCreateForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request, 'You are successfully resgitered')
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'users/register.html', context)


@decorator
def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are successfully logged in')
            return redirect('/')
    return render(request, 'users/login.html')


def userlogout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def profileuser(request):
    if request.method == 'POST':
        form = ProfileUpdate(request.POST, request.FILES,
                             instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your accoutn has been updated')
            return redirect('profile')

    else:
        form = ProfileUpdate(instance=request.user.profile)

    context = {'form': form}
    return render(request, 'users/profile.html', context)
