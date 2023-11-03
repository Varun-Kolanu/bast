from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "product_image", "description", "image", "category", "owner", "status", "place"]

admin.site.register(Product, ProductAdmin)
