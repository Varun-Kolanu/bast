from django.urls import path
from .views import AuctionView, AuctionEditView, ShowAuctionsView, MyAuctions

app_name = 'bid'

urlpatterns = [
    path('<int:pk>/', AuctionView.as_view(), name='bid' ),
    path('edit/<int:pk>/', AuctionEditView.as_view(), name='auction_edit'),
    path('show_auctions/', ShowAuctionsView.as_view(), name='show_auctions'),
    path('my_direct_sellings/', MyAuctions.as_view(), name='my_auctions'),

]
