from django.urls import path
from .views import buat_berita_flutter, index, buat_Berita, index_json, load_lagi, detailberita, index_json, buat_berita_flutter

urlpatterns = [
    path('lihatberita',index, name='lihatberita'),
    path('tambahberita', buat_Berita, name='tambahberita'),
    path('load-lagi', load_lagi, name='load-lagi'),
    path('isi/<int:id>',detailberita,name='detailberita'),
    path('json', index_json, name='json'),
    path('buat_berita_flutter',buat_berita_flutter, name='buat_berita_flutter'),
]