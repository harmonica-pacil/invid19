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
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.utils.encoding import force_bytes, force_text
from django.core.mail import EmailMessage


@login_required(login_url="login")
def profile(request):
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
                user.is_active = False
                user.save()

                current_site = get_current_site(request)
                mail_subject = "Activate your account."
                message = render_to_string(
                    "users/acc_activate_email.html",
                    {
                        "user": user,
                        "domain": current_site.domain,
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "token": account_activation_token.make_token(user),
                    },
                )
                to_email = form.cleaned_data.get("email")
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()
                messages.success(request, "Please confirm your email address!")

                return redirect("login")
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


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(
            request, "Your account has been activated successfully"
        )
        return redirect("edit-profile")
    else:
        return HttpResponse("Activation link is invalid!")
