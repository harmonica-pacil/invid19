from django.db import models
from diskusi.models import Forum
from users.models import Profile

# Create your models here.

class Comment(models.Model):
    
    message = models.TextField()
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, blank = True, null = True)
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

