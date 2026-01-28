from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import *
class User(AbstractUser):
    name = models.CharField(max_length=255)
     



