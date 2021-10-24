from django.db import models
from users.models import Profile

class Forum(models.Model):
    title = models.CharField(max_length=50)
    message = models.TextField()
    creator = Profile.id
    created_at = models.DateTimeField(auto_now_add=True)

