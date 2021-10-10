from django.db import models

# Create your models here.
class donors(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=3)
    phone = models.CharField(max_length=10)
    blood = models.CharField(max_length=5)
class user(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=20)
