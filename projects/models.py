from django.db import models

# Create your models here.


class Address(models.Model):
    id = models.indexes
    street = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip = models.CharField(max_length=10)


class Project(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    birthDate = models.DateField()
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)