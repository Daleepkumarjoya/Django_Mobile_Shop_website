from django.db import models


# Create your models here.
class Product(models.Model):
    id = models.AutoField
    image = models.ImageField(upload_to='Shop', default="")
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    Desc = models.CharField(max_length=500)
    publish = models.DateField()
    catogery = models.CharField(max_length=1000, default="Shop")

    def __str__(self):
        return self.name


class Contact(models.Model):
    Msg_id = models.AutoField(primary_key='True')
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=100, default='')
    desc = models.CharField(max_length=1000, default='')

    def __str__(self):
        return self.name


class OrderedBooked(models.Model):
    Order_id = models.AutoField(primary_key='True')
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=100, default='')
    City = models.CharField(max_length=200, default='')
    State = models.CharField(max_length=200, default='')
    address = models.CharField(max_length=1000, default='')

    def __str__(self):
        return self.name


# class User(models.Model):
#     User_id = models.AutoField(primary_key='True')
#     Fname = models.CharField(max_length=100)
#     Lname = models.CharField(max_length=100)
#     email = models.CharField(max_length=100, default='')
#     phone = models.CharField(max_length=100, default='')
#     CreatePassword = models.BigIntegerField()
#
#     def __str__(self):
#         return self.name
