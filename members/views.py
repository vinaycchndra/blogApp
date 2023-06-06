from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm
from .forms import  UserUpdateForm, UpdatePasswordForm
from django.urls import reverse_lazy
from django.urls import reverse

def createUserProfile(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
        else:
            context = {'post': form}
            return render(request, 'registration/registration.html', context)
    form = SignUpForm()
    context = {'post': form}
    return render(request, 'registration/registration.html', context)


def updateUserProfile(request):
    if request.method=='POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('logout'))
        else:
            context = {'post': form}
            return render(request, 'registration/updateProfile.html', context)
    form = UserUpdateForm(instance=request.user)
    context = {'post': form}
    return render(request, 'registration/updateProfile.html', context)


def updatePassword(request):
    if request.method=='POST':
        form = UpdatePasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your password was successfully updated!')
            return redirect(reverse('logout'))
        else:
            context = {'post': form}
            return render(request, 'registration/updatePassword.html', context)
    form = UpdatePasswordForm(request.user)
    context = {'post': form}
    return render(request, 'registration/updatePassword.html', context)


