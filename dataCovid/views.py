from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import response
# from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from dataCovid.forms import KrisanForm
from dataCovid.models import Krisan
import json
import requests


# Create your views here.


@login_required(login_url="login")
def add_krisan(request):
    context ={}
  
    # create object of form
    form = KrisanForm(request.POST or None, request.FILES or None)
      
    # check if form data is valid

    if form.is_valid():
        # save the form data to model
        form.save()
        return redirect("/data-covid/")
    # data = Krisan.objects.all()
    # context['data'] = data
    context['form']= form
    return render(request, "dataCovid.html", context)

def info_provinsi(request):
    lst = {}
    try:
        item = request.GET['q']
    except:
        item = ""
    response = requests.get('https://indonesia-covid-19.mathdro.id/api/provinsi/').json()
    for i in response["data"]:
        if(item.lower() in i["provinsi"].lower()):
            lst = i
    print(lst)
    # print(response)

    return JsonResponse(lst, safe= False)