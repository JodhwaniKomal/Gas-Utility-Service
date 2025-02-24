from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.TextField(blank=True, null=True)

    # Fix reverse accessor clash by specifying unique related_name values
    groups = models.ManyToManyField(Group, related_name="custom_user_set", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions_set", blank=True)


# Create your models here.
