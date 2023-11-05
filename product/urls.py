from django.urls import path
from .views import ProductCreateView

app_name = 'product'

urlpatterns = [
    path('', ProductCreateView.as_view(), name='product_create')
]
