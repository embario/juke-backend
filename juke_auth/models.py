from django.db import models
from django.contrib.auth.models import AbstractUser


class JukeUser(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)


class MusicProfile(models.Model):
    name = models.CharField(blank=True, null=True, max_length=200)
    user = models.ForeignKey(JukeUser, on_delete=models.PROTECT, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
