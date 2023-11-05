from django.db import models
from product.models import Product
from Authentication.models import User
from django.utils.safestring import mark_safe


# Create your models here.
class DirectsellProduct(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def product_image(self): # new
        return mark_safe('<img src="/../../media/%s" width="150" height="150" />' % (self.product.image))

    def __str__(self):
        return self.product.name