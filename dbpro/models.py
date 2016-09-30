from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length = 50)
    addr = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 20)
    desc = models.CharField(max_length = 200)
    createtime = models.DateTimeField(auto_now_add=True)

class User(models.Model):
    name = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 20)
    desc = models.CharField(max_length = 200)
    createtime = models.DateTimeField(auto_now_add=True)

class Commodity(models.Model):
    name = models.CharField(max_length = 50)
    desc = models.CharField(max_length = 200)
    price = models.FloatField(default = 0)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    available = models.BooleanField(default = True)
    totalbuy = models.IntegerField(default = 0)

class Address(models.Model):
    addr = models.CharField(max_length = 200)
    name = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 20)
    available = models.BooleanField(default = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Cart(models.Model):
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    num = models.IntegerField(default = 1)

class Order(models.Model):
    status = models.IntegerField(default = 0)
    createtime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE)
    addess = models.ForeignKey(Address, on_delete = models.CASCADE)
