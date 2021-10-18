from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile

# Create your views here.
# 9e3c2391-63db-44a4-bcd4-1c12adeb50f3
@login_required(login_url="login")
def profile(request):
    if not request.user.is_authenticated:
        return redirect("login")

    profile = Profile.objects.get(user=request.user)
    context = {"profile": profile}
    return render(request, "users/profile.html", context)


@login_required(login_url="login")
def edit_profile(request):
    return render(request, "users/edit-profile.html")


def loginUser(request):
    if request.user.is_authenticated:
        return redirect("profile")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username or password is incorrect")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("main:home")
        else:
            print("Username or password is incorrect")

    return render(request, "users/login.html")


def logoutUser(request):
    logout(request)
    return redirect("login")
