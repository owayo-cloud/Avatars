from django.db import models
from django.contrib.auth.models import User
import random

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar_url = models.URLField(default="")  # Placeholder for the avatar URL

    def save(self, *args, **kwargs):
        if not self.avatar_url:
            avatars = [
                "https://example.com/avatar1.png",
                "https://example.com/avatar2.png",
                "https://example.com/avatar3.png",
                # Add more URLs for diversity
            ]
            self.avatar_url = random.choice(avatars)
        super(UserProfile, self).save(*args, **kwargs)