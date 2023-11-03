from django.db import models
from product.models import Product
from Authentication.models import User

# Create your models here.
class Trade(models.Model):
    product1 = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product1')
    product2 = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product2')
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2')