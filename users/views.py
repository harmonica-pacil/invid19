from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from .forms import CustomSignupForm


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
            messages.success(request, "User was logged in!")
            return redirect("main:home")
        else:
            messages.error(request, "Username or password is incorrect")

    return render(request, "users/login.html")


def logoutUser(request):
    logout(request)
    messages.error(request, "User was logged out!")
    return redirect("login")


def signupUser(request):
    if request.user.is_authenticated:
        return redirect("main:home")

    if request.method == "POST":
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "User account was created!")
            return redirect("login")
        else:
            messages.error(
                request, "An error has occurred during registration "
            )

    form = CustomSignupForm()

    context = {"form": form}
    return render(request, "users/signup.html", context)
