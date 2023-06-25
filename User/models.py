from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(
        verbose_name="email address",
        unique=True,
        max_length=100,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email