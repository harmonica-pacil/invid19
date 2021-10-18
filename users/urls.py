from django.urls import path
from . import views

urlpatterns = [
    path("profile", views.profile, name="profile"),
    path("edit-profile", views.edit_profile, name="edit-profile"),
    path("profile/json", views.profile_data_json, name="profile-json"),
]
