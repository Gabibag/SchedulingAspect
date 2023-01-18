from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    IdNumber = models.IntegerField(default=-1)
    Teacher = models.BooleanField(default= False)
    Student = models.BooleanField(default= False)
    