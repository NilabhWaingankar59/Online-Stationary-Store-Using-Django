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


