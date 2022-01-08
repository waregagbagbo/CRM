from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User,null=True, blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=20,null=True)
    profile_pic = models.ImageField(default="banner.png",null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name
  

class Tag(models.Model):
    name = models.CharField(max_length=200,null=True) 

    def __str__(self):
        return self.name


class  Product(models.Model):
    CAT = (
    ('indoor','indoor'),
    ('outdoor','outdoor')

)
    name = models.CharField(max_length=200,null=True)
    price = models.CharField(max_length=200,null=True)
    category = models.CharField(max_length=200,null=True,choices=CAT)
    description = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
       return self.name 




class Order(models.Model):
    STAT =(
    ('pending','pending'),
    ('out  for delivery','out for delivery'),
    ('delivered','delivery')
)   

    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    status = models.CharField(max_length=200,choices=STAT)
    
    def __str__(self):
        return self.product.name



