from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True, null=True)
    age = models.PositiveIntegerField(verbose_name = 'возраст', blank=True, null=True)     
    phone = models.CharField(verbose_name = 'телефон', max_length=20, blank=True, null=True) 
