from django.shortcuts import render

# Create your views here.
# 9e3c2391-63db-44a4-bcd4-1c12adeb50f3
def profile(request):
    return render(request, "users/profile.html")
