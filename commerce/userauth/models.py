from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.CharField(verbose_name='country', max_length=255)
    email = models.EmailField(verbose_name='email', unique=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]