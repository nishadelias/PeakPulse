from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    # Additional fields can go here
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Use a unique related_name to avoid clashes
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Use a unique related_name to avoid clashes
        blank=True,
    )