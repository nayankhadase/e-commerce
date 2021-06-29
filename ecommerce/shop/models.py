from django.db import models

# Create your models here.
class Userdata(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=30)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField(max_length=50,default='none')
    status_user=models.TextChoices('status_user','BLOCK UNBLOCK')
    user_status=models.CharField(default='BLOCK',choices=status_user.choices,max_length=20)
    address=models.TextField(default="none")
    mobile_number=models.BigIntegerField(default=0)

class Wishlist(models.Model):
    pid=models.IntegerField(default=0)
    uid=models.IntegerField(default=0)

class Cart(models.Model):
    pid=models.IntegerField(default=0)
    uid=models.IntegerField(default=0)
    qty=models.IntegerField(default=1)

class Buynow(models.Model):
    pid=models.IntegerField(default=0)
    uid=models.IntegerField(default=0)
    qty=models.IntegerField(default=1)


class Orderplace(models.Model):
    pid=models.IntegerField()
    uid=models.IntegerField()
    qty=models.IntegerField()
    price=models.IntegerField()


