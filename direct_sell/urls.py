from django.urls import path
from .views import DirectSellView, DirectSellEditView, MyDirectSellings

app_name = 'direct_sell'

urlpatterns = [
    path('<int:pk>/', DirectSellView.as_view(), name='direct_sell'),
    path('edit/<int:pk>/', DirectSellEditView.as_view(), name='direct_sell_edit'),
    path('my_direct_sellings/', MyDirectSellings.as_view(), name='my_direct_sellings'),
]
