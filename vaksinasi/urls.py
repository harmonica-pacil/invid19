from django.urls import path
from . import views

urlpatterns = [
    path('add-vaksin', views.add_vaksin, name='add-vaksin'),
    path('add-pendaftar', views.add_pendaftar, name='add-pendaftar'),
    path('', views.index, name='lihat-vaksin'),
    path('lihat-individu', views.lihat_individu, name='lihat-individu'),
    path('load', views.load, name='load'),
    path('json', views.index_json, name='json'),
    path('add-pendaftar-flutter', views.add_pendaftar_flutter, name='add-pendaftar-flutter'),
    path('add-vaksin-flutter', views.add_vaksin_flutter, name='add-vaksin-flutter'),
]