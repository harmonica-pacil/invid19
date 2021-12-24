from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Vaksin, Pendaftar
from .forms import VaksinForm, PendaftarForm
from django.core.paginator import Paginator
from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    if 'q' in request.GET:
        q=request.GET['q']
        vaksins=Vaksin.objects.filter(title__icontains=q)
    else:
        vaksins=Vaksin.objects.order_by('tanggal')
 
    paginator=Paginator(vaksins,6)
    page_number=request.GET.get('page')
    posts_obj=paginator.get_page(page_number)
    return render(request,'index.html',{'vaksins':posts_obj})

def index_json(request):
    if 'q' in request.GET:
        q=request.GET['q']
        vaksins=Vaksin.objects.filter(title__icontains=q)
    else:
        vaksins=Vaksin.objects.order_by('tanggal')
    data = serializers.serialize('json', vaksins)
    return HttpResponse(data, content_type="application/json")

@login_required(login_url="login")
def lihat_individu(request):
    if request.method == 'POST':
        kode1 = request.POST.get("kode")
    pendaftars = Pendaftar.objects.filter(kode=kode1)
    response = {'pendaftars': pendaftars}
    return render(request, 'list_daftar.html', response)

@login_required(login_url="login")
def add_vaksin(request):
    if request.method == 'POST':
        form = VaksinForm(request.POST)
        if form.is_valid():
            form.save() 
            return HttpResponseRedirect('/vaksinasi/lihat-vaksin')    
   
    else:
        form = VaksinForm()
    return render(request, 'form_vaksin.html', {'form': form})

@login_required(login_url="login")
def add_pendaftar(request):
    if request.method == 'POST':
        form = PendaftarForm(request.POST)
        if form.is_valid():
            form.save() 
            Vaksin.objects.get(kode = form.instance.kode).add_pendaftar()
            return HttpResponseRedirect('/vaksinasi/lihat-vaksin') 
    else:
        form = PendaftarForm()
    return render(request, 'form_daftar.html', {'form': request.POST['kode']})

@csrf_exempt
def add_pendaftar_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        kode = data["kode"]
        NIK = data["NIK"]
        nama_lengkap = data["nama_lengkap"]

        form = PendaftarForm(
            kode = kode,
            NIK = NIK,
            nama_lengkap = nama_lengkap
        )
        
        form.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def add_vaksin_flutter(request):
    if request.method == 'POST':
        kode = data["kode"]
        kota = data["kota"]
        provinsi = data["provinsi"]
        lokasi = data["lokasi"]
        jenis_vaksin = data["jenis_vaksin"]
        tanggal = data["tanggal"]
        jam_mulai = data["jam_mulai"]
        jam_berakhir = data["jam_berakhir"]
        kuota = data["kuota"]

        form = VaksinForm(
            kode = kode,
            kota = kota,
            provinsi = provinsi,
            lokasi = lokasi,
            jenis_vaksin = jenis_vaksin,
            tanggal = tanggal,
            jam_mulai = jam_mulai,
            jam_berakhir = jam_berakhir,
            kuota = kuota
        )
        
        form.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)


def load(request):
    offset=int(request.POST['offset'])
    limit=3
    vaksins=Vaksin.objects.order_by('tanggal')[offset:limit+offset]
    totalData=Vaksin.objects.count()
    data={}
    vaksins_json=serializers.serialize('json',vaksins)
    return JsonResponse(data={
        'vaksins': vaksins_json,
        'totalResult':totalData
    })
# Load more pagination source https://github.com/codeartisanlab/django-3-crud-application
