from django.contrib import admin
from .models import DirectsellProduct

# Register your models here.
class DirectsellAdmin(admin.ModelAdmin):
    list_display = ["product", "product_image", "price"]

admin.site.register(DirectsellProduct, DirectsellAdmin)
