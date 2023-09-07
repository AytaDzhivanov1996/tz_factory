from django.contrib.auth.models import AbstractUser

from django.db import models

from users.managers import CustomUserManager

NULLABLE = {'blank': True, 'null': True}

class User(AbstractUser):
    objects = CustomUserManager()

    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
