from django.urls import path
from .views import index, buat_Berita, load_lagi, detailberita

urlpatterns = [
    path('lihatberita',index, name='lihatberita'),
    path('tambahberita', buat_Berita, name='tambahberita'),
    path('load-lagi', load_lagi, name='load-lagi'),
     path('isi/<int:id>',detailberita,name='detailberita'),
]