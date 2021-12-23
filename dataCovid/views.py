from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from dataCovid.forms import KrisanForm
from dataCovid.models import Krisan
import json
import requests
from django.views.decorators.csrf import csrf_exempt

from django.core import serializers





@login_required(login_url="login")
def add_krisan(request):
    context ={}
  
   
    form = KrisanForm(request.POST or None, request.FILES or None)
      
   

    if form.is_valid():
    
        form.save()
        return redirect("/data-covid/")
  
    context['form']= form
    return render(request, "dataCovid.html", context)


@csrf_exempt
def add_krisan_flutter(request):
    body_unicode = request.body.decode('utf-8')
    data = json.loads(body_unicode)
    new_krisan = Krisan(**data)
    new_krisan.save()
    return JsonResponse({
        "success": "Kritik dan saran berhasil terkirim.",
    })