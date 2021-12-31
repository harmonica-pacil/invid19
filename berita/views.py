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
from django.views.decorators.csrf import csrf_exempt


def index(request):
    posts=Berita.objects.all()
    # Pagintion
    paginator=Paginator(posts,3)
    page_number=request.GET.get('page')
    posts_obj=paginator.get_page(page_number)
    return render(request,'beritalist.html',{'posts':posts_obj})

def index_json(request):
    posts=Berita.objects.all()
    data = serializers.serialize('json', posts)
    return HttpResponse(data, content_type="application/json")

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

@csrf_exempt
# def buat_berita_flutter(request):
#     if request.method == 'POST':
#         body = request.body.decode('utf-8')
#         data = json.loads(body)
#         beritabaru = Berita(**data)
#         beritabaru.save()

def buat_berita_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        judulBerita = data["judulBerita"]
        tanggalRilis = data["tanggalRilis"]
        penulis = data["penulis"]
        spoiler = data["spoiler"]
        isiBerita = data["isiBerita"]
        beritabaru = Berita(**data)
        beritabaru.save()
        return JsonResponse({"status": "success"}, status = 200)
    else:
        return JsonResponse({"status": "error"}, status = 401)

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

