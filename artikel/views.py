from django.shortcuts import render
from .models import Artikel
from .forms import ArtikelForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    posts = Artikel.objects.all()
    paginator = Paginator(posts,4)
    page_number=request.GET.get('page')
    posts_obj=paginator.get_page(page_number)
    response = {'posts':posts_obj}
    return render(request,'artikel_list.html',response)

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

def search(request):
    if request.is_ajax():
        res = None
        article = request.POST.get('article')
        qs = Artikel.objects.filter(judulArtikel__icontains=article)

        if len(qs) > 0 and len(article) > 0:
            data = []
            for pos in qs:
                item = {
                    'pk': pos.pk,
                    'judulArtikel': pos.judulArtikel,
                    'isiArtikel': pos.isiArtikel,
                    'tglRilis': pos.tglRilis,
                    'peninjau': pos.peninjau,
                    'thumbnail': pos.thumbnail
                }
                data.append(item)
            res = data
        else:
            res = 'Artikel tidak ditemukan'
        return JsonResponse({'data':res})
    return JsonResponse({})

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

def search_flutter(request):
    if 'article' in request.GET:
        article = request.GET.get('article')
        qs = Artikel.objects.filter(judulArtikel__icontains=article)
    else:
        qs = Artikel.objects.all()
    data = serializers.serialize('json', qs)
    return HttpResponse(data, content_type = 'application/json')

@csrf_exempt
def add_flutter(request):
    body = request.body.decode('utf-8')
    data = json.loads(body)
    artikel_baru = Artikel(**data)
    artikel_baru.save()