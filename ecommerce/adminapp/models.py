from django.db import models
from django.db.models.base import Model

# Create your models here.
class Category(models.Model):
    category=models.CharField(max_length=30)
    status_category=models.TextChoices('status_category','BLOCK UNBLOCK')
    cat_status=models.CharField(default="BLOCK",choices=status_category.choices,max_length=30)

class SubCategory(models.Model):
    subcategory=models.CharField(max_length=50)
    categoryint=models.IntegerField(default=0)
    status_subcategory=models.TextChoices('status_subcategory','BLOCK UNBLOCK')
    subcat_status=models.CharField(default="BLOCK",choices=status_subcategory.choices,max_length=30)

class Product(models.Model):
    categoryindex=models.IntegerField(default=0)
    subcategoryindex=models.IntegerField(default=0)
    productname=models.CharField(max_length=60)
    author=models.CharField(max_length=60,default='None')
    productprice=models.IntegerField(default=0)
    discount=models.IntegerField(default=0)
    discountprice=models.IntegerField(default=0)
    productimage=models.ImageField(upload_to='product/images',null=True,blank=True)
    proddiscription=models.CharField(default='NONE', max_length=100)
    status_prod=models.TextChoices('status_prod','BLOCK UNBLOCK')
    prod_status=models.CharField(default='BLOCK',choices=status_prod.choices,max_length=30)
