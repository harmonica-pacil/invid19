from django.urls import path
from .views import index, add_forum, index_json
from comment.views import index as comment_index

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_forum, name='add'),
    path('json/', index_json, name='json api'),
    path('<int:id>', comment_index, name='comment'),
]
