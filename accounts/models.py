from django.db import models
from django.contrib.auth.models import User

class customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    contact = models.CharField(max_length=13, default='')
    address = models.CharField(max_length=255, default='')
    district = models.CharField(max_length=15, default='')
    pin = models.CharField(max_length=6, default='')


class category(models.Model):
    catid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)

class products(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    discription=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    stock=models.IntegerField(default=0)
    image = models.ImageField(
        upload_to='Images/', default='user_profile1.png', null=True)
    catid = models.ForeignKey(category, on_delete=models.CASCADE,default=1)

class cart(models.Model):
    cartid=models.AutoField(primary_key=True)
    custid = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

class cartproduct(models.Model):
    cartid = models.ForeignKey(cart, on_delete=models.CASCADE, default=1)
    pid = models.ForeignKey(products, on_delete=models.CASCADE, default=1)
    n=models.IntegerField(default=1)

class order(models.Model):
    custid = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    paymenttype = models.CharField(max_length=4)
    deliverystatus = models.BooleanField(default=False,null=True)
    deliverytime = models.DateTimeField(auto_now_add=False,null=True)


class orderproduct(models.Model):
    orderid = models.ForeignKey(order, on_delete=models.CASCADE, default=1)
    pid = models.ForeignKey(products, on_delete=models.CASCADE, default=1)
    n = models.IntegerField(default=1)
