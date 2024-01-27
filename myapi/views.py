# Dans myapp/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import requires_csrf_token, csrf_exempt

from .forms import OrderForm
from .models import Order

def get_orders(request):
    orders = Order.objects.all()
    data = {'orders': list(orders.values())}
    return JsonResponse(data)

@csrf_exempt
def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)  # Utilisez votre formulaire pour traiter les données POST
        if form.is_valid():
            form.save()  # Enregistrez la nouvelle commande si le formulaire est valide
            return JsonResponse({"message": "Commande ajoutée avec succès"})
        else:
            return JsonResponse({"error": "Données invalides"})
    else:
        return JsonResponse({"error": "La méthode HTTP doit être POST"})


