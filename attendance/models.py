from django.db import models
from django.conf import settings

# Create your models here.
class Attendance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    position = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.position
