# Dans myapp/urls.py

from django.urls import path
from .views import get_orders

urlpatterns = [
    path('api/orders/', get_orders, name='get_orders'),
]
