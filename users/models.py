import uuid
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    ROLES = (
        ("regularUser", "regularUser"),
        ("admin", "admin"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=500, null=True, blank=True)
    username = models.CharField(
        max_length=200, null=True, blank=True, unique=True
    )
    bio = models.TextField(null=True, blank=True)
    short_intro = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    role = models.CharField(
        max_length=50,
        choices=ROLES,
        default="regularUser",
        blank=True,
        null=True,
    )

    profile_image = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True,
        default="profiles/default-user_pfzkxt",
    )
    # profile_image = CloudinaryField("image", blank=True, null=True)

    def __str__(self):
        return str(self.username)
