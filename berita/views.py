from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout

# def artikel(request):
#     return render(request, "html")

# @login_required(login_url="login")
# def buat_Artikel(request):
#     form = 

#     if request.method == "POST":
#         form =
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Artikel was updated!")
#             return redirect("artikel")

