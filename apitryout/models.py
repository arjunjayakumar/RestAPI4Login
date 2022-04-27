import email
from django.db import models

# Create your models here.
class test(models.Model):
    name=models.CharField(max_length=20)
    phone=models.CharField(max_length=100)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=8)