from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('main.urls'), name='main'),
    path('admin/', admin.site.urls, name='admin'),
    path('auth/', include('Authentication.urls'), name='auth'),
    path('product/', include('product.urls'), name='product'),
    path('direct_sell/', include('direct_sell.urls')),
    path('bid/', include('bid.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
