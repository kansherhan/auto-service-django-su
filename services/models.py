from django.db import models
from django.contrib.auth.models import User


class Service(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.URLField()
    detail = models.TextField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=60)
    registered_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserServiceCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service)
