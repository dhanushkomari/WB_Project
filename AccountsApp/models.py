
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser
from App.models import Restaurant
# Create your models here.

class CustomUser(AbstractUser):
    rest = models.OneToOneField(Restaurant, on_delete = models.CASCADE, null = True)
    mobile = models.CharField(max_length = 13, null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'User'
        verbose_name = 'Main User'
    
    def __str__(self):
        return str(self.username)