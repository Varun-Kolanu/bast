from django.urls import path
from .views import AuctionView

app_name = 'bid'

urlpatterns = [
    path('<int:pk>/', AuctionView.as_view(), name='bid' )
]
