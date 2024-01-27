from django.contrib import admin

from myapi.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_entree', 'date_livraison', 'note_livreur', 'note_gestionnaire', 'nom_client', 'tel_client', 'region', 'adresse', 'nom_produit', 'unite', 'prix_propose', 'frais_livraison', 'gains', 'etat_livraison', 'soldee', 'date_added', 'url_order')


# Enregistrez les modèles dans l'interface d'administration
admin.site.register(Order, OrderAdmin)
