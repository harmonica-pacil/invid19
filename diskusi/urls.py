from django.urls import path
from .views import index, add_forum

urlpatterns = [
    path('', index, name='index'),
    path('add', add_forum, name='add'),
]
