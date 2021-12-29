from django.urls import path
from artikel.views import index, add_artikel, isi_artikel, load_more, search, search_flutter, add_flutter

urlpatterns = [
    path('',index, name='indexArticle'),
    path('add',add_artikel,name='addArticle'),
    path('contents/<int:id>',isi_artikel,name='isiArtikel'),
    path('load-more',load_more,name='load-more'),
    path('search-article',search,name='search-article'),
    path('search_flutter',search_flutter),
    path('add_flutter',add_flutter)
]