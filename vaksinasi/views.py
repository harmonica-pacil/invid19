from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Vaksin, Pendaftar
from .forms import VaksinForm, PendaftarForm
from django.core.paginator import Paginator
from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

def index(request):
    if 'q' in request.GET:
        q=request.GET['q']
        vaksins=Vaksin.objects.filter(title__icontains=q)
    else:
        vaksins=Vaksin.objects.all()
 
    paginator=Paginator(vaksins,6)
    page_number=request.GET.get('page')
    posts_obj=paginator.get_page(page_number)
    return render(request,'index.html',{'vaksins':posts_obj})

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

def load_more(request):
    offset=int(request.POST['offset'])
    limit=6
    vaksins=Vaksin.objects.all()[offset:limit+offset]
    totalData=Vaksin.objects.count()
    data={}
    vaksins_json=serializers.serialize('json',vaksins)
    return JsonResponse(data={
        'vaksins': vaksins_json,
        'totalResult':totalData
    })

# Load more pagination source https://github.com/codeartisanlab/django-3-crud-application