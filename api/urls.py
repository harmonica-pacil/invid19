from django.urls import path
from .views import *

app_name = "api"
urlpatterns = [
    path("user/create", UserRecordView.as_view(), name="users"),
    path("user/get", GetUserView.as_view(), name="get-user"),
    path("user/profile", GetProfileView.as_view(), name="get-profile"),
    path(
        "user/update-profile",
        UpdateProfileView.as_view(),
        name="update-profile",
    ),
]
