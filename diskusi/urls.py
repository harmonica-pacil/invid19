from django.urls import path
from .views import index, add_forum, index_json

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_forum, name='add'),
    path('json/', index_json, name='json api'),
]
