from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from .forms import CustomSignupForm, ProfileForm
from datetime import datetime
from django.http import HttpResponse
from django.core import serializers


@login_required(login_url="login")
def profile(request):
    if not request.user.is_authenticated:
        return redirect("login")

    return render(request, "users/profile.html")


@login_required(login_url="login")
def edit_profile(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile was updated!")
            return redirect("profile")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{form.error_messages[msg]}")

    context = {
        "form": form,
        "profile": profile,
        "joined": datetime.strftime(profile.created_at, "%d %B %Y"),
    }
    return render(request, "users/edit-profile.html", context)


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
    messages.info(request, "User was logged out!")
    return redirect("login")


def signupUser(request):
    if request.user.is_authenticated:
        return redirect("main:home")

    if request.method == "POST":
        form = CustomSignupForm(request.POST)
        usernameEx = User.objects.filter(
            username=request.POST["username"]
        ).exists()
        emailEx = User.objects.filter(email=request.POST["email"]).exists()

        if usernameEx:
            messages.error(request, "Username already exists")
        elif emailEx:
            messages.error(request, "Email already exists")
        else:
            if form.is_valid():
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.save()
                messages.success(request, "User account was created!")
                login(request, user)
                return redirect("edit-profile")
            else:
                for msg in form.error_messages:
                    messages.error(request, f"{form.error_messages[msg]}")

    form = CustomSignupForm()

    context = {"form": form}
    return render(request, "users/signup.html", context)


@login_required(login_url="login")
def profile_data_json(request):
    profile = Profile.objects.get(user=request.user)
    data = serializers.serialize("json", [profile])

    return HttpResponse(data, content_type="application/json")
