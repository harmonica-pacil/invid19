from django.db import models
from diskusi.models import Forum
from users.models import Profile

# Create your models here.

class Comment(models.Model):
    
    message = models.TextField()
    forum_creator_username = models.CharField(max_length=200, null=True, blank=True)
    forum_creator = models.ForeignKey(Forum, on_delete=models.CASCADE, blank = True, null = True)
    comment_creator = models.ForeignKey(Profile, on_delete=models.CASCADE, blank = True, null = True)
    created_at = models.CharField(max_length=50,null=True, blank=True)
    comment_creator_username = models.CharField(max_length=200, null=True, blank=True)
    creator_image = models.ImageField(
        blank=True,
        null=True,
        default="profiles/default-user_pfzkxt",
    )

