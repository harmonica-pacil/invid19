from django.urls import path
from .views import UserRecordView, GetUserView

app_name = "api"
urlpatterns = [
    path("user/create", UserRecordView.as_view(), name="users"),
    path("user/get", GetUserView.as_view(), name="get-user"),
]
