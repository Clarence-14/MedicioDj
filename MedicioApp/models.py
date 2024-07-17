from datetime import datetime

from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.CharField(max_length=200)
    color = models.CharField(max_length=20)
    description = models.TextField()


def __str__(self):
     return self.name

class Branch(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    manager = models.CharField(max_length=200)
    email = models.EmailField()

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    message = models.CharField(max_length=200)

def __str__(self):
    return self.name

class Appoint(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    date = models.DateField()
    department = models.CharField(max_length=50)
    doctor = models.CharField(max_length=20)
    message = models.TextField()

def __str__(self):
   return self.name


class Member(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

def __str__(self):
    return self.name

