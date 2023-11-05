from django.urls import path
from .views import ProductCreateView, ProductView

app_name = 'product'

urlpatterns = [
    path('', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/', ProductView.as_view(), name='product')
]
