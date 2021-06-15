from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=31)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
