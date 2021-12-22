from django.urls import path
from .views import index, add_forum, index_json
from comment.views import index as index_comment

urlpatterns = [
    path('', index, name='forum_list'),
    path('add/', add_forum, name='add'),
    path('json/', index_json, name='json api'),
    path('<int:id>', index_comment, name='comment'),
]
