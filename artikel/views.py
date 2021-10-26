from django.shortcuts import render
from .models import Artikel
from .forms import ArtikelForm
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
from django.core.paginator import Paginator

def index(request):
    posts = Artikel.objects.order_by('tglRilis').reverse()
    paginator = Paginator(posts,4)
    page_number=request.GET.get('page')
    posts_obj=paginator.get_page(page_number)
    response = {'posts':posts_obj}
    return render(request,'artikel_list.html',response)

def artikel_terkini(request):
    posts = Artikel.objects.order_by('tglRilis').reverse()[0:4]
    paginator = Paginator(posts,4)
    page_number=request.GET.get('page')
    posts_obj=paginator.get_page(page_number)
    response = {'posts':posts_obj}
    return render(request,'artikel_terkini.html',response)

def load_more(request):
    offset=int(request.POST['offset'])
    limit=4
    posts = Artikel.objects.order_by('tglRilis')[offset:offset+limit]
    totalData=Artikel.objects.count()
    data={}
    posts_json=serializers.serialize('json',posts)
    return JsonResponse(data={
        'posts':posts_json,
        'totalResult':totalData
    })


@login_required(login_url='login')
def isi_artikel(request,id):
    contents = Artikel.objects.all().get(id=id)
    response = {'contents':contents}
    return render(request,'artikel_detail.html',response)

@login_required(login_url='login')
def add_artikel(request):
    form = ArtikelForm(request.POST or None)
    if (form.is_valid() and request.method=='POST'):
        form.save()
        return HttpResponseRedirect('/artikel')
    
    response = {'form':form}
    return render(request,'artikel_form.html',response)