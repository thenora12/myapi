# Dans myapp/views.py

from django.http import JsonResponse
from .models import Order

def get_orders(request):
    orders = Order.objects.all()
    data = {'orders': list(orders.values())}
    return JsonResponse(data)

