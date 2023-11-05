from django.urls import path
from .views import DirectSellView, DirectSellEditView

app_name = 'direct_sell'

urlpatterns = [
    path('<int:pk>/', DirectSellView.as_view(), name='direct_sell'),
    path('edit/<int:pk>/', DirectSellEditView.as_view(), name='direct_sell_edit'),
]
