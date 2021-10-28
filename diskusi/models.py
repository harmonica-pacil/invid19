from django.db import models
from users.models import Profile

class Forum(models.Model):
    title = models.CharField(max_length=50)
    message = models.TextField()
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE, blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    creator_username = models.CharField(
        max_length=200, null=True, blank=True
    )
    creator_image = models.ImageField(
        blank=True,
        null=True,
        default="profiles/default-user_pfzkxt",
    )

