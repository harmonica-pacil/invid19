from django.urls import path
from .views import index, json_api

app_name = "comment"
urlpatterns = [
    path('', index, name='index'),
    # path('add/', add_comment, name='add'),
    path('json/', json_api , name='json_api'),
    
]
