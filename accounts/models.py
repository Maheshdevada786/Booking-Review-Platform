
# accounts/models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, blank=True)
    bio = models.TextField(max_length =500, blank=True)

    def __str__(self):
        return self.user.username


