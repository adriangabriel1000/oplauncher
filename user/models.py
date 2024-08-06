from django.db import models
from django.conf import settings
import os

def get_image_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.user,ext)
    #new_filename = os.rename(filename, "adi.png")
    #return f"profile_pics/{filename}"
    #return f"profile_pics/{instance.user}/{filename}"
    return os.path.join('profile_pics/', filename)


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    id_number = models.CharField(max_length=255, blank=True)
    un_number = models.CharField(max_length=255, blank=True)
    tel_number = models.CharField(max_length=255, blank=True)
    alt_number = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    avatar = models.FileField(upload_to=get_image_name, null=True, blank=True)
    #avatar = models.ImageField(upload_to='profile_pics', blank=True)
    
    def __str__(self):
        return self.user.get_full_name()
    