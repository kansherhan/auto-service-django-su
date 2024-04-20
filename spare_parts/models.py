from django.db import models
from django.contrib.auth.models import User


class SparePart(models.Model):
    name = models.CharField(max_length=100)
    detail = models.TextField()
    price = models.IntegerField()
    file = models.FileField(upload_to='files/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserSparePartCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    spare_parts = models.ManyToManyField(SparePart)
