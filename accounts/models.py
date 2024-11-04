from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_TYPE = (
        ("administrator", "Administrator"),
        ("employee", "Employee"),
    )
    usertype = models.CharField(
        max_length=20, choices=USER_TYPE, default="administrator"
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username
