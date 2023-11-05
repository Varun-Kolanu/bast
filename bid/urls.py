from django.urls import path
from .views import AuctionView, AuctionEditView

app_name = 'bid'

urlpatterns = [
    path('<int:pk>/', AuctionView.as_view(), name='bid' ),
    path('edit/<int:pk>/', AuctionEditView.as_view(), name='auction_edit'),

]
