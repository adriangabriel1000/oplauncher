from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    id_number = models.CharField(max_length=255, blank=True)
    un_number = models.CharField(max_length=255, blank=True)
    tel_number = models.CharField(max_length=255, blank=True)
    alt_number = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.user.get_full_name()
    