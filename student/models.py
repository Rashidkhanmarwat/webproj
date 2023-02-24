from django.db import models

# Create your models here.
class StdBio(models.Model):
    roll = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    address = models.TextField()
    def __str__(self):
        return self.name