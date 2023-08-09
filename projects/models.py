from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    birthDate = models.DateField()
    address = models.CharField(max_length=255)