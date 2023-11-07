from django.urls import path
from .views import ProductCreateView, ProductView, ProductDeleteView, ProductChangeStatusView

app_name = 'product'

urlpatterns = [
    path('sell/', ProductCreateView.as_view(), name='product_create'),
    path('show/<int:pk>/', ProductView.as_view(), name='product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('change_status/<int:pk>/', ProductChangeStatusView.as_view(), name='change_status'),
]
