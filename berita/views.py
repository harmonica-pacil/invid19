from django.http import response
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import Berita
from .forms import formBerita
from django.core import serializers
import json
from django.http import JsonResponse
from django.core.paginator import Paginator


def index(request):
    posts=Berita.objects.all()
    # Pagintion
    paginator=Paginator(posts,3)
    page_number=request.GET.get('page')
    posts_obj=paginator.get_page(page_number)
    return render(request,'beritalist.html',{'posts':posts_obj})

def detailberita (request,id):
    posts=Berita.objects.all().get(id=id)
    return render(request,'detailberita.html',{'isi':posts})

@login_required(login_url="login")
def buat_Berita(request):
    #buat form baru
    form =  formBerita(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/berita/lihatberita')

    response = {'isiform':form}
    return render(request, "formberita.html", response)

# Load More
# source : https://github.com/codeartisanlab/django-3-crud-application
def load_lagi(request):
    offset=int(request.POST['offset'])
    limit=3
    posts=Berita.objects.all().order_by('tanggalRilis')[offset:limit+offset]
    totalData=Berita.objects.count()
    data={}
    posts_json=serializers.serialize('json',posts)
    return JsonResponse(data={
        'posts':posts_json,
        'totalResult':totalData
    })

