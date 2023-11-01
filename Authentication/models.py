from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    A User class extending AbstractUser
    """
    address = models.TextField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'email', 'password']

    def __str__(self):
        return self.username