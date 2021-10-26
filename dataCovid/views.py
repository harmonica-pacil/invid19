from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render
from dataCovid.forms import KrisanForm
from dataCovid.models import Krisan
import json
import requests


# Create your views here.


# @login_required(login_url="login")
def add_krisan(request):
    context ={}
  
    # create object of form
    form = KrisanForm(request.POST or None, request.FILES or None)
      
    # check if form data is valid

    if form.is_valid():
        # save the form data to model
        form.save()
  
    context['form']= form
    return render(request, "dataCovid.html", context)


def info_provinsi(request):
    lst = []
    try:
        item = request.GET['q']
    except:
        item = ""
    response = requests.get('https://api.kawalcorona.com/indonesia/provinsi/').json()
    for i in response:
        if(item.lower() in i["attributes"]["Provinsi"].lower()):
            lst.append(i["attributes"])
    # print(lst)

    return JsonResponse(lst, safe= False)