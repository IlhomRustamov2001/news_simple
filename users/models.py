from django.db import models
from django.contrib.auth.models import AbstractUser #bu model orqali user yaratebmiz

class CustomUser(AbstractUser):#customuser degan user shabloni yaratebmiz
    age=models.PositiveIntegerField(null=True, blank=True)
    address=models.CharField(max_length=200)
    job=models.CharField(max_length=50)

     