from django.db import models
from enum import Enum
from Authentication.models import User
from django.utils.safestring import mark_safe

# Create your models here.

class Category(Enum):
    MOBILES = 'Mobiles'
    FASHION = 'Fashion'
    BOOKS = 'Books'

    @classmethod
    def get_choices(cls):
        return [(status.name, status.value) for status in cls]

class Status(Enum):
    DIRSELL = 'Direct Sell'
    AUCTION = 'Auction'
    RENT = 'Rent'

    @classmethod
    def get_choices(cls):
        return [(status.name, status.value) for status in cls]

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='product')
    category = models.CharField(
        max_length=20, 
        choices=Category.get_choices()
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20, 
        choices=Status.get_choices(), 
        default=Status.DIRSELL.value
    )
    place = models.CharField(max_length=50)
    upload_date = models.DateTimeField(auto_now_add=True)

    def product_image(self): # new
        return mark_safe('<img src="/../../media/%s" width="150" height="150" />' % (self.image))
    
    def __str__(self):
        return self.name

class Buyer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
