from django.db import models
from django.contrib.auth.models import User


class Service(models.Model):
    name = models.CharField(max_length=100)
    detail = models.TextField()
    price = models.IntegerField()
    file = models.FileField(upload_to='service_files/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ServiceMaster(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_work = models.BooleanField(default=False)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=60)
    registered_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserServiceCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service)
