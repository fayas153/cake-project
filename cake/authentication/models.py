from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class RoleChoices(models.TextChoices):

    USER = 'USER','USER'

    ADMIN = 'ADMIN','ADMIN'

class Profile(AbstractUser):

    role = models.CharField(max_length=20,choices=RoleChoices.choices)

    class Meta:

        verbose_name = 'Profile'

        verbose_name_plural = 'Profile'