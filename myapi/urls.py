# Dans myapp/urls.py


from django.urls import path
from .views import get_orders, add_order

urlpatterns = [
    path('api/orders/', get_orders, name='get_orders'),
    path('add_data/', add_order, name='add_data'),
]
