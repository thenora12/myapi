# Dans myapp/urls.py
from msilib import add_data

from django.urls import path
from .views import get_orders

urlpatterns = [
    path('api/orders/', get_orders, name='get_orders'),
    path('add_data/', add_data, name='add_data'),
]
