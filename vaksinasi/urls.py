from django.urls import path
from . import views

urlpatterns = [
    path('add-vaksin', views.add_vaksin, name='add-vaksin'),
    path('add-pendaftar', views.add_pendaftar, name='add-pendaftar'),
    path('lihat-vaksin', views.index, name='lihat-vaksin'),
    path('lihat-individu', views.lihat_individu, name='lihat-individu'),
    path('load-more', views.load_more,name='load-more'),
]