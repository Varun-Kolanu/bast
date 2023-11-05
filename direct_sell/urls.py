from django.urls import path
from .views import DirectSellView

app_name = 'direct_sell'

urlpatterns = [
    path('<int:pk>/', DirectSellView.as_view(), name='direct_sell')
]
