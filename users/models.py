import uuid
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(
        max_length=500, null=True, blank=True, unique=True
    )
    username = models.CharField(
        max_length=200, null=True, blank=True, unique=True
    )
    bio = models.TextField(null=True, blank=True)
    short_intro = models.TextField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    profile_image = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True,
        default="profiles/default-user.jpeg",
    )

    def __str__(self):
        return str(self.username)
