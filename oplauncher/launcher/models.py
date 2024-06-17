from django.db import models

# Create your models here.
class Quals(models.Model):
    qualName = models.CharField(max_length = 200)
    expDate = models.DateField()
    def __str__(self):
        return f"{self.qualName}"    
