from django.urls import path
from .views import ProductCreateView, ProductView, ProductDeleteView

app_name = 'product'

urlpatterns = [
    path('', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/', ProductView.as_view(), name='product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete')
]
