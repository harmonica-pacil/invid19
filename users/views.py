from django.shortcuts import render
from .models import Profile

# Create your views here.
# 9e3c2391-63db-44a4-bcd4-1c12adeb50f3
def profile(request):
    # profile = Profile.objects.get(user=request.user)
    profile = Profile.objects.get(id="00235683-df81-4715-9b74-efcf81c16d92")
    context = {"profile": profile}
    return render(request, "users/profile.html", context)


def edit_profile(request):
    return render(request, "users/edit-profile.html")


def login(request):
    return render(request, "users/login.html")
