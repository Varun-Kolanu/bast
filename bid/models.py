from django.db import models
from product.models import Product
from Authentication.models import User

# Create your models here.
class AuctionItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    starting_price = models.IntegerField()
    end_time = models.DateTimeField()
    current_highest_bid = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.product.name

class Bid(models.Model):
    auction_item = models.ForeignKey(AuctionItem, on_delete=models.CASCADE)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bidder.username} bid ${self.amount} on {self.auction_item}"