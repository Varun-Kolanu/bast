from django.urls import path
from .views import HomeView, CategoryView

app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<str:category>/', CategoryView.as_view(), name='category')
]
